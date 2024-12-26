# Code supporting Marching into the leadership Pipeline:  Race and Gender in ROTC Participation
#
# 2023-24

import os

# set the  template file path
# we produce interactive HTML by filling in a template which is an HTML file with {{ jinja2_tags }} indicating each place where we will insert 
# content and the {{ name_of_the_key }} in the dictionary we set up below of values to fill in.

# A dictionary entry can contain either text or an interactive graphics.  (In principle, we could combine text and graphics 
# into one dictionary entry, but this seems likely to cause opacity and exciting debugging headaches that giving each concept
# its own descriptive dictionary key would avoid.)

template_directory = r"D:\rjl\docs\socius rotc visualization"
HTML_output_directory = r"D:\rjl\docs\socius rotc visualization"
data_directory = r"D:\rjl\docs\socius rotc visualization"

import markdown
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import scipy

from jinja2 import Template

import pandas as pd

import sys


sys.path.append(r"D:\anaconda3\envs\plotlyeps\Library\usr\bin")

pio.renderers.default = "browser"



# this dictionary maps from variable names to plain English for axis labels
race_string_dict = {
    "black":"identify as Black or African American",
    "hispanic":"identify as Hispanic or Latino",
    "asian":"identify as Asian American, Pacific Islander, or Native Hawaiian",
    "American_Indian_or_Alaska_Native":"identify as American Indian or Alaska Native",
    "female":"are female"
}

# dictionary to keep figures we produce so we can apply formatting in bulk
fig_dict = dict()


# read the main data set
df_campus = pd.read_csv(os.path.join(data_directory, "GAO_105857_ROTC_campus_data.csv"))




# subset the data to just host campuses.  This captures about 80% of commissionees 


# The all male Saint Johns University and the all female College of Saint Benedict share many things including the Saint John's ROTC unit
# GAO reported campus enrollment for just SJU, but combined ROTC enrollment for both schools.  
# Here we add campus enrollment data for the College of Saint Benedict and clarify the institution name to be clear that it reflects the combination of the two campuses

df_campus.loc[df_campus["institution_name"]=="Saint Johns University", "count_institution_female"]=1668
df_campus.loc[df_campus["institution_name"]=="Saint Johns University", "count_ipeds"]+=1668
df_campus.loc[df_campus["institution_name"]=="Saint Johns University", "share_institution_female"]= 100*df_campus.loc[df_campus["institution_name"]=="Saint Johns University", "count_institution_female"] /df_campus.loc[df_campus["institution_name"]=="Saint Johns University", "count_ipeds"]

print(df_campus[df_campus["institution_name"]=="Saint Johns University"][["count_institution_female","count_ipeds", "share_institution_female"]])

df_campus["institution_name"]=df_campus["institution_name"].str.replace("Saint Johns University","Saint John's University and College of Saint Benedict")

# compute the number of officers commissioned from non hosts and hosts to report in the supplement
supplement_jinja_data = {"total_commissioned_from_non_hosts":f'{df_campus[(df_campus["rotc_campus_type"]!="host") & (df_campus["iclevel"]==1) ]["count_commissioned"].sum():,.0f}'}
supplement_jinja_data["total_commissioned_from_hosts"]=f'{df_campus[(df_campus["rotc_campus_type"]=="host") & (df_campus["iclevel"]==1) ]["count_commissioned"].sum():,.0f}'

# we limit the rest of the analysis to 4 year schools, because there are only 3 two year schools that are hosts; they are military junior colleges; and the commissioning data for two year colleges is incomplete
df_campus =df_campus[(df_campus["rotc_campus_type"]=="host") & (df_campus["iclevel"]==1) ]

# compute the total number of women and Black officers commissioned from host units
supplement_jinja_data["ROTC_host_total_women"]=f'{df_campus["count_commissioned_female"].sum():,.0f}'
supplement_jinja_data["ROTC_host_total_Black"]=f'{df_campus["count_commissioned_black"].sum():,.0f}'

# percent of all students who earned a commission
df_campus["pct_commissioned"] = df_campus["count_commissioned"]/(df_campus["count_institution_male"]+df_campus["count_institution_female"])

df_campus["proportion_female_students_commissioned"]=df_campus["count_commissioned_female"]/(df_campus["count_institution_female"])
df_campus["Female ROTC enrollees (percent)"]=100*df_campus["count_rotc_female"]/(df_campus["count_rotc_female"]+df_campus["count_rotc_male"])
df_campus["ROTC completion rate"]=100*df_campus["count_commissioned"]/(df_campus["count_rotc"])
df_campus["ROTC completion rate for female cadets"]=100*df_campus["count_commissioned_female"]/(df_campus["count_rotc_female"])
df_campus["ROTC completion rate for Black cadets"]=100*df_campus["count_commissioned_black"]/(df_campus["count_rotc_black"])
df_campus["pct_male_students_commissioned"]=df_campus["count_commissioned_male"]/(df_campus["count_institution_male"])

# compute the percent of officers commissioned at minority serving institutions who are female before combing that category with 
# all other campuses because it is not materially different from all other campuses and keeping MSIs and All other campuses 
# separate adds complication without much additional insight
supplement_jinja_data["MSI_percent_female"]=df_campus[df_campus["campus_category_unique_for_icons_and_dropdowns"]=="Minority Serving Institutions other than HBCUs and Military Colleges"]["count_commissioned_female"].sum()/df_campus[df_campus["campus_category_unique_for_icons_and_dropdowns"]=="Minority Serving Institutions other than HBCUs and Military Colleges"]["count_commissioned"].sum()
supplement_jinja_data["HBCU_percent_female"]=df_campus[df_campus["campus_category_unique_for_icons_and_dropdowns"]=="Historically Black Colleges and Universities (HBCUs)"]["count_commissioned_female"].sum()/df_campus[df_campus["campus_category_unique_for_icons_and_dropdowns"]=="Historically Black Colleges and Universities (HBCUs)"]["count_commissioned"].sum()
# the percentage is essentially the same for all ROTC hosts and for all other campuses, excluding HBCUs, Military Colleges and MSIs.
supplement_jinja_data["all_host_percent_female"]=df_campus["count_commissioned_female"].sum()/df_campus["count_commissioned"].sum()

# apply human friendly rounding and percentage formatting
for key in ["all_host_percent_female", "MSI_percent_female", "HBCU_percent_female"]:
    supplement_jinja_data[key]=f"{supplement_jinja_data[key]:.1%}"



# Minority Serving Institutions other than HBCUs and Military Colleges do not separate visually from all other
# institutions.  this is a non result we discuss in a footnote in the text.
# Here we combine MSIs and all other institutions
df_campus.loc[df_campus["campus_category_unique_for_icons_and_dropdowns"]=="Minority Serving Institutions other than HBCUs and Military Colleges", "campus_category_unique_for_icons_and_dropdowns"]="All Other Schools"



#### MAKE SUMMARY TABLES

# count counts 1 if it's non missing; zero if the field is missing
summary_df = df_campus.groupby('campus_category_unique_for_icons_and_dropdowns', observed=False).sum().reset_index().copy()
summary_df=summary_df[["campus_category_unique_for_icons_and_dropdowns", "count_institution_female","count_commissioned_female","count_ipeds", "count_institution_male","count_commissioned_male","count_rotc_male", "count_rotc_female", "count_institution_black","count_commissioned_black", "count_rotc_black", "count_commissioned"]]
count_df = df_campus[["campus_category_unique_for_icons_and_dropdowns", "state"]].groupby("campus_category_unique_for_icons_and_dropdowns", observed=False).count().rename(columns={"state":"Number of ROTC host campuses"}).copy()
summary_df= pd.merge(summary_df, count_df, right_on="campus_category_unique_for_icons_and_dropdowns", left_on="campus_category_unique_for_icons_and_dropdowns").reset_index()

# the synonym dict applies reader friendly synonymous language to text that will be presented to readers, while keeping the field names
synonym_dict = {"institution":"students", "rotc":"ROTC enrollees","commissioned":"officers commissioned through ROTC"}
for var_type in ["institution","rotc", "commissioned"]:
    summary_df[f"Male {synonym_dict[var_type]} (percent)"] = summary_df[f"count_{var_type}_male"]/(summary_df[f"count_{var_type}_female"]+summary_df[f"count_{var_type}_male"])
    summary_df[f"Black {synonym_dict[var_type]} (percent)"] = summary_df[f"count_{var_type}_black"]/(summary_df[f"count_{var_type}_female"]+summary_df[f"count_{var_type}_male"])
    summary_df[f"Female {synonym_dict[var_type]} (percent)"] = summary_df[f"count_{var_type}_female"]/(summary_df[f"count_{var_type}_female"]+summary_df[f"count_{var_type}_male"])
# the synonym dict applies reader friendly synonymous language to text that will be presented to readers, while keeping the field names
cat_synonym_dict = {
    "male":"male",
    "female":"female",
    "black":"Black",
}

for var_type in ["male","female", "black"]:
    summary_df[f"Percentage of {cat_synonym_dict[var_type]} students who enroll in ROTC"] = summary_df[f"count_rotc_{var_type}"]/summary_df[f"count_institution_{var_type}"]
    summary_df[f"Percentage of {cat_synonym_dict[var_type]} enrollees who earn a commission"] = summary_df[f"count_commissioned_{var_type}"]/summary_df[f"count_rotc_{var_type}"]

summary_df_original_names = summary_df.copy()

#sorting by Male ROTC enrollees puts HBCUs first, then Military Colleges, then all other schools 
# -- which is the desired order for these tables.
summary_df.sort_values("count_rotc_male", ascending=True, inplace=True)


# apply column headers for output tables
summary_df.rename(columns={
        "campus_category_unique_for_icons_and_dropdowns":"Campus type",
        "count_institution_female":"Female students",
        "count_ipeds":"Total students",
        "count_institution_black":"Black students",
        "pct_institution_female":"Female students (percent)",
        "pct_institution_black":"Black students (percent)",
        "count_rotc_female":"Female ROTC enrollees",
        "count_rotc_male":"Male ROTC enrollees",
        "count_rotc_black":"Black ROTC enrollees",
        "count_commissioned_female":"Female officers commissioned",
        "count_commissioned_male":"Male officers commissioned",
        "count_commissioned_black":"Black officers commissioned",
    },
    inplace=True)

# select subsets of columns that will appear together as a table, then format each as markdown and put them in the jinja dictionary
summary_df_pct = summary_df[["Campus type",
                             "Number of ROTC host campuses",
                             "Total students",
                             "Female students",
                             "Black students",
                             "Female students (percent)",
                             "Black students (percent)"]].copy()


supplement_jinja_data["campus_table"] = summary_df_pct.to_markdown(floatfmt=(".0f",",.0f",",.0f",",.0f", ",.0f", ".1%", ".1%"), index=False)

supplement_jinja_data["rotc_enrollment_table"] = summary_df[["Campus type",
                                                              "Female ROTC enrollees",
                                                              "Male ROTC enrollees",
                                                              "Black ROTC enrollees",
                                                              "Percentage of female students who enroll in ROTC",
                                                              "Percentage of male students who enroll in ROTC",
                                                              "Percentage of Black students who enroll in ROTC",
                                                            ]].to_markdown(floatfmt=(".0f",",.0f", ",.0f", ",.0f",".2%",".2%", ".2%"), 
                                                            index=False)

supplement_jinja_data["rotc_commissioning_table"] = summary_df[["Campus type",
                                                                "Female officers commissioned",
                                                                "Male officers commissioned",
                                                                "Black officers commissioned",
                                                                "Percentage of female enrollees who earn a commission",
                                                                "Percentage of male enrollees who earn a commission",
                                                                "Percentage of Black enrollees who earn a commission"]
                                                                       ].to_markdown(floatfmt=(".0f",",.0f", ",.0f", ",.0f",".1%",".1%", ".1%"), index=False)

# undo the reader friendly renaming so the rest of the code runs
summary_df = summary_df_original_names

# convert the summary tables to HTML
for key in supplement_jinja_data.keys():
    if "table" in key:
        supplement_jinja_data[key] = markdown.markdown(supplement_jinja_data[key], extensions=['tables'])





# KEY INSIGHTS ABOUT HOW TO CUSTOMIZE THE HOVERTEXT WITH ADDITIONAL FIELDS
# per stack overflow https://stackoverflow.com/questions/59057881/python-plotly-how-to-customize-hover-template-on-with-what-information-to-show
###             For Plotly Express, you need to use the custom_data argument when you create the figure. For example:
###
###         fig = px.scatter(
###             data_frame=df,
###             x='ColX',
###             y='ColY',
###             custom_data=['Col1', 'Col2', 'Col3']
###         )
###         and then modify it using update_traces and hovertemplate, referencing it as customdata. For example:
###
###         fig.update_traces(
###             hovertemplate="<br>".join([
###                 "ColX: %{x}",
###                 "ColY: %{y}",
###                 "Col1: %{customdata[0]}",
###                 "Col2: %{customdata[1]}",
###                 "Col3: %{customdata[2]}",
###             ])
###         )
# Plotly express uses the custom_data parameter while  graph objects uses a customdata parameter that captures 
# the same idea, but requires that the input be run thought numpy and list

# check a blended, but mostly 2 year military school that is tiny on the graph
print(f'{df_campus[df_campus["institution_name"]=="Georgia Military College"][["count_institution_female","count_commissioned_female","count_institution_male","count_commissioned_male"]]=}')
print(f'{df_campus[df_campus["institution_name"]=="Georgia Military College"][["share_institution_female", "share_commissioned_female"]]=}')


df_campus["count_commissioned_minority"] = df_campus["count_commissioned"]-df_campus["count_commissioned_white"]
df_campus["count_rotc_races_other_than_black"] = df_campus["count_rotc"]-df_campus["count_rotc_black"]
df_campus["count_commissioned_races_other_than_black"] = df_campus["count_commissioned"]-df_campus["count_commissioned_black"]
assert "count_rotc_female" in summary_df


def make_summary_df(input_df, summary_description):
    
    columns_to_keep_list = list(filter(lambda col_name: "count" in col_name, input_df.columns))

    summary_df= input_df[columns_to_keep_list].copy()
    summary_df = summary_df.copy().agg("sum")
    summary_df["summarized_group"]=summary_description

    print(summary_df["count_ipeds"])

    return summary_df

# this generates a summary series
dod_wide_summary = make_summary_df(df_campus,"DOD Wide")

df_campus["commissionees_from_other_campuses"]= dod_wide_summary["count_commissioned"]-df_campus[f"count_commissioned"]
df_campus["female_commissionees_from_other_campuses"]= dod_wide_summary["count_commissioned_female"]-df_campus[f"count_commissioned_female"]


list_of_rows = []
for n, row in df_campus.iterrows():
    contingency_table_for_row = np.array([[int(row["count_commissioned_female"]*11), int(row["female_commissionees_from_other_campuses"]*11)], [int(row["count_commissioned"]*11), int(row["commissionees_from_other_campuses"]*11)]])
    res = scipy.stats.chi2_contingency(contingency_table_for_row)
    row["p-value female percent commissioned campus vs ROTC as a whole"] = res.pvalue
    list_of_rows.append(row)

df_campus = pd.DataFrame(list_of_rows)


df_campus.rename(columns={"share_institution_female":"Female students (percent)","share_commissioned_female":"Female officers commissioned (percent)"}, inplace=True)    
percent_female_scatterplot = px.scatter(df_campus,
                x=f"Female students (percent)", 
                y=f"Female officers commissioned (percent)",
                color="campus_category_unique_for_icons_and_dropdowns",
                size=f'count_commissioned_female', 
                custom_data = ['institution_name','services_on_campus', 'count_ipeds', 'count_commissioned','count_institution_female','count_rotc_female','count_commissioned_female',"ROTC completion rate","count_rotc", "Female officers commissioned (percent)", "p-value female percent commissioned campus vs ROTC as a whole"],
                category_orders={"campus_category_unique_for_icons_and_dropdowns": ["All Other Schools", "Military Colleges", "Historically Black Colleges and Universities (HBCUs)"] #order so that "All other schools" are on the bottom
                                 },
                #808 px appears to be the maximum possible width of the Sage publications text column, but they do not currently put interactive graphics there
                #needed to set the height smaller to accommodate the source line on a 1920x1080 monitor
                #the scale ratio elsewhere makes the axes 1:1 to 1% on X equals 1% on Y and makes the graph area square.
                height=780,
                width=808,
                #title="Figure S1:  The relationship between student and ROTC-graduate gender",
)




pct_female_students_commissioned_all_hosts=df_campus["count_commissioned_female"].sum()/df_campus["count_institution_female"].sum()
pct_male_students_commissioned_all_hosts=df_campus["count_commissioned_male"].sum()/df_campus["count_institution_male"].sum()

student_body_pct_female = df_campus["count_institution_female"].sum()/(df_campus["count_institution_female"].sum()+df_campus["count_institution_male"].sum())
student_body_pct_male = 1-student_body_pct_female

officers_pct_female = df_campus["count_commissioned_female"].sum()/(df_campus["count_commissioned"].sum())

female_to_male_commissioning_ratio= officers_pct_female*student_body_pct_male/(student_body_pct_female*(1-officers_pct_female))

print(pct_female_students_commissioned_all_hosts)
print(pct_male_students_commissioned_all_hosts)
print(f"{female_to_male_commissioning_ratio=}")



assert "count_rotc_female" in summary_df
assert "campus_category_unique_for_icons_and_dropdowns" in summary_df


print("female difference")

female_comm_rate_diff = (int(dod_wide_summary[f"count_commissioned_female"])/int(dod_wide_summary[f"count_rotc_female"]))-(int(summary_df[summary_df["campus_category_unique_for_icons_and_dropdowns"]=="Historically Black Colleges and Universities (HBCUs)"]["count_commissioned_female"].iloc[0])/int(summary_df[summary_df["campus_category_unique_for_icons_and_dropdowns"]=="Historically Black Colleges and Universities (HBCUs)"]["count_rotc_female"].iloc[0]))
assert female_comm_rate_diff <= 1 and female_comm_rate_diff >= 0
supplement_jinja_data["additional_women_from_HBCU_female_completion_rate_parity"] = int(summary_df[summary_df["campus_category_unique_for_icons_and_dropdowns"]=="Historically Black Colleges and Universities (HBCUs)"]["count_rotc_female"].iloc[0])*female_comm_rate_diff
print(f"{supplement_jinja_data['additional_women_from_HBCU_female_completion_rate_parity']=}")

completion_rate_races_other_than_black = 100*(int(dod_wide_summary["count_commissioned_races_other_than_black"])/(int(dod_wide_summary["count_rotc_races_other_than_black"])))
supplement_jinja_data["completion_rate_races_other_than_black"]=f"{completion_rate_races_other_than_black:0.1f}%"
racial_comm_rate_diff = (completion_rate_races_other_than_black/100)-(int(dod_wide_summary[f"count_commissioned_black"])/int(dod_wide_summary[f"count_rotc_black"]))
print(f"{racial_comm_rate_diff=}")
assert racial_comm_rate_diff <= 1 and racial_comm_rate_diff >= 0
supplement_jinja_data["additional_black_officers_from_black_completion_rate_parity"] = int(dod_wide_summary[f"count_rotc_black"])*(racial_comm_rate_diff)


for key in ["additional_black_officers_from_black_completion_rate_parity", "additional_women_from_HBCU_female_completion_rate_parity"]:
    supplement_jinja_data[key]=f"{supplement_jinja_data[key]:.0f}"




for group in ["female","minority", "black"]:
    df_campus[f"Net contribution of {group} officers"] = df_campus[f"count_commissioned"]*((df_campus[f"count_commissioned_{group}"]/df_campus[f"count_commissioned"])-((int(dod_wide_summary[f"count_commissioned_{group}"])-df_campus[f"count_commissioned_{group}"])/(int(dod_wide_summary[f"count_commissioned"])-df_campus[f"count_commissioned"])))

# capitalize for output
df_campus.rename(columns={"Net contribution of black officers": "Net contribution of Black officers"}, inplace=True)




net_impact_of_host_diversity_scatter_all_other_races_female = px.scatter(
                df_campus, 
                #title="Campus impact on ROTC graduates' racial and gender diversity",
                x="Net contribution of minority officers",
                y="Net contribution of female officers", 
                color=f"campus_category_unique_for_icons_and_dropdowns",
                size=f'count_commissioned_female',
                custom_data = ['institution_name','services_on_campus', 'count_ipeds', 'count_commissioned','count_commissioned_female', "Net contribution of Black officers",],
                category_orders={"campus_category_unique_for_icons_and_dropdowns": ["All Other Schools", "Military Colleges", "Historically Black Colleges and Universities (HBCUs)"]} #order so that "All other schools" are on the bottom
                )

net_impact_of_host_diversity_scatter_all_other_races_female.add_vline(0,line_width=0.5,  line_color="gray")
net_impact_of_host_diversity_scatter_all_other_races_female.add_hline(0, line_width=0.5,line_color="gray")

#Campus level ROTC completion rates for Black and female cadets
completion_rate_scatter = px.scatter(df_campus[(df_campus["count_rotc_black"]>=2) & (df_campus["count_rotc_female"]>=2) ], x="ROTC completion rate for Black cadets", y="ROTC completion rate for female cadets",  color=f"campus_category_unique_for_icons_and_dropdowns",
                        size=f'count_commissioned_female', 
                        custom_data = ['institution_name','services_on_campus', f'count_ipeds', 'count_commissioned',f'count_institution_female',f'count_rotc_female',f'count_commissioned_female', "ROTC completion rate","count_rotc", "Female officers commissioned (percent)", "p-value female percent commissioned campus vs ROTC as a whole"],
                category_orders={"campus_category_unique_for_icons_and_dropdowns": ["All Other Schools", "Military Colleges", "Historically Black Colleges and Universities (HBCUs)"]}, #order so that "All other schools" are on the bottom
                )
# Lines are mean completion rates. Solid lines give each recruit equal weight.<br>The dashed blue lines show the ROTC-wide completion rate for men and for students of races other than Black
completion_rate_scatter.add_vline(100*(int(dod_wide_summary[f"count_commissioned_black"])/int(dod_wide_summary[f"count_rotc_black"])),annotation={"text":"Percentage of<br> Black ROTC cadets<br> who earn a commission"}, annotation_position="bottom left",line_width=0.5,annotation_align="right")
completion_rate_scatter.add_vline(completion_rate_races_other_than_black, line = dict(color='blue', dash='dash'), annotation={"text":"Percentage of <br>non-Black ROTC cadets<br> who earn a commission"}, annotation_position="top right",line_width=0.8,annotation_align="left")
completion_rate_scatter.add_hline(100*(int(dod_wide_summary[f"count_commissioned_female"])/int(dod_wide_summary[f"count_rotc_female"])),annotation={"text":"Percentage of<br> female ROTC cadets<br> who earn a commission"}, annotation_position="bottom right",line_width=0.5, )
completion_rate_scatter.add_hline(100*(int(dod_wide_summary[f"count_commissioned_male"])/int(dod_wide_summary[f"count_rotc_male"])), line = dict(color='blue', dash='dash'),annotation={"text":"Percentage of<br> male ROTC cadets<br> who earn a commission"},line_width=0.8,)

# Lines are mean completion rates. Solid lines give each recruit equal weight.<br>The dashed blue lines show the ROTC-wide completion rate for men and for students of races other than Black

# percent_female_scatterplot.add_trace(go.Scatter(x=list(range(71)), y=[100*(i*female_to_male_commissioning_ratio)/(100-i) for i in range(71)], line_shape='linear', name = f"ROTC percent female if women on all campuses were {female_to_male_commissioning_ratio*100:4.2f}% as likely as men to earn commissions", mode='lines'))

for fig_name in ["percent_female_scatterplot", "completion_rate_scatter"]:
    fig = eval(fig_name)
    if fig_name != "completion_rate_scatter":
        fig.add_trace(go.Scatter(x=[0,70], y=[0,70], line_shape='linear',
                                                        mode='lines', 
                                                        line=dict(width=.7, color="Gray", dash='dot'),
                                                        showlegend = False,
                                                        #we moved the legend entry to the text of the paper, so no longer need it here
                                                        #name = "Women make up the same percentage of students<br> and officers commissioned through ROTC", 
                                                        #legendrank=999 #force this to be the first item in the legend so we can then reverse and make it the last item in the legend
                                                        ))


    fig.update_xaxes(
        range=[0,71],
        constrain="domain",
        dtick = 10
    )

    fig.update_yaxes(
        scaleanchor="x",
        scaleratio=1,
        range=[0,71],
        constrain="domain",
        dtick = 10
    )


df_campus.rename(columns={"proportion_female_students_commissioned":"Female officers commissioned through ROTC each year<br>as proportion of all female students (log scale)"}, inplace=True)

df_campus["Female officers commissioned"]=df_campus["count_commissioned_female"]

# configure the behavior of plotly HTML output in the web browser
config_dict= dict(
            displayModeBar = False,  #False suppresses the plotly zoom and pan tools.
            responsive=False) 


for fig_name in ["percent_female_scatterplot",  "net_impact_of_host_diversity_scatter_all_other_races_female", "completion_rate_scatter"]:
    fig = eval(fig_name)

    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)




    #CUSTOMIZE THE HOVERTEXT THAT POPS UP WHEN THE USER MOUSES OVER EACH POINT ON THE GRAPH
    #for documentation of formatting of the values in the hovertemplate, see:  https://plotly.com/javascript/hover-text-and-formatting/

    if fig_name == "net_impact_of_host_diversity_scatter_all_other_races_female":
        # the net impact mouse over text is different.
        fig.update_traces(hovertemplate="<br>".join([
                "%{customdata[0]}",
                "%{customdata[1]}",
                "Average annual total students:  %{customdata[2]:,.1f}",
                "Average annual graduates commissioned:  %{customdata[3]:.1f}",
                "Annual average female students commissioned:  %{customdata[4]:.1f}" ,
                "Net contribution of female officers:  %{y:.1f}",
                "Net contribution of Black officers:   %{customdata[5]:.1f}", 
                "Net contribution of minority officers:   %{x:.1f}"
                "<extra></extra>"
            ]))
    else:  #if it's not net_impact, apply the standard mouse over text
        fig.update_traces(hovertemplate="<br>".join([
                    "%{customdata[0]}",
                    "%{customdata[1]}",
                    "Average annual total students:  %{customdata[2]:,.1f}",
                    "Average annual total female students:  %{customdata[4]:,.1f}",
                    "Average annual students enrolling in ROTC: %{customdata[8]:.1f}",
                    "Average annual graduates commissioned:  %{customdata[3]:.1f}",
                    "Annual average female students enrolling in ROTC:  %{customdata[5]:.1f}",
                    "Annual average female students commissioned:  %{customdata[6]:.1f}" ,
                    "Female officers commissioned (p-value):  %{customdata[9]:.1f}% (%{customdata[10]:.3f})" ,
                    "We report the p-value for the hypothesis that the proportion",
                    "of female officers commissioned on this campus is equal to",
                    "the proportion commissioned in the rest of the ROTC program." ,
                    "<extra></extra>"
                ])
        )


    fig.data[2]["marker"]["symbol"]="circle"
    fig.data[2]["marker"]["color"]="#2dc1e7"
    fig.data[2]["marker"]["line"]["width"]=1
    fig.data[2]["marker"]["line"]["color"]="black"

    fig.data[1]["marker"]["symbol"]="circle"
    fig.data[1]["marker"]["color"]="#0B6623"
    fig.data[1]["marker"]["line"]["width"]=1
    fig.data[1]["marker"]["line"]["color"]='black'

    fig.data[0]["marker"]["symbol"]="circle"
    fig.data[0]["marker"]["line"]["width"]=1
    fig.data[0]["marker"]["line"]["color"]="#768692"
    fig.data[0]["marker"]["color"]="white"
    fig.add_vline(0, line_width=1.4, line_color="gray")
    fig.add_hline(0, line_width=1.4, line_color="gray")

    # repurpose the tick length parameter to add spacing between
    # the axis label numbers and the axis line
    fig.update_xaxes(ticks="outside",
                    tickcolor="white",  # adjust color of the tick
                    ticklen=4  # adjust length of the tick = distance from axis
                    )
    fig.update_yaxes(ticks="outside",
                    tickcolor="white",  # adjust color of the tick
                    ticklen=4  # adjust length of the tick = distance from axis
                    )
    

    #move the legend to the bottom left of the graph and make it horizontal
    fig.update_layout(
        title=dict(text="Source:  United States Government Accountability Office",
                   yref="container",
                   xanchor="center",
                  #setting y to 0 cuts off the bottom of the Y
                  x=0.5, y=0.005, font=dict(size=12)),
        legend=dict(
            orientation="h",
            yref="container",
            #yanchor="top",
            y=0.03,
            #y=-0.07,
            xanchor="center",
            x=0.5,
            title_text="",
            #put HBCUs first in the legend order, then military colleges second, then all other schools third and the line 4th
            traceorder="reversed"
        ),
        margin=dict(t=1),
        plot_bgcolor='white',
    )

    fig.show()
    #include_plotlyjs="plotly-2.29.1.min.js" implies that there is a copy of plotly-2.29.1.min.js on the web server in the same folder as 
    #the HTML.  That makes efficient use of disk space and means that you are not vulnerable to e.g. Plotly turning off its webserver
    #or to it removing old versions from its webserver.
    supplement_jinja_data[fig_name]=fig.to_html(config=config_dict, include_plotlyjs="plotly-2.29.1.min.js",full_html=False)
    
    #output a version that the journal can insert into their content management system.
    with open(os.path.join(HTML_output_directory, f"{fig_name}.html"), "w") as interactive_graphic_html:
        interactive_graphic_html.write(fig.to_html(config=config_dict, include_plotlyjs="plotly-2.29.1.min.js",full_html=True))







supplement_jinja_data["net_impact_of_host_diversity_scatter_all_other_races_female"]=net_impact_of_host_diversity_scatter_all_other_races_female.to_html(config=config_dict, include_plotlyjs="plotly-2.29.1.min.js",full_html=False)

# # characterize the median institution to compare to small HBCUs

df_campus.shape

supplement_jinja_data["women_commissioned_by_median_ROTC_unit"] = f'{df_campus["count_commissioned_female"].median():.1f}'

supplement_jinja_data["African_Americans_commissioned_by_median_ROTC_unit"] = f'{df_campus["count_commissioned_black"].median():.1f}'


pct_female_students_commissioned_hbcu=df_campus[df_campus["campus_category_unique_for_icons_and_dropdowns"]=="Historically Black Colleges and Universities (HBCUs)"]["count_commissioned_female"].sum()/(df_campus[df_campus["campus_category_unique_for_icons_and_dropdowns"]=="Historically Black Colleges and Universities (HBCUs)"]["count_institution_female"].sum())
pct_female_students_commissioned_not_hbcu=df_campus[df_campus["campus_category_unique_for_icons_and_dropdowns"]!="Historically Black Colleges and Universities (HBCUs)"]["count_commissioned_female"].sum()/(df_campus[df_campus["campus_category_unique_for_icons_and_dropdowns"]!="Historically Black Colleges and Universities (HBCUs)"]["count_institution_female"].sum())
supplement_jinja_data["HBCU_female_commissioning_ratio"]=f"{pct_female_students_commissioned_hbcu/pct_female_students_commissioned_not_hbcu:0.1f}"

pct_male_students_commissioned_hbcu=df_campus[df_campus["campus_category_unique_for_icons_and_dropdowns"]=="Historically Black Colleges and Universities (HBCUs)"]["count_commissioned_male"].sum()/(df_campus[df_campus["campus_category_unique_for_icons_and_dropdowns"]=="Historically Black Colleges and Universities (HBCUs)"]["count_institution_male"].sum())
pct_male_students_commissioned_not_hbcu=df_campus[df_campus["campus_category_unique_for_icons_and_dropdowns"]!="Historically Black Colleges and Universities (HBCUs)"]["count_commissioned_male"].sum()/(df_campus[df_campus["campus_category_unique_for_icons_and_dropdowns"]!="Historically Black Colleges and Universities (HBCUs)"]["count_institution_male"].sum())

supplement_jinja_data["HBCU_male_commissioning_ratio"]=f"{pct_male_students_commissioned_hbcu/pct_male_students_commissioned_not_hbcu:0.1f}"

pct_black_students_enrolled=df_campus["count_rotc_black"].sum()/df_campus["count_institution_black"].sum()
pct_races_other_than_Black_students_enrolled=(df_campus["count_rotc"].sum()-df_campus["count_rotc_black"].sum())/(df_campus["count_ipeds"].sum()-df_campus["count_institution_black"].sum())

supplement_jinja_data["Black_races_other_than_Black_rotc_enrollment_ratio"]=f"{pct_black_students_enrolled/pct_races_other_than_Black_students_enrolled:0.1f}"

pct_black_students_enrolled_HBCU=(df_campus[df_campus["campus_category_unique_for_icons_and_dropdowns"]=="Historically Black Colleges and Universities (HBCUs)"]["count_rotc_black"].sum())/(df_campus[df_campus["campus_category_unique_for_icons_and_dropdowns"]=="Historically Black Colleges and Universities (HBCUs)"]["count_institution_black"].sum())
pct_black_students_enrolled_non_HBCU=(df_campus[df_campus["campus_category_unique_for_icons_and_dropdowns"]!="Historically Black Colleges and Universities (HBCUs)"]["count_rotc_black"].sum())/(df_campus[df_campus["campus_category_unique_for_icons_and_dropdowns"]!="Historically Black Colleges and Universities (HBCUs)"]["count_institution_black"].sum())



supplement_jinja_data["Black_HBCU_not_HBCU_enrollment_ratio"]=f"{pct_black_students_enrolled_HBCU/pct_black_students_enrolled_non_HBCU:0.1f}"

pct_female_students_rotc_hbcu=df_campus[df_campus["campus_category_unique_for_icons_and_dropdowns"]=="Historically Black Colleges and Universities (HBCUs)"]["count_rotc_female"].sum()/(df_campus[df_campus["campus_category_unique_for_icons_and_dropdowns"]=="Historically Black Colleges and Universities (HBCUs)"]["count_institution_female"].sum())
pct_female_students_rotc_not_hbcu=df_campus[df_campus["campus_category_unique_for_icons_and_dropdowns"]!="Historically Black Colleges and Universities (HBCUs)"]["count_rotc_female"].sum()/(df_campus[df_campus["campus_category_unique_for_icons_and_dropdowns"]!="Historically Black Colleges and Universities (HBCUs)"]["count_institution_female"].sum())

supplement_jinja_data["HBCU_female_enrollment_ratio"]=f"{pct_female_students_rotc_hbcu/pct_female_students_rotc_not_hbcu:0.1f}"

pct_male_students_rotc_hbcu=df_campus[df_campus["campus_category_unique_for_icons_and_dropdowns"]=="Historically Black Colleges and Universities (HBCUs)"]["count_rotc_male"].sum()/(df_campus[df_campus["campus_category_unique_for_icons_and_dropdowns"]=="Historically Black Colleges and Universities (HBCUs)"]["count_institution_male"].sum())
pct_male_students_rotc_not_hbcu=df_campus[df_campus["campus_category_unique_for_icons_and_dropdowns"]!="Historically Black Colleges and Universities (HBCUs)"]["count_rotc_male"].sum()/(df_campus[df_campus["campus_category_unique_for_icons_and_dropdowns"]!="Historically Black Colleges and Universities (HBCUs)"]["count_institution_male"].sum())

supplement_jinja_data["HBCU_male_enrollment_ratio"]=f"{pct_male_students_rotc_hbcu/pct_male_students_rotc_not_hbcu:0.1f}"


# Make tables and graphs that discuss heterogeneity within HBCUs
df_hbcu =df_campus[(df_campus["campus_category_unique_for_icons_and_dropdowns"]=="Historically Black Colleges and Universities (HBCUs)")].copy()


df_hbcu=df_hbcu[["institution_name", "count_commissioned", "count_commissioned_male","count_commissioned_female","count_commissioned_black", "count_rotc_female","count_rotc_black","count_rotc", "count_rotc_male","count_ipeds","count_institution_black","count_institution_female","count_institution_male"]].sort_values("count_commissioned").reset_index()

df_hbcu["cum_comm"]= df_hbcu["count_commissioned"].cumsum()

df_hbcu["commissioning size category"]= pd.cut(df_hbcu["count_commissioned"], [0,7,14,21], right=False, labels=["n < 7","7 ≤ n < 14", "14 ≤ n < 21"])

df_hbcu["pct_of_all_commissioned"]=100*df_hbcu["count_commissioned"]/df_hbcu["count_commissioned"].sum()
df_hbcu["pct_of_black_commissioned"]=100*df_hbcu["count_commissioned_black"]/df_hbcu["count_commissioned_black"].sum()
df_hbcu["pct_of_female_commissioned"]=100*df_hbcu["count_commissioned_female"]/df_hbcu["count_commissioned_female"].sum()
df_hbcu["pct_of_all_campuses"]=100/len(df_hbcu["count_ipeds"])
df_hbcu["pct_of_all_rotc_female"]=100*df_hbcu["count_rotc_female"]/df_hbcu["count_rotc_female"].sum()
df_hbcu["pct_of_all_rotc_black"]=100*df_hbcu["count_rotc_black"]/df_hbcu["count_rotc_black"].sum()
df_hbcu["pct_of_all_black_students"]=100*df_hbcu["count_institution_black"]/df_hbcu["count_institution_black"].sum()
df_hbcu["pct_of_all_female_students"]=100*df_hbcu["count_institution_female"]/df_hbcu["count_institution_female"].sum()
df_hbcu["pct_of_all_students"]=100*df_hbcu["count_ipeds"]/df_hbcu["count_ipeds"].sum()

count_df = df_hbcu[["commissioning size category", "institution_name"]].groupby("commissioning size category", observed=False).count().rename(columns={"institution_name":"Number of ROTC host campuses"}).copy()


df_hbcu_summarized = df_hbcu.groupby("commissioning size category", observed=False).agg("sum").reset_index()
df_hbcu_summarized= pd.merge(df_hbcu_summarized, count_df, on="commissioning size category").reset_index()


df_hbcu_summarized["retention_rate_black"] = df_hbcu_summarized["count_commissioned_black"]/df_hbcu_summarized["count_rotc_black"]
df_hbcu_summarized["recruiting_rate_black"] = df_hbcu_summarized["count_rotc_black"]/df_hbcu_summarized["count_institution_black"]
df_hbcu_summarized["pct_students_earning_commission"] = 100*df_hbcu_summarized["count_commissioned"]/df_hbcu_summarized["count_ipeds"]

df_hbcu_summarized["retention_rate_female"] = df_hbcu_summarized["count_commissioned_female"]/df_hbcu_summarized["count_rotc_female"]
df_hbcu_summarized["recruiting_rate_female"] = df_hbcu_summarized["count_rotc_female"]/df_hbcu_summarized["count_institution_female"]

df_hbcu_summarized["retention_rate_male"] = df_hbcu_summarized["count_commissioned_male"]/df_hbcu_summarized["count_rotc_male"]
df_hbcu_summarized["recruiting_rate_male"] = df_hbcu_summarized["count_rotc_male"]/df_hbcu_summarized["count_institution_male"]


supplement_jinja_data["average_female_officers_commissioned_top_third_hbcu"]=f'{(df_hbcu_summarized["count_commissioned_female"].iloc[-1])/(df_hbcu_summarized["Number of ROTC host campuses"].iloc[-1]):.1f}'
print(supplement_jinja_data["average_female_officers_commissioned_top_third_hbcu"])

HBCU_size_category_table=df_hbcu_summarized[["commissioning size category",
                                              "Number of ROTC host campuses",
                                                  "count_institution_female",
                                                  "count_institution_black",
                                                  "count_ipeds",
                                                  "count_commissioned_female",
                                                  "count_commissioned_black",
                                                  "count_commissioned_male",
                                                  ]
                   ].rename(columns={
                    "commissioning size category":"HBCU Size category:  Number of officers commissioned per year",
                    "recruiting_rate_female":"Percentage of female students who enroll in ROTC",
                    "count_institution_female":"Female students",
                    "count_institution_black":"Black students",
                    "count_ipeds":"Total students",
                    "count_commissioned_female":"Female officers commissioned",
                    "count_commissioned_black":"Black officers commissioned",
                    "count_commissioned_male":"Male officers commissioned",}


                    ).to_markdown(floatfmt=(".0f",",.0f",",.0f",",.0f",",.0f", ",.0f",",.0f",",.0f"), index=False)


supplement_jinja_data["HBCU_size_category_table_campus"]= markdown.markdown(HBCU_size_category_table, extensions=['tables'])

HBCU_size_category_table_rotc_rates=df_hbcu_summarized[[
                                                  "commissioning size category",
                                                  "recruiting_rate_female",
                                                  "retention_rate_female",
                                                  "recruiting_rate_black",
                                                  "retention_rate_black",
                                                  "recruiting_rate_male",
                                                  "retention_rate_male",]
                   ].rename(columns={
                    "commissioning size category":"HBCU Size category:  Number of officers commissioned per year",
                    "recruiting_rate_female":"Percentage of female students who enroll in ROTC",
                    "retention_rate_female":"Percentage of female enrollees who earn a commission",
                    "recruiting_rate_black":"Percentage of Black students who enroll in ROTC",
                    "retention_rate_black":"Percentage of Black enrollees who earn a commission",
                    "recruiting_rate_male":"Percentage of male students who enroll in ROTC",
                    "retention_rate_male":"Percentage of male enrollees who earn a commission"}
                    ).to_markdown(floatfmt=(".0f",".2%", ".1%",".2%", ".1%",".2%", ".1%"), index=False)


supplement_jinja_data["HBCU_size_category_table_rotc_rates"]= markdown.markdown(HBCU_size_category_table_rotc_rates, extensions=['tables'])






df_hbcu_summarized = df_hbcu_summarized[["commissioning size category", 
"pct_of_all_female_students",
"pct_of_all_rotc_female",
"pct_of_female_commissioned",
"pct_of_all_black_students",
"pct_of_all_rotc_black",
"pct_of_black_commissioned",
"pct_of_all_campuses",]].rename(columns={
    "pct_of_black_commissioned":"Percentage of all Black officers commissioned",
    "pct_of_female_commissioned":"Percentage of female officers commissioned",
    "pct_of_all_rotc_female":"Percentage of all female enrollees",
    "pct_of_all_rotc_black":"Percentage of all Black enrollees",
    "pct_of_all_black_students":"Percentage of all Black students",
    "pct_of_all_female_students":"Percentage of female students",
    }
).transpose().reset_index()

list(df_hbcu_summarized.iloc[0])

df_hbcu_summarized.columns=list(df_hbcu_summarized.iloc[0])
df_hbcu_summarized=df_hbcu_summarized.iloc[1:]



df_hbcu_summarized

print(df_hbcu_summarized)


cut_points=df_hbcu_summarized[df_hbcu_summarized["commissioning size category"]=="pct_of_all_campuses"].copy()


df_hbcu_summarized=df_hbcu_summarized[df_hbcu_summarized["commissioning size category"]!="pct_of_all_campuses"]


col_list = list(df_hbcu_summarized.columns[1:])
col_list.reverse()


HBCU_production_by_size = make_subplots(rows=1,cols=2)

bar_color_dict = {
    0:"#0a4c6a",
    1:"#1696d2",
    2:"#a2d4ec",
}

for bar_number, col in enumerate(col_list):

    for col_number, type in enumerate(["female", "Black"]):
        df_to_plot = df_hbcu_summarized[df_hbcu_summarized['commissioning size category'].str.contains(type)]
        HBCU_production_by_size.add_trace(go.Bar(
            x=df_to_plot['commissioning size category'],
            y=df_to_plot[col],
            name=str(col),
            marker_color=bar_color_dict[bar_number],
            showlegend=(col_number==0),
            hoverinfo='none'  #by default, the hover info reported too many decimal places.  This turns it off
            #hover_data={df_to_plot[col]:':.1f'}
            ),
            row=1,
            col=col_number+1


        )

HBCU_production_by_size.add_hline(100-32.14,line_color="gray")
HBCU_production_by_size.add_hline(100-32.14-35.71,line_color="gray")

HBCU_production_by_size.update_layout(
        #title="Percentage of HBCU students, ROTC cadets, and commissionees by Campus ROTC size category<br>Horizontal lines show the percentage of campuses in each category",
        title="Horizontal lines show the percentage of campuses in each category",
        barmode='stack',
        legend_title_text='Campus ROTC size category:<br> Number of officers<br> commissioned per year',
        plot_bgcolor='white',
    )

HBCU_production_by_size.show()

supplement_jinja_data["production_of_African_Americans_and_women_by_HBCU_size_figure"]= HBCU_production_by_size.to_html(config=config_dict, include_plotlyjs="plotly-2.29.1.min.js",full_html=False)

#full_html should be True for standalone, graph only output files linked from Sage and false for interactive graphics that will be inserted 
# into author supplied markdown or HTML
with open(os.path.join(HTML_output_directory, "HBCU_production_by_size.html"), "w") as interactive_graphic_html:
        interactive_graphic_html.write(HBCU_production_by_size.to_html(config=config_dict, include_plotlyjs="plotly-2.29.1.min.js",full_html=True))


# insert the graphics, tables, and numbers into the template.

#we moved the main paper to LaTeX to fit into the Sage submission system and did not integrate the final changes into the markdown
#input_template_path = os.path.join(template_directory, "marching into the leadership pipeline.md")
#output_html_path = os.path.join(template_directory,"marching into the leadership pipeline.html")
#with open(output_html_path, "w", encoding="utf-8") as output_file:
#    with open(input_template_path, encoding="utf-8") as template_file:
#        j2_template = Template(markdown.markdown(template_file.read(), extensions=['footnotes']))
#        output_file.write(j2_template.render(supplement_jinja_data))


input_template_path = os.path.join(template_directory, "supplement.md")
output_html_path = os.path.join(template_directory,"ROTC_supplement.html")
with open(output_html_path, "w", encoding="utf-8") as output_file:
    with open(input_template_path, encoding="utf-8") as template_file:
        j2_template = Template(markdown.markdown(template_file.read(), extensions=['footnotes']))
        output_file.write(j2_template.render(supplement_jinja_data))

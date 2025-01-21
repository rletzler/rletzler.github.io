<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<style>
@page {
  size: 210mm 297mm; 
  /* Chrome sets own margins, we change these printer settings */
  margin: 27mm 16mm 27mm 16mm; 
}
    img {
        width: 100%;
    }

  table {
  border-collapse: collapse;
}

td, th {
  border: 1px solid black;
  padding: 6px;
  font-size: 75%;
}

</style>
</head>
# Supplementary material for "Marching into the leadership pipeline"

Robert Letzler, Signe Janoska-Bedi, and Andrew Penner

Our supplement also includes [code](https://allorama.org/marching.py) and the [markdown necessary to run that code.](https://marching-into-the-leadership-pipeline.github.io/supplement.md).  [The supplement published in Socius](https://journals.sagepub.com/doi/suppl/10.1177/23780231241297776/suppl_file/sj-pdf-1-srd-10.1177_23780231241297776.pdf) contains the definitive supplement text.  It varies slightly from the draft produced by this markdown file.  We have published this file so that interested readers can run and understand our code.

# Putting Female and Black HBCU ROTC participants in context

The demographics of the officers ROTC commissions are shaped by characteristics of the ROTC program, student propensity to serve, ROTC unit locations, recruiting efforts, operating decisions that affect cadet retention, and the attractiveness of military service.   ROTC and university decisions affect which campuses host units and thus the demographics of students ROTC can recruit. Military policies, the social standing of servicemembers and veterans, and the network of veterans in the job market affect the attractiveness of ROTC.  Unit recruiting efforts, reputations, and cadet social networks affect which students on host campuses enroll. Finally, campus-enrollee and unit-enrollee interactions affect which students remain on campus and in the ROTC program until they earn a commission.

The supplement begins with additional background about the role of officers in the military and veterans in society.  Then the supplement digs into the process that produced the main graphic's finding about the relationship between host campus and commissionee characteristics, what that relationship means, and what additional research can shed light on the dynamics at play.  We work through data on campus demographics, enrollment, and retention that drive our central result step-by-step.  We describe the implications of campus level demographics for overall ROTC diversity and discuss the variation among HBCUs.  Finally, we describe the public data we used that is available for further scholarship.

## The impact of officer status on the military, the workforce, and individuals

Officers are leaders. They make consequential decisions for 2.5 million servicemembers (Department of Defense, 2023) and become members of a substantial professional community of current- and former-servicemembers.  When they leave active duty, they get veterans' preference for government jobs and contracts.  Benefits of military service include retirement programs and pensions; lifelong healthcare; and the Montgomery and Post-9/11 GI Bills which, among other things, pay for education and subsidize mortgages. [^b] As of 2023, there were 8.4 million veterans in the civilian workforce (Bureau of Labor Statistics, 2024). Veterans play a significant role in economic sectors like law enforcement, government, and aviation.  Twenty-two percent of US law enforcement officers and approximately one-third of US commercial pilots are veterans (Lewis and Pathak 2014, Van Dam 2018). [^most_pilots_are_officers]


[^b]:  For a broader discussion on the benefits of military service, see Mettler, 2005, Frydl, 2009, and Mittelstadt, 2015.

[^most_pilots_are_officers]: All Air Force, Navy, and Marine pilots are officers (Air Force, 2024; Marine Corps, 2024; and Navy, 2024), while Army pilots are a blend of officers and warrant officers (Army 2024A and 2024B).


<!--p style="page-break-after: always;">&nbsp;</p>
<p style="page-break-before: always;">&nbsp;</p-->


## Data about campuses, enrollment and retention.  

The following tables explore the process of ROTC participation from campus selection to enrollment to commissioning.

In interpreting these tables, note that:

- The GAO data counts students every year they are taking classes, but only counts ROTC enrollees in the year that they first enroll and ROTC commissionees the year they earn a commission.  A hypothetical school where everyone enrolls in ROTC and graduates in four years would thus appear in our data to have four times more students than ROTC enrollees.  There are contexts in which it would be natural to consider the number of students enrolling in ROTC as a percentage of the campus's incoming freshman class and the number of commissionees graduating from ROTC as a percentage of the number of bachelor's degree recipients.  The data GAO published does not allow us to make those computations.  

- The largest ROTC programs are at a handful of schools, the senior military colleges.  The senior military colleges are members of the Association of Military Colleges and Schools of the United States.  The statistics we report for this category blend three small, heavily male schools with a combined enrollment of about 7,000 students (the Citadel, the Virginia Military Institute, and Norwich University) with large schools like Texas A&M, Virginia Tech, and the University of North Georgia.  Over 40% of students at the Citadel, the Virginia Military Institute, and Norwich University enroll in ROTC while a smaller percentage of students enrolls in ROTC at the large senior military colleges.  The results below give each student or enrollee equal weight, so the large campuses drive the results that show the senior military colleges are relatively gender balanced and that under 4% of male students enroll in ROTC there.  The situation at the three military colleges with smaller student bodies is substantially different.  These schools -- the Citadel, the Virginia Military Institute, and Norwich University -- are home to the second, third, and fourth largest ROTC programs.  Officers earning a commission at the Citadel, the Virginia Military Institute, and Norwich University graduate from universities with student bodies that are 11%, 11%, and 24% female, respectively.  ROTC graduates become leaders in a military that is 18% female (Department of Defense 2023).  Officers earning a commission at the Citadel, the Virginia Military Institute, and Norwich University graduate from universities with student bodies that are 22%, 19%, and 26% minority, respectively.  ROTC graduates become leaders in a military that is 31% minority (Department of Defense 2023). By contrast, Texas A&M has the largest ROTC unit and a student body that is 48% female and 35% minority.    

- Variation among HBCUs is important.  The largest HBCU ROTC units -- at Norfolk State, Hampton and Tuskegee Universities -- produce about five times more officers, female officers, and Black officers than the smallest HBCU ROTC-host campuses.  We discuss this heterogeneity in detail in the “Variation among HBCU host units” section, below.

- We report only students pursuing degrees at a 4 year ROTC-host campus and do not report students who are pursuing degrees at nearby schools that have crosstown agreements with the units we analyze.  (“Crosstown agreements” allow students to pursue a degree on one campus and participate in ROTC on another campus.) The GAO data does not report which host unit provided the military education to the crosstown students, and crosstown campus enrollments are often quite small, so the crosstown data are both less complete and less statistically precise than the host unit data.  We exclude crosstown students from this analysis.  Crosstown units may be ripe for future analysis, since they expose enrollees to the demographics and culture of one campus and the ROTC unit culture and demographics from another.

### Demographics Characteristics

HBCUs represent about 9% of all host campuses, enroll about 3% of all students and produce about 4% of all commissionees and 7% of all female commissionees.  Roughly one in four Black students on ROTC-host campuses attend an HBCU and 38% of all Black officers earning a commission at an ROTC-host campus attended an HBCU.

{{ campus_table }}

### ROTC enrollment

Black students attending ROTC-host campuses are {{ Black_races_other_than_Black_rotc_enrollment_ratio }} times as likely to enroll in ROTC as non-Black students.  Black students at HBCUs are {{ Black_HBCU_not_HBCU_enrollment_ratio }} times as likely to enroll in ROTC as Black students at all other non-military colleges.  Female students at HBCUs are {{ HBCU_female_enrollment_ratio }}  times as likely to enroll in ROTC and {{ HBCU_female_commissioning_ratio }} times as likely to earn an ROTC commission as female students at other schools, while male students at HBCUs are {{ HBCU_male_enrollment_ratio }} times as likely to enroll as men at other schools and {{ HBCU_male_commissioning_ratio }} times more likely to earn a commission.  

{{ rotc_enrollment_table }}

There are few other obvious patterns among schools that produce high or low percentages of female officers.  Non-HBCU schools notable for commissioning high percentages of women include the University of Pennsylvania, the University of Scranton, Loyola University of Chicago, and Texas Christian University.  Similarly, non-military colleges that have majority female campuses but extremely heavily male ROTC programs include the University of Nebraska Omaha, Providence College, Utah State, and CUNY City College.

### Retention of ROTC enrollees until they earn a commission

Black cadets are less likely to finish the program than non-Black cadets and Black students are thus underrepresented among ROTC commissionees.  If Black cadets earned commissions at the same rate as non-Black cadets, ROTC would commission {{ additional_black_officers_from_black_completion_rate_parity }} more Black officers per year.  Given the high number of Black cadets at HBCUs, it is not surprising that female cadets at HBCUs have lower completion rates than female cadets at other schools.  If female cadets who enrolled in ROTC at HBCUs earned commissions at the same rate as female cadets at other schools, ROTC would commission {{ additional_women_from_HBCU_female_completion_rate_parity }} more female officers per year.  We do not have enough data to explore the relative role of cadet race, cadet gender, and campus characteristics in this difference.  Individual-level data, and particularly information about when and why enrollees leave ROTC, would help interpret and address racial and gender differences in attrition.

{{ rotc_commissioning_table }}

Figure S1 shows the substantial variation among campuses in the completion rates for Black and female cadets.  We restrict Figure S1 to campuses where ROTC enrolled an average of at least 2 female cadets and 2 Black cadets per year over our 11-year study period to ensure adequate sample size for completion rate estimates.  Figure S1 shows that several HBCUs commission women at rates higher than the ROTC-wide average and that some ROTC-host campuses commission Black students at rates similar to or higher than the ROTC-wide completion rates for non-Black students, {{ completion_rate_races_other_than_black }}.  HBCUs commission a slightly higher percentage of Black enrollees than other campuses, but men and women who enroll in ROTC at HBCUs are less likely to earn commissions than their peers at other colleges.  These graduation-rate-by-gender estimates do not adjust for race.  Our data do not allow us to compute the rate of completion for gender and race simultaneously (e.g., we cannot examine the completion rate of Black women by campus type).  

Throughout this document, there are links to interactive versions of our graphics that show campus details when the mouse pointer hovers over the school's marker.  Throughout this document, the bubble sizes show the number of female students commissioned from each unit.


<!--p style="page-break-after: always;">&nbsp;</p>
<p style="page-break-before: always;">&nbsp;</p-->

### Figure S1:  Campus level ROTC completion rates for Black and female cadets
([Interactive version](https://allorama.org/completion_rate_scatter.html))
{{ completion_rate_scatter }}

Figure S2 shows the impact of specific campuses on ROTC diversity. Specifically, it reports how the number of female commissionees and the number of commissionees of color would change if we replaced the students earning commissions from each ROTC unit with a group of the same size with the gender and racial composition of the combined commissionees of all other ROTC programs.  The text that pops up when the mouse pointer hovers over each dot also reports that campus's net impact on the number of Black officers commissioned.  Units in the top right add gender and racial diversity.  Some HBCUs stand out because they add both racial and gender diversity.  Other heavily Asian or Latino campuses add racial diversity, but most have little effect on gender diversity because their gender ratios are similar to ROTC as a whole.[^MSI]  Units in the bottom left reduce overall diversity.  ROTC is heavily white and male, so units with a large negative impact on both gender and racial diversity necessarily enroll both a large number of cadets and a higher percentage of white men than the ROTC-wide average. 

[^MSI]:  The cohort of officers earning commissions from non-HBCU minority-serving institution host campuses – such as the University of Texas at San Antonio and the University of Guam -- is 25.8% female, while the officers completing ROTC at all host campuses are 22.1% female and officers commissioned from HBCUs are 38.5% female.  The GAO data and report subdivide the "all other schools" category we report into a "minority-serving institutions" category and an "all other schools" category that excludes minority-serving institutions.  The GAO data categorizes a non-HBCU institution of higher education as a Minority-Serving Institution (MSI) if its “enrollment of a single minority is over 25 percent of total enrollment or a combination of minorities is over 50 percent of total enrollment” (Government Accountability Office 2023 p. 10).

### Figure S2:  Campus impact on ROTC graduates' racial and gender diversity
([Interactive version](https://allorama.org/net_impact_of_host_diversity_scatter_all_other_races_female.html))
{{ net_impact_of_host_diversity_scatter_all_other_races_female  }}


## Variation among HBCU host units

Figure S2 shows that some HBCU campuses make a net annual contribution of about a dozen additional minority officers and two additional female officers relative to what we would expect for a unit of their size, while others contribute fewer than two additional minority officers and close to zero additional female officers. This variation reflects differences in HBCU student bodies and ROTC enrollment and retention patterns.  While the majority of students at most HBCU campuses are Black and female, Morehouse is all male and only 26% of students at West Virginia State (an HBCU) are Black.  Variation in the number of officers who graduate from HBCUs is a particularly important source of the variation in HBCU impact.  In Figure S3 we provide information separately for the 9 HBCU host campuses that produce at least 14 officers per year, the 10 campuses producing at least 7 and fewer than 14 officers per year, and the 9 campuses producing fewer than 7 officers per year.  We explore the characteristics of those campuses and their ROTC units in the table below and in Figure S3.  The HBCU host campuses that produce the fewest officers have smaller student bodies, lower enrollment rates, and lower completion rates.

### Figure S3 :  Percentage of HBCU students, ROTC cadets, and commissionees by Campus ROTC size category
([Interactive version](https://allorama.org/HBCU_production_by_size.html))
{{ production_of_African_Americans_and_women_by_HBCU_size_figure  }}

{{ HBCU_size_category_table_campus }}

{{ HBCU_size_category_table_rotc_rates }}

HBCU campuses in the lowest commissioning category often produce fewer female officers than the ROTC-wide median host unit, which commissions {{ women_commissioned_by_median_ROTC_unit }} women per year, while campuses in the top third of HBCUs commission an average of {{ average_female_officers_commissioned_top_third_hbcu }} women per year. [^prod]  All HBCU host campuses commission more Black officers than the ROTC-wide median host unit, which produced an average of {{ African_Americans_commissioned_by_median_ROTC_unit }} Black officers per year over the 11 year study period.  While Figure S2 highlights what would happen if the United States Department of Defense (DOD) shifted individual scholarships and recruiting or retention efforts among campuses, this look at medians begins to address what would happen if DOD moved host units to new campuses.  Replacing one of these small host units with one that commissioned the ROTC median cohort would produce more officers and more female officers, even if it led to a small reduction in the percentage of officers who complete ROTC who are female since it would produce even more male officers.  It is also important to put these small units in the context of a program that, during an average year between 2011-2022, commissioned {{ total_commissioned_from_hosts }} officers per year from  host campuses[^crosstown_officers], including {{ ROTC_host_total_women }} women and {{ ROTC_host_total_Black }} Black officers.  Exploring the assignment of ROTC units to campuses is beyond the scope of this paper.  It is also important to note that there are only three four-year HBCUs with enrollment over 5,000 students that do not currently host an ROTC unit, so that there are few opportunities to increase the number of female and Black officers commissioned by placing additional ROTC-host units on HBCU campuses. [^three_large_HBCUs_are_crosstowns] 

[^crosstown_officers]:  ROTC commissioned another {{ total_commissioned_from_non_hosts }} officers from 4 year crosstown campuses.  
[^three_large_HBCUs_are_crosstowns]: The three four-year HBCUs with enrollment over 5,000 students that do not currently host an ROTC unit (Albany State University, North Carolina Central University, and Texas Southern University) have relatively strong “crosstown” arrangements that allow their students to participate in ROTC programs hosted at nearby universities. The diversity benefits of adding host units at these campuses would be limited to the officers who would not have earned commissions through the crosstown arrangement.

[^prod]:  The GAO study discusses ROTC unit productivity and DOD criteria for the number of graduates per year required for units to be considered "viable".


# Data source

We use data on student bodies, ROTC enrollment and ROTC commissioning between 2011 to 2021 at 4 year colleges and universities that host ROTC units drawn from a [public data set](https://files.gao.gov/interactive/data/105857/GAO-23-105857-ROTC-Diversity-data-documentation-tab-is-in-excel-sheet.zip) published as part of GAO’s 2023 report, [“Senior Reserve Officers’ Training Corps: Actions Needed to Better Monitor Diversity Progress.”](https://www.gao.gov/products/gao-23-105857)  GAO aggregated that data from non-public DOD files and combined it with 11 years of data from the Department of Education Integrated Postsecondary Education Data System (IPEDS).  The public GAO data do not provide racial breakdowns by gender, which limits our analysis.  The public GAO data does not report campus-level trends or variation over time, although the GAO report analyzed program-wide time trends and shows that ROTC commissioned more female and minority officers at the end of the period than at the beginning.  That report provides context for our focused look at the role of HBCUs in ROTC gender diversity.  It performs broader analysis, including considering the role of minority-serving institutions and ROTC crosstown units.

We exclude students with crosstown enrollments throughout this analysis, and our results discuss only students who pursue degrees and participate in ROTC on the same host campus.  We also exclude the three two-year military schools that are host campuses because the commissioning data for two-year schools is not comparable to the commissioning data for four year schools.  

# Works Cited

Air Force, United States. (2024). Careers > Aviation and Flight > Pilot. [https://www.airforce.com/careers/aviation-and-flight/pilot](https://www.airforce.com/careers/aviation-and-flight/pilot)  Retrieved April 7, 2024.

Army, United States. (2024A). Aviation Officer.  [https://www.goarmy.com/careers-and-jobs/career-match/aviation/managing-piloting-aircraft/15a-aviation-officer.html](https://www.goarmy.com/careers-and-jobs/career-match/aviation/managing-piloting-aircraft/15a-aviation-officer.html)  Retrieved April 7, 2024.

Army, United States. (2024B). Fixed Wing Aviator Warrant Officer.  [https://www.goarmy.com/careers-and-jobs/career-match/aviation/managing-piloting-aircraft/155a-fixed-wing-aviator-warrant-officer.html](https://www.goarmy.com/careers-and-jobs/career-match/aviation/managing-piloting-aircraft/155a-fixed-wing-aviator-warrant-officer.html) Retrieved April 7, 2024.

Bureau of Labor Statistics. (2024).  Table A-5. Employment status of the civilian population 18 years and over by veteran status, period of service, and sex, not seasonally adjusted. [https://www.bls.gov/news.release/empsit.t05.htm](https://www.bls.gov/news.release/empsit.t05.htm), March 8, 2024 version.

Department of Defense. (2023). 2022 Demographics Report  [https://download.militaryonesource.mil/12038/MOS/Reports/2022-demographics-report.pdf](https://download.militaryonesource.mil/12038/MOS/Reports/2022-demographics-report.pdf)  November 29, 2023

Frydl, Kathleen. (2009). The GI bill. Cambridge University Press.

Government Accountability Office. (2023). Senior Reserve Officers’ Training Corps: Actions Needed to Better Monitor Diversity Progress.  GAO-23-105857.

Lewis, G. B., & Pathak, R. (2014). The employment of veterans in state and local government service. _State and Local Government Review_, 46(2), 91-105.  

Marine Corps, United States. (2024). Marine Corps Aviation.  [https://www.mcrc.marines.mil/Portals/95/E-O/Naval%20Programs/Aviation%20Information/Marine%20Corps%20Aviation%20Brief.pdf?ver=q3z2dAQDcdL31yQ5Rhwi0g%3d%3d](https://www.mcrc.marines.mil/Portals/95/E-O/Naval%20Programs/Aviation%20Information/Marine%20Corps%20Aviation%20Brief.pdf?ver=q3z2dAQDcdL31yQ5Rhwi0g%3d%3d)  Retrieved April 7, 2024.

Mettler, Suzanne. (2005). Soldiers to citizens: The GI Bill and the making of the greatest generation. Oxford University Press.

Mittelstadt, Jennifer. (2015). The Rise of the Military Welfare State. Harvard University Press.

Navy, United States. (2024).  Careers > Aviation > Fixed Wing Pilot. [https://www.navy.com/careers-benefits/careers/aviation/fixed-wing-pilot](https://www.navy.com/careers-benefits/careers/aviation/fixed-wing-pilot) Retrieved April 7, 2024.

Van Dam, Andrew. (2018).  What are the odds of a former fighter pilot being at the controls of your plane? _The Washington Post_  April 20, 2018.

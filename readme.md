# Sales Data Dashboard + Weather

## Overview

This is a project unifying a Tableau-based dashboard showcasing insights from a year of sales data with ML model insights using historical weather data.

## Status:
This project is still under development. But feel free to see the insanity of simulating full outer joins in MySQL

## Data Sources: 
Weather data was sourced from Open-Meteo.

Sales data for this project was adapted with permission from real sales data that was scaled and anonymized. 
Missing values were imputed using dynamic proportional distribution imputation. 

1. All weeks with full sales data were partitioned by week and weekday to find the average percentage of sales per day of the week.


2. This was then dynamically applied to impute missing values for each week by determining and applying the relative grouped and individual weights of the missing values and operational values. 


3. Finally, bounded, multiplicative gaussian noise was applied to the data to disrupt any implicit carryover of structure from the imputation method into the data and further anonymize the data. 

I'll be adding methodology and documentation of this as its own repo soon! 


# Data Science Salary Estimator: Project Overview

- Built model to estimate the salary of Data Scientist based on Glassdoor data.
- Scraped 2000 job descriptions from glassdoor using python and selenium.
- Engineered features from the text of each job description to quantify the value companies put on Python, R, Excel, Spark, AWS, Hadoop, Apache, SAS.
- Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.

## Web Scraping

Tweaked the web scraper github repo (above) to scrape 2000 job postings from glassdoor.com. With each job, we got the following:

- Job title
- Salary Estimate
- Job Description
- Rating
- Company
- Location
- Company Headquarters
- Company Size
- Company Founded Date
- Type of Ownership
- Industry
- Sector
- Revenue
- Competitors

## Data Cleaning

After scraping the data, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:

- Parsed numeric data out of salary
- Parsed rating out of company text
- Made a new column for company state
- Added a column for if the job was at the company’s headquarters
- Transformed founded date into age of company
- Made columns for different skills listed in the job description:
- Column for simplified job title and seniority
- Column for description length

## EDA

- Comparing the demand for certain skills,
- Understanding the demand for a data scientist based on size, state, industry, type of the company, etc
- Analyzing the Min, Max, and Average salary distributions,
- Understanding correlation between features,
- Plotting Word Cloud for Job Description

![](https://github.com/tmargary/glassdoor_salary_prediction/blob/master/assets/graphs/'python'%2C%20'r'.png)
![](https://github.com/tmargary/glassdoor_salary_prediction/blob/master/assets/graphs/Min%2C%20Max%2C%20and%20Avg%20salaries.png)
![](https://github.com/tmargary/glassdoor_salary_prediction/blob/master/assets/graphs/state.png)
![](https://github.com/tmargary/glassdoor_salary_prediction/blob/master/assets/graphs/corr.png)
![](https://github.com/tmargary/glassdoor_salary_prediction/blob/master/assets/graphs/words.png)
![](https://github.com/tmargary/glassdoor_salary_prediction/blob/master/assets/graphs/type.png)


## Model Building

Under construction

## Model performance

Under construction

## resources
- **Python Version:** 3.8<br/>
- **Video guide:** https://www.youtube.com/watch?v=MpF9HENQjDo&list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t
- **Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium<br/>
- **Scraper Github:** https://github.com/arapfaik/scraping-glassdoor-selenium<br/>
- **Scraper Article:** https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905<br/>

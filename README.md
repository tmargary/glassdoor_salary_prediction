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
- Made columns for employer provided salary and hourly wages
- Removed rows without salary
- Parsed rating out of company text
- Made a new column for company state
- Added a column for if the job was at the company’s headquarters
- Transformed founded date into age of company
- Made columns for if different skills were listed in the job description:
- Column for simplified job title and Seniority
- Column for description length

## EDA

Under construction

## Model Building

Under construction

## Model performance

Under construction

## resources
- **Video guide:** https://www.youtube.com/watch?v=MpF9HENQjDo&list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t
- **Python Version:** 3.7<br/>
- **Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium<br/>
- **Scraper Github:** https://github.com/arapfaik/scraping-glassdoor-selenium<br/>
- **Scraper Article:** https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905<br/>

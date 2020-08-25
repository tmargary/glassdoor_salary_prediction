# Data Science Salary Estimator: Project Overview

- Built model to estimate the salary of Data Scientist based on Glassdoor data.
- Scraped 2000 job descriptions from glassdoor using python and selenium.
- Engineered features from the text of each job description to quantify the value companies put on Python, R, Excel, Spark, AWS, Hadoop, Apache, SAS.
- Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.

## Web Scraping

Tweaked the web scraper GitHub repo (link below) to scrape 2000 job postings from glassdoor.com. With each job, we got the following:

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

- Comparing the demand for specific skills,
- Understanding the demand for a data scientist based on size, state, industry, type of the company, etc
- Analyzing the Min, Max, and Average salary distributions,
- Understanding the correlation between features,
- Plotting Word Cloud for Job Description

![](https://github.com/tmargary/glassdoor_salary_prediction/blob/master/assets/graphs/'python'%2C%20'r'.png)
![](https://github.com/tmargary/glassdoor_salary_prediction/blob/master/assets/graphs/state.png)
![](https://github.com/tmargary/glassdoor_salary_prediction/blob/master/assets/graphs/Min%2C%20Max%2C%20and%20Avg%20salaries.png)
![](https://github.com/tmargary/glassdoor_salary_prediction/blob/master/assets/graphs/corr_new.png)
![](https://github.com/tmargary/glassdoor_salary_prediction/blob/master/assets/graphs/words.png)
![](https://github.com/tmargary/glassdoor_salary_prediction/blob/master/assets/graphs/type_new.png)


## Model Building

Based on the EDA, the following features are selected:
`'avg_salary', 'Rating', 'Size', 'Type of ownership', 'Industry', 'Sector', 'Revenue', 'job_state',
'same_state', 'age', 'python', 'r', 'spark', 'aws', 'hadoop', 'apache', 'sas', 'excel', 'job_simp', 
'seniority', 'desc_leng', 'num_comp'`

After choosing the features, I tried three models (Linear Regression, Lasso Regression, Random forest) and used Mean Absolute Error to evaluate the performance of the model.

## Model Performance

After feeding these features to our model, these are the results of the following algorithms:
- Random Forest (after GridsearchCV): MAE = 6.96
- Random Forest (before GridsearchCV): MAE = 7.25
- Linear Regression: MAE = 12.04
- Lasso Regression: MAE = 13.43

**In this case, Random Forest performed really well, and MAE of 6.96 means the model predicts the annual salary on the test set with a mean average error of $ 6,969, which is not a bad result at all.**

## Resources
- **Python Version:** 3.8<br/>
- **Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium<br/>
- **Scraper Github:** https://github.com/arapfaik/scraping-glassdoor-selenium<br/>
- **Scraper Article:** https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905<br/>
- **Video tutorials:** https://www.youtube.com/watch?v=MpF9HENQjDo&list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t

## Future Plans
- Do research to underdstand why Lasso Regression did worse than Linear Regression and kept deteriorating as alpha increased.<br/>
![](https://github.com/tmargary/glassdoor_salary_prediction/blob/master/assets/graphs/Lasso.png)
- Try to increase the quality of feature selection.
- Come up with new feature engineering ideas which will increase the prediction accuracy.
- Deploy the model

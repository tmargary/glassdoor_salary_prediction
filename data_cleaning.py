# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 22:29:20 2020

@author: tigra
"""


import pandas as pd
df = pd.read_csv('glassdoor_jobs.csv')

# parsing min, max and avg salaries
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x: x.replace('K', '').replace('$', ''))
df['min_salary'] = minus_kd.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = minus_kd.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary) / 2

# Deleting rating from the name of those companies which have rating other than -1
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] == -1 else x['Company Name'][:-4], axis = 1)

# parsing job state from location
df['job_state'] = df['Location'].apply(lambda x: x.split(', ')[1] if ',' in x else 'na')
df.job_state.value_counts()

# same_state 0 or 1 (location vs headquarters)
df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

# calculating age of the company
df['age'] = df.Founded.apply(lambda x: x if x == -1 else 2020 - x)

# parsing skills from job despcription
df['python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.python.value_counts()
df['r'] = df['Job Description'].apply(lambda x: 1 if ' r ' in x.lower() else 0)
df.r.value_counts()
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()
df['aws'] = df['Job Description'].apply(lambda x: 1 if ' aws ' in x.lower() else 0)
df.aws.value_counts()
df['hadoop'] = df['Job Description'].apply(lambda x: 1 if 'hadoop' in x.lower() else 0)
df.hadoop.value_counts()
df['apache'] = df['Job Description'].apply(lambda x: 1 if 'apache' in x.lower() else 0)
df.apache.value_counts()
df['sas'] = df['Job Description'].apply(lambda x: 1 if 'sas' in x.lower() else 0)
df.sas.value_counts()
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel.value_counts()

# saving the ds as csv
df.to_csv('glassdoor_jobs_cleaned.csv', index = False)
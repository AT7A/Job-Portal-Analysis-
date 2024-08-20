#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


df = pd.read_csv("job_descriptions.csv")


# In[4]:


df.head(3)


# In[5]:


df.describe()


# In[6]:


df.shape


# In[7]:


df.dtypes


# In[8]:


type(df)


# In[9]:


df.columns


# In[10]:


df.rename(columns= {'Job Id':'Job_Id','Salary Range':'Salary_Range','Company Profile':'Company_Profile','Work Type':'Work_Type','Company Size':'Company_Size','Job Posting Date':'Job_Posting_Date','Contact Person':'Contact_Person','Job Title':'Job_Title','Job Portal':'Job_Portal','Job Description':'Job_Description'}, inplace= True)


# In[11]:


df.head(2)


# In[12]:


df.dropna(inplace= True)


# In[13]:


df.isnull().sum()


# In[14]:


df.drop_duplicates(inplace= True)


# In[15]:


df.shape


# In[16]:


df.to_csv('Job-Description1.csv')


# In[17]:


df.shape


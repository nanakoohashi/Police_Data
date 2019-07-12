#!/usr/bin/env python
# coding: utf-8


# ##Gather
# The police chief asks you to analyze the logs from emergency 911 calls in the city and then provide a summary of that data.


# In[1]:

import pandas as pd
import numpy as np


# In[2]:


# read .xlsx file
df = pd.read_excel("Raw Data.xlsx")
df


# Before looking cleaning the data, I want to understand what each of the column headers mean. I was unable to find the original dataset on the [City of Seattle website](https://data.seattle.gov/Public-Safety/Seattle-Police-Department-911-Incident-Response/3k2p-39jp). At this stage, I would have spoken to the department and asked for clarification for all the column headers to make sure I understand what each of the columns mean. However, I did find [this report](https://visualizationdesign.files.wordpress.com/2015/06/caocolhtsingh_fr2.pdf) and used the data variables to figure out the meaning of each column header in the dataset.

# - **CAD CDW ID**: ID in Computer Aided Dispatch System
# - **CAD Event Number**: Event Number in Computer Aided Dispatch System
# - **General Offense Number**: Number of general offense
# - **Event Clearance Code**: Clearance code of incident
# - **Event Clearance Description**: Description of incident when cleared
# - **Event Clearance SubGroup**: SubGroup of incident when cleared
# - **Event Clearance Group**: Group of incident when cleared
# - **Event Clearance Date**: Date of clearance
# - **Hundred Block Location**: Location of the incident shown in hundred block
# - **District/Sector**: Geographic area where incident occurred
# - **Zone/Beat**: Geographic area where incident occurred
# - **Census Tract**: Census geographic region where incident occurred
# - **Longitude**: Longitude where incident occurred
# - **Latitude**: Latitude where incident occurred
# - **Incident Location**: (Latitude, Longitude)
# - **Initial Type Description**: Description of incident when occurred
# - **Initial Type Subgroup**: SubGroup of incident when occurred
# - **Initial Type Group**: Group of incident when occurred
# - **At Scene Time**: Date/time when police at scene of incident


# ##Assess


# In[3]:


df.info()


# In[4]:

#find null entries
df.isnull().sum()


# In[5]:

# Check for duplicates
sum(df.duplicated())


# ##Clean


# In[6]:


# Rename columns to help code more easily
df.columns = df.columns.str.replace(' ', '_')
df


# In[7]:


# Replace `/` to `_` in column headings
df.columns = df.columns.str.replace('/', '_')
df


# In[8]:


# Observe NaNs in District Sector column
nan_rows = df[df['District_Sector'].isnull()]
nan_rows


# In[9]:


# Check if any other rows contain the same Zone_Beat as the NaN row.
df.query('Zone_Beat == "FS"')


# In[10]:


# Due to only one row containing the Zone/Beat FS, I will delete this row.
df = df.dropna(subset=['District_Sector'])


# In[11]:


# Check to make sure the row has been deleted.
df[df['District_Sector'].isnull()]


# In[12]:


# Observe NaNs in District Sector column
nan_rows1 = df[df['Census_Tract'].isnull()]
nan_rows1


# In[13]:


# sum all duplicated entries in CAD CDW ID column
sum(df.CAD_CDW_ID.duplicated())


# In[14]:


# sum all duplicated entries in CAD Event Number column
sum(df.CAD_Event_Number.duplicated())


# In[15]:


# sum all duplicated entries in General Offense Number column
sum(df.General_Offense_Number.duplicated())

#!/usr/bin/env python
# coding: utf-8


# #Part 1
# The police chief asks you to analyze the logs from emergency 911 calls in the city and then provide a summary of that data.


# In[1]:

import pandas as pd
import numpy as np


# In[2]:


# read .xlsx file
df = pd.read_excel("Raw Data.xlsx")
df


# In[3]:

df.info()

#!/usr/bin/env python
# coding: utf-8


# In[1]:

import pandas as pd
import numpy as np


# In[2]:


# read .xlsx file
df = pd.read_excel("Raw Data.xlsx")
df


# In[3]:

df.info()

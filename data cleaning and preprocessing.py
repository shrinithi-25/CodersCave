#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[49]:


df=pd.read_csv('amazon.csv')
df.head()


# In[6]:


#columns information
df.columns


# In[7]:


#rows and columns
df.shape


# In[8]:


#datatypes of each column
df.dtypes


# In[9]:


#changing datatypes
df['discounted_price'] = df['discounted_price'].str.replace('₹','')
df['discounted_price'] = df['discounted_price'].str.replace(',','')
df['discounted_price'] = df['discounted_price'].astype('float64')
df['discounted_price']


# In[10]:


df['actual_price'] = df['actual_price'].str.replace('₹','')
df['actual_price'] = df['actual_price'].str.replace(',','')
df['actual_price'] = df['actual_price'].astype('float64')
df['actual_price']


# In[11]:


df['discount_percentage'] = df['discount_percentage'].str.replace('%','').astype('float64')
df['discount_percentage'] = df['discount_percentage'] / 100
df['discount_percentage']


# In[12]:


#inspecting rating column
df['rating'].value_counts()


# In[13]:


df.query('rating == "|"')


# In[14]:


df['rating'] = df['rating'] .str.replace('|', '3.0')
df['rating'] = df['rating'] .astype('float64')
df['rating']


# In[15]:


df.isna().sum()


# In[16]:


data = df[['product_id', 'product_name', 'category', 'discounted_price', 'actual_price', 'discount_percentage', 'rating', 'rating_count']].copy()


# In[17]:


categories = df['category'].str.split('|', expand=True)
categories


# In[18]:


categories = categories.rename(columns={0:'category_1', 1:'category_2', 2:'category_3'})
categories


# In[20]:


data['category_1'] = categories['category_1']
data['category_2'] = categories['category_2']

data.drop(columns='category', inplace=True)

data


# In[21]:


data['category_1'].value_counts()


# In[22]:


data['category_1'] = data['category_1'].str.replace('&', ' & ')
data['category_1'] = data['category_1'].str.replace('OfficeProducts', 'Office Products')
data['category_1'] = data['category_1'].str.replace('MusicalInstruments', 'Musical Instruments')
data['category_1'] = data['category_1'].str.replace('HomeImprovement', 'Home Improvement')


# In[23]:


data['category_2'].value_counts()


# In[26]:


data['product_id'].str.strip()


# In[28]:


rating_score = []
for score in data['rating']:
    if score < 2.0 : rating_score.append('Poor')
    elif score < 3.0 : rating_score.append('Below Average')
    elif score < 4.0 : rating_score.append('Average')
    elif score < 5.0 : rating_score.append('Above Average')
    elif score == 5.0 : rating_score.append('Excellent')


# In[29]:


data['rating_score'] = rating_score
data['rating_score'] = data['rating_score'].astype('category')


# In[30]:


data['rating_score'] = data['rating_score'].cat.reorder_categories(['Below Average', 'Average', 'Above Average', 'Excellent'], ordered=True)


# In[31]:


data['difference_price'] = data['actual_price'] - data['discounted_price']


# In[33]:


data.head()


# In[34]:


reviewers = df[['user_id','user_name']]
reviewers


# In[35]:


review = reviewers['user_id'].str.split(',', expand=False)
review


# In[37]:


review1 = review.explode()
review2 = review1.reset_index(drop=True)
review2


# In[41]:


reviewn = reviewers['user_name'].str.split(',', expand=False)
reviewn


# In[42]:


reviewn1 = reviewn.explode()
reviewn2 = reviewn1.reset_index(drop=True)
reviewn2


# In[46]:


data21 = pd.DataFrame(data=review2)
data22 = pd.DataFrame(data=reviewn2)
data2 = pd.merge(data21, data22, left_index=True, right_index=True)


# In[47]:


data2 = pd.merge(data21, data22, left_index=True, right_index=True)


# In[48]:


data2.head()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # Pandas Tutorial
# ## Python Pandas Tutorial (Part 1): Getting Started with Data Analysis - Installation and Loading Data
# * link https://www.youtube.com/watch?v=ZyhVh-qRZPA&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS
# * code https://www.youtube.com/watch?v=ZyhVh-qRZPA&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS
# * Virtual Environment Tutorial - https://youtu.be/Kg1Yvry_Ydk
# * Jupyter Tutorial - https://youtu.be/HW29067qVWk
# * StackOverflow Survey Download Page - http://bit.ly/SO-Survey-Download
# 

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('survey_results_public.csv')


# In[3]:


df.tail(10)


# In[4]:


df.shape


# In[5]:


pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)


# In[7]:


schema_df = pd.read_csv('survey_results_schema.csv')


# In[8]:


schema_df


# In[9]:


pd


# In[29]:


df = pd.read_csv('survey_results_public.csv', index_col='Respondent')
schema_df = pd.read_csv('survey_results_schema.csv', index_col='Column')


# In[30]:


pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)


# In[31]:


df.head()


# In[32]:


schema_df


# In[33]:


schema_df.loc['MgrIdiot', 'QuestionText']


# In[34]:


schema_df.sort_index(inplace=True)


# In[35]:


schema_df


# In[40]:


filt = df['LanguageWorkedWith'].str.contains('Python', na=False)
filt


# In[41]:


df.loc[filt]


# In[80]:


df.rename(columns={'ConvertedComp': 'SalaryUSD'}, inplace=True)


# In[81]:


df['SalaryUSD']


# In[82]:


df['Hobbyist']


# In[83]:


df['Hobbyist'].map({'Yes': True, 'No': False})


# In[84]:


df['Hobbyist'] = df['Hobbyist'].map({'Yes': True, 'No': False})
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Python Pandas Tutorial (Part 2): DataFrame and Series Basics - Selecting Rows and Columns
# * link https://www.youtube.com/watch?v=zmdjNSmRXF4&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=2
# * code https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Pandas/02-DataFrames

# In[10]:


df['Hobbyist']


# In[11]:


df.loc[0:2, 'Hobbyist':'Employment']


# In[12]:


person = {
    "first": "Corey", 
    "last": "Schafer", 
    "email": "CoreyMSchafer@gmail.com"
}


# In[13]:


people = {
    "first": ["Corey"], 
    "last": ["Schafer"], 
    "email": ["CoreyMSchafer@gmail.com"]
}


# In[14]:


people = {
    "first": ["Corey", 'Jane', 'John'], 
    "last": ["Schafer", 'Doe', 'Doe'], 
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}


# In[15]:


people['email']


# In[16]:


df_exa = pd.DataFrame(people)


# In[17]:


df_exa


# In[18]:


df_exa['email']


# In[19]:


df_exa.email


# In[20]:


# 根据index找对应未知的值
df_exa.iloc[[0, 1], 2]


# In[21]:


# 根据行index和列名称找对应未知的值
df_exa.loc[[0, 1], ['email', 'last']]


# ## Python Pandas Tutorial (Part 3): Indexes - How to Set, Reset, and Use Indexes
# * link https://www.youtube.com/watch?v=W9XjRYFkkyw&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=3
# * code http://bit.ly/Pandas-03

# In[23]:


df_exa.set_index('email', inplace=True)


# In[24]:


df_exa


# In[25]:


df_exa.index


# In[26]:


df_exa.loc['CoreyMSchafer@gmail.com', 'last']


# In[27]:


df_exa.iloc[0]


# In[28]:


df_exa.reset_index(inplace=True)
df_exa


# ## Python Pandas Tutorial (Part 4): Filtering - Using Conditionals to Filter Rows and Columns
# * link https://www.youtube.com/watch?v=Lw2rlcxScZY&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=4
# * code http://bit.ly/Pandas-04

# In[36]:


filt = (df_exa['last'] == 'Schafer') | (df_exa['first'] == 'John')


# In[37]:


df_exa.loc[~filt, 'email'] # 不选择满足条件的


# ## Python Pandas Tutorial (Part 5): Updating Rows and Columns - Modifying Data Within DataFrames
# * link https://www.youtube.com/watch?v=DCDe29sIKcE&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=5
# * code http://bit.ly/Pandas-05

# In[48]:


people = {
    "first": ["Corey", 'Jane', 'John'], 
    "last": ["Schafer", 'Doe', 'Doe'], 
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}


# In[49]:


df_exa = pd.DataFrame(people)


# In[50]:


df_exa.columns = ['first_name', 'last_name', 'email']


# In[51]:


df_exa


# In[52]:


df_exa.columns = [x.lower() for x in df_exa.columns]
df_exa


# In[53]:


df_exa.rename(columns={'first_name': 'first', 'last_name': 'last'}, inplace=True)


# In[54]:


df_exa.loc[2] = ['John', 'Smith', 'JohnSmith@email.com']
df_exa


# In[57]:


df_exa.loc[2, ['last', 'email']] = ['Doe', 'JohnDoe@email.com']
df_exa


# In[58]:


df_exa.loc[2, 'last'] = 'Smith'
df_exa


# In[59]:


df_exa.at[2, 'last'] = 'Doe'
df_exa


# In[60]:


filt = (df_exa['email'] == 'JohnDoe@email.com')
df_exa[filt]['last'] = 'Smith'


# In[62]:


df_exa['email'] = df_exa['email'].str.lower()
df_exa


# In[63]:


df_exa['email'].apply(len)


# In[64]:


def update_email(email):
    return email.upper()


# In[66]:


df_exa['email'].apply(update_email)


# In[68]:


df_exa['email'] = df_exa['email'].apply(lambda x: x.lower())
df_exa


# In[69]:


df_exa['email'].apply(len)


# In[70]:


df_exa.apply(len, axis='columns') ##???


# In[71]:


len(df_exa['email'])


# In[72]:


df_exa.apply(pd.Series.min)


# In[73]:


df_exa.apply(lambda x: x.min())


# In[74]:


df_exa.applymap(len)


# In[75]:


df_exa.applymap(str.lower)


# In[76]:


df_exa['first'].map({'Corey': 'Chris', 'Jane': 'Mary'})


# In[78]:


df_exa['first'] = df_exa['first'].replace({'Corey': 'Chris', 'Jane': 'Mary'})


# In[79]:


df_exa


# In[85]:


help(df.applymap)


# In[88]:


help(df_exa['first'].map)


# In[89]:


df_exa['first'].map({'Corey': 'Chris', 'Jane': 'Mary'},na_action='ignore)


# ## Python Pandas Tutorial (Part 6): Add/Remove Rows and Columns From DataFrames
# * link https://www.youtube.com/watch?v=HQ6XO9eT-fc&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=6
# * code http://bit.ly/Pandas-06

# In[ ]:





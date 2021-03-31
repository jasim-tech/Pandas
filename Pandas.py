#!/usr/bin/env python
# coding: utf-8

# 
# Data loading in to pandas

# In[141]:


import pandas as pd
#load as txt file
df=pd.read_csv('pokemon_data.csv')
#load as csv file
#df=pd.read_csv('pokemon_data.txt',delimiter='\t')
print(df)


# 
# Reading Data in pandas
# 

# In[142]:


import pandas as pd
#print columns name
print(df.columns)

#print specific column
print(df['Name'][0:5])


# In[143]:


#get some specific columns
print(df[['Name','Type 1','Type 2']])


# In[144]:


#Get some Row from up to down
print(df.head(5))
#get some row from down to up
print(df.tail(5))


# In[145]:


#Read specific Row
print(df.iloc[3])
#Read data from row 2 to row 5
print(df.iloc[2:5])


# In[146]:


#Read specific element from data table
print(df.iloc[799,1])


# In[147]:


#Get all row with respect to index
for index , row in df.iterrows():
    #print(index,row)
    print(index,row[["Name",'HP']])


# In[148]:


#Read same type of element of any row
print(df.loc[df['Type 1']=='Fire'])


# Data sorting and describing

# In[149]:


df.describe()


# In[150]:


print(df)
#sorting data with accesending order
print(df.sort_values(['Name']))


# In[151]:


#sorting with descending
print(df.sort_values('Name',ascending=False))


# In[152]:


#Two columns sorting at a time in same order
#print(df.sort_values(['Type 1','HP']))


# In[153]:


#Two columns sorting at a time in different order
#print(df.sort_values(['Type 1','HP'],ascending=[1,0]))


# Making change in Data

# In[154]:


df.head(5)


# In[155]:


#Adding a column
df['Total']=df['HP']+df['Attack']+df['Defense']+df['Sp. Atk']+df['Sp. Def']+df['Speed']
print(df)


# In[156]:


#df.head(5)


# In[161]:


#df=df.drop(columns=['Total'])
#print(df)


# In[158]:


#another way to add an new total colummn
#df['Total']=df.iloc[:,4:10].sum(axis=1)
#print(df)


# In[159]:


#columns reordering
#df=df[['Total','HP','Defense']]
#print(df)


# In[160]:


#Set a coulmn in a specific position
#print(df)
cols=list(df.columns)
df=df[cols[0:4]+[cols[-1]]+cols[4:12]]
print(df)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[4]:


#import libraries
#!pip install kaggle
import kaggle


# In[ ]:


#download a dataset using kaggle api
get_ipython().system('kaggle datasets download ankitbansal06/retail-orders -f orders.csv')


# In[6]:


#extract file from zip file
import zipfile
zip_ref=zipfile.ZipFile('orders.csv.zip')
zip_ref.extractall() #extract file to dir
zip_ref.close() #close file


# In[10]:


#read data from the file and handle null values
import pandas as pd
df=pd.read_csv('orders.csv',na_values=['Not Available','unknown'])
#df.head(20)
df['Ship Mode'].unique()


# In[33]:


#rename column names ,make them lowercase and replace space with underscore
#df
#df.rename(columns={'Order Id':'order_id','City':'city'}) #this is not a good practice to rename each and every column
#df.columns=df.columns.str.lower()
#df.columns=df.columns.str.replace(' ','_')
#df.head(5)


# In[25]:


#derive new columns discount,sale price and profit
#df['discount']=df['list_price']*df['discount_percent']*0.01
#df['sale_price']=df['list_price']-df['discount']
df['profit']=df['sale_price']-df['cost_price']
df.head(5)


# In[29]:


#convert order date from object datatype to datetime
df['order_date']=pd.to_datetime(df['order_date'],format='%Y-%m-%d')


# In[32]:


#drop cost price , list price,discount columns
df.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)


# In[35]:


#load the data into sql server using replace option
import sqlalchemy as sal
engine=sal.create_engine('mssql://RahityaGovindu/master?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')
conn=engine.connect()


# In[37]:


#load data into sql using append option
df.to_sql('df_orders',con=conn,index=False,if_exists='append')


# In[ ]:





# In[ ]:





# In[ ]:





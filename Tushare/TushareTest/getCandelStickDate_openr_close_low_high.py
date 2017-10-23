
# coding: utf-8

# In[2]:

from sqlalchemy import create_engine
import tushare as ts
import pymysql
import datetime


# In[33]:

weekdata = ts.get_hist_data('000050', '2017-10-09', '2017-10-21', '30', 3)


# In[34]:

weekdata = weekdata.sort_index(axis=0)


# In[35]:

weekdata = weekdata.loc[:,['open','close','low','high']]
weekdata


# In[36]:

json = '['
for row in weekdata.iterrows() :
    rowStr = row[1]
    rowStr = str(rowStr.tolist())
    rowStr = rowStr[:1] + rowStr[1:]
    json += rowStr+','
json = json[0:-1]
json += ']'
print(json)


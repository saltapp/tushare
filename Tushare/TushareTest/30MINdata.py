
# coding: utf-8

# In[22]:

from sqlalchemy import create_engine
import tushare as ts
import pymysql
import datetime
pymysql.install_as_MySQLdb()


# print(time.time())

beforeweek = datetime.datetime.now() - datetime.timedelta(days = 7)
 
start = datetime.datetime.strftime(beforeweek,"%Y-%m-%d")
# 
end = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d")
 
weekdata = ts.get_hist_data('000050', start, end, '30', 3)
 
# # print(weekdata['volume'])
# 
# for x in range(1,len(weekdata['volume'])):
#     print(weekdata['volume'][x] - weekdata['volume'][x-1])
#     print('-----')
#  
# classifieds = ts.get_concept_classified();
weekdata = weekdata.sort_index(axis=0)

weekdata = weekdata.iloc[:,0:5]
wkclose = weekdata['close']
wklow = weekdata['low']
weekdata.drop(labels=['close'], axis=1,inplace = True)
weekdata.insert(1,'close',wkclose)

weekdata.drop(labels=['low'], axis=1,inplace = True)
weekdata.insert(2,'low',wklow)
print(weekdata)


# In[23]:

rowIndex = weekdata.index
print(rowIndex)
row = weekdata.iloc[0].tolist()
print(str(row))


# In[24]:

import pandas as pd
json = '['
for row in weekdata.iterrows() :
    rowStr = row[1]
    rowStr = str(rowStr.tolist())
    rowStr = rowStr[:1] + '"' + row[0] + '", ' + rowStr[1:]
    json += rowStr+','
json += ']'

print(json)


# In[50]:




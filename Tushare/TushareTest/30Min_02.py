
# coding: utf-8

# In[99]:




# In[22]:

from sqlalchemy import create_engine
import tushare as ts
import pymysql
import datetime
pymysql.install_as_MySQLdb()


# print(time.time())

beforeweek = datetime.datetime.now() - datetime.timedelta(days = 1)
 
start = datetime.datetime.strftime(beforeweek,"%Y-%m-%d")
# 
end = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d")
 
weekdata = ts.get_hist_data('000050', start, end, '30', 3)

df = ts.get_tick_data('000050',date=start);
print(weekdata)
print(df)


# In[94]:

volData1000 = df[df.time < '10:00:00'].loc[:,['price','volume']].groupby('price').sum()
volData1030 = df[df.time < '10:30:00'][df.time > '10:00:00'].loc[:,['price','volume']].groupby('price').sum()
volData1100 = df[df.time < '11:00:00'][df.time > '10:30:00'].loc[:,['price','volume']].groupby('price').sum()
volData1130 = df[df.time < '11:30:00'][df.time > '11:00:00'].loc[:,['price','volume']].groupby('price').sum()
volData0130 = df[df.time < '13:30:00'][df.time > '13:00:00'].loc[:,['price','volume']].groupby('price').sum()
volData0200 = df[df.time < '14:00:00'][df.time > '13:30:00'].loc[:,['price','volume']].groupby('price').sum()
volData0230 = df[df.time < '14:30:00'][df.time > '14:00:00'].loc[:,['price','volume']].groupby('price').sum()
volData0300 = df[df.time < '15:00:00'][df.time > '14:30:00'].loc[:,['price','volume']].groupby('price').sum()
volDatas = [volData1000,volData1030,volData1100,volData1130,volData0130,volData0200,volData0230,volData0300]


# In[85]:

def getJsonV(volData):  
    jsonV = ''
    for row in volData1000.iterrows() :
        jsonV += str(row[0]) + ', ' + str(row[1].tolist()[0])+','
    jsonV = jsonV[0:-1]
    return jsonV

getJsonV(volDatas[0])


# In[87]:

# classifieds = ts.get_concept_classified();
weekdata = weekdata.sort_index(axis=0)
print(weekdata)
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


# In[80]:

import pandas as pd
json = '['
i = 0
for row in weekdata.iterrows():
    rowStr = row[1]
    rowStr = str(rowStr.tolist())
    rowStr = '[' + '"' + row[0] + '", ' + rowStr[1:-1] + ', ' + getJsonV(volDatas[i])
    json += rowStr+'],'
    i = i + 1
json += ']'
print(json)


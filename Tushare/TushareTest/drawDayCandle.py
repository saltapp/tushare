
# coding: utf-8

# In[42]:

from sqlalchemy import create_engine
import tushare as ts
import pymysql
import datetime

weekdata = ts.get_hist_data('000050', '2017-08-23', '2017-10-23', 'D', 3)

weekdata = weekdata.sort_index(axis=0)

weekdata = weekdata.loc[:,['open','close','low','high']]
weekdata

json = '['
for row in weekdata.iterrows() :
    rowStr = row[1]
    rowStr = str(rowStr.tolist())
    rowStr = rowStr[:1] + rowStr[1:]
    json += rowStr+','
json = json[0:-1]
json += ']'
print(json)


# In[11]:

print(list(weekdata.index))


# In[43]:

beforedate = datetime.datetime.now() - datetime.timedelta(days = (61))
beforedate = datetime.datetime.strftime(beforedate,"%Y-%m-%d")
print(beforedate)


# In[48]:

beforeweek = []
volDatas = []
timePoints = [' 10:00:00',' 10:30:00',' 11:00:00',' 11:30:00',' 01:30:00',' 02:00:00',' 02:30:00',' 03:00:00']
markIndex = 0
for i in range(0,60):
    beforedate = datetime.datetime.now() - datetime.timedelta(days = (61-i))
    beforedate = datetime.datetime.strftime(beforedate,"%Y-%m-%d")
    print(beforedate)
    df = ts.get_tick_data('600048',date=str(beforedate),pause=2,retry_count=5)
    if (df.head(1)['time']).item() == 'alert("当天没有数据");':
        continue
    df = df.loc[:,['price','volume']].groupby('price').sum()
    df.loc[:,'time'] = (str(beforedate))
    volDatas.append(df)
    print('-------------------------------------------------------')


# In[49]:

jsonV = '['
for vd in volDatas:
    for row in vd.index:
        jsonV = jsonV + '[\'' + vd.loc[row]['time'] + '\', ' + str(row) + ', ' + str(vd.loc[row]['volume']) + '], '
jsonV = jsonV + ']'
print(jsonV)


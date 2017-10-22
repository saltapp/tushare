
# coding: utf-8

# In[2]:

from IPython.display import HTML


# In[146]:

from sqlalchemy import create_engine
import tushare as ts
import pymysql
import datetime
pymysql.install_as_MySQLdb()


# print(time.time())
beforeweek = []
volDatas = []
timePoints = [' 10:00:00',' 10:30:00',' 11:00:00',' 11:30:00',' 01:30:00',' 02:00:00',' 02:30:00',' 03:00:00']
markIndex = 0
for i in range(1,15):
    beforedate = datetime.datetime.now() - datetime.timedelta(days = (15-i))
    beforedate = datetime.datetime.strftime(beforedate,"%Y-%m-%d")
    print(beforedate)
    df = ts.get_tick_data('000050',date=str(beforedate))
    print(type(df.head(1)['time']))
    if (df.head(1)['time']).item() == 'alert("当天没有数据");':
        continue
    #print('------------------------------------------------')
    #print(df)
    #print('------------------------------------------------')
    volData1000 = df[df.time < '10:00:00'].loc[:,['price','volume']].groupby('price').sum()
    volData1030 = df[df.time < '10:30:00'][df.time > '10:00:00'].loc[:,['price','volume']].groupby('price').sum()
    volData1100 = df[df.time < '11:00:00'][df.time > '10:30:00'].loc[:,['price','volume']].groupby('price').sum()
    volData1130 = df[df.time < '11:30:00'][df.time > '11:00:00'].loc[:,['price','volume']].groupby('price').sum()
    volData0130 = df[df.time < '13:30:00'][df.time > '13:00:00'].loc[:,['price','volume']].groupby('price').sum()
    volData0200 = df[df.time < '14:00:00'][df.time > '13:30:00'].loc[:,['price','volume']].groupby('price').sum()
    volData0230 = df[df.time < '14:30:00'][df.time > '14:00:00'].loc[:,['price','volume']].groupby('price').sum()
    volData0300 = df[df.time < '15:00:00'][df.time > '14:30:00'].loc[:,['price','volume']].groupby('price').sum()
    
    volData1000.loc[:,'time'] = (str(beforedate) + ' 10:00:00')
    volData1030.loc[:,'time'] = (str(beforedate) + ' 10:30:00')
    volData1100.loc[:,'time'] = (str(beforedate) + ' 11:00:00')
    volData1130.loc[:,'time'] = (str(beforedate) + ' 11:30:00')
    volData0130.loc[:,'time'] = (str(beforedate) + ' 01:30:00')
    volData0200.loc[:,'time'] = (str(beforedate) + ' 02:00:00')
    volData0230.loc[:,'time'] = (str(beforedate) + ' 02:30:00')
    volData0300.loc[:,'time'] = (str(beforedate) + ' 03:00:00')
    
    
    volDatas.append(volData1000)
    volDatas.append(volData1030)
    volDatas.append(volData1100)
    volDatas.append(volData1130)
    volDatas.append(volData0130)
    volDatas.append(volData0200)
    volDatas.append(volData0230)
    volDatas.append(volData0300)
#print(volDatas)
    #for i in range(0,7):
    #    volDatas[i + markIndex].loc[:,'time'] = (str(beforedate) + timePoints[i])
    #markIndex = 8 * (i - 1)
#start = datetime.datetime.strftime(beforeweek,"%Y-%m-%d")
#end = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d")
 
#weekdata = ts.get_hist_data('000050', start, end, '30', 3)


# print(volDatas)

# In[117]:

print(type(volDatas[1]))


# In[24]:


volData1000 = df[df.time < '10:00:00'].loc[:,['price','volume']].groupby('price').sum()
volData1030 = df[df.time < '10:30:00'][df.time > '10:00:00'].loc[:,['price','volume']].groupby('price').sum()
volData1100 = df[df.time < '11:00:00'][df.time > '10:30:00'].loc[:,['price','volume']].groupby('price').sum()
volData1130 = df[df.time < '11:30:00'][df.time > '11:00:00'].loc[:,['price','volume']].groupby('price').sum()
volData0130 = df[df.time < '13:30:00'][df.time > '13:00:00'].loc[:,['price','volume']].groupby('price').sum()
volData0200 = df[df.time < '14:00:00'][df.time > '13:30:00'].loc[:,['price','volume']].groupby('price').sum()
volData0230 = df[df.time < '14:30:00'][df.time > '14:00:00'].loc[:,['price','volume']].groupby('price').sum()
volData0300 = df[df.time < '15:00:00'][df.time > '14:30:00'].loc[:,['price','volume']].groupby('price').sum()
volDatas.append(volData1000)
volDatas.append(volData1030)
volDatas.append(volData1100)
volDatas.append(volData1130)
volDatas.append(volData0130)
volDatas.append(volData0200)
volDatas.append(volData0230)
volDatas.append(volData0300)
timePoints = [' 10:00:00',' 10:30:00',' 11:00:00',' 11:30:00',' 01:30:00',' 02:00:00',' 02:30:00',' 03:00:00']


# In[43]:

for i in range(0,len(volDatas)):
    volDatas[i].loc[:,'time'] = (datetime.datetime.strftime(beforeweek,"%Y-%m-%d") + timePoints[i])


# In[64]:

volData0230


# In[147]:

jsonV = '['
XaxisData = []
for vd in volDatas:
    for row in vd.index:
        jsonV = jsonV + '[\'' + vd.loc[row]['time'] + '\', ' + str(row) + ', ' + str(vd.loc[row]['volume']) + '], '
        XaxisData.append(vd.loc[row]['time'])
jsonV = jsonV + ']'
print(jsonV)
listXaxis = list(set(XaxisData))
listXaxis.sort(key=XaxisData.index)
print(listXaxis)


# In[134]:

dfTest1 = ts.get_tick_data('000050',date='2017-10-21')
print(dfTest1.head(1)['time'] == 'alert("当天没有数据");')

dfTest2 = ts.get_tick_data('000050',date='2017-10-20')
print(dfTest2.head(1)['time'] == 'alert("当天没有数据");')


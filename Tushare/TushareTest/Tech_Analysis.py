'''
Created on 2017年9月18日

@author: saltapp
'''
import tushare as ts
import pymysql
import datetime
import matplotlib.pyplot as plt
pymysql.install_as_MySQLdb()


# print(time.time())

beforeweek = datetime.datetime.now() - datetime.timedelta(days = 7)
 
start = datetime.datetime.strftime(beforeweek,"%Y-%m-%d")
# 
end = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d")
 
weekdata = ts.get_hist_data('000050', start, end, 'D', 3)

print(weekdata['close'])

weekdata['close'].plot(grid=True, figsize=(8,5))

plt.show()
# from sklearn import svm
# 
# x = [[1,1],[2,3]]
# y = [0,1]
# clf = svm.SVC(kernel='linear')
# clf.fit(x,y)
# 
# print (clf)
# 
# print (clf.support_vectors_)
# 
# print(clf.predict([2,4]))

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
 
weekdata = ts.get_hist_data('000050', start, end, '5', 3)
 
# # print(weekdata['volume'])
# 
for x in range(1,len(weekdata['volume'])):
# for x in range(1,len(weekdata['volume'])):
#     print(weekdata['volume'][x] - weekdata['volume'][x-1])
#     print('-----')
#  
# classifieds = ts.get_concept_classified();
# 
engine = create_engine('mysql://root:root@127.0.0.1/tushare?charset=utf8')
# # 
weekdata.to_sql('SC000050',engine)


 
 
 
# timestr = time.strptime(beforeweek, "%Y-%m_%d")




# df = ts.get_concept_classified()
# df = ts.get_today_all()

# print(df)
#engine = create_engine('mysql://root:root@127.0.0.1/tushare?charset=utf8')

# print(df)
# engine = create_engine("mysql://root:root@127.0.0.1/tushare?charset=utf8")
# 
# df.to_sql('000050STM',engine)
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
from statsmodels.iolib.tests.test_table_econpy import cell0data
pymysql.install_as_MySQLdb()


df = ts.get_hist_data('000050', '2017-08-20', '2017-09-10', 'D', 3, 0)
#engine = create_engine('mysql://root:root@127.0.0.1/tushare?charset=utf8')

print(df ['open'])
# engine = create_engine("mysql://root:root@127.0.0.1/tushare?charset=utf8")
# 
# df.to_sql('000050STM',engine)
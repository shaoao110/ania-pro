from mysql.connector import errorcode
import json
import mysql.connector

# 加载数据库配置
with open('config/datasource.json', 'r', encoding='utf-8') as f:
    dbconf = json.load(f)

class SqlMapper():
    def getUserInfoByUserId(self,userId) -> object:
        cnct = mysql.connector.connect(host=dbconf['host'],port=dbconf['port'],user=dbconf['user'],password=dbconf['password'],database=dbconf['database'])
        cursor = cnct.cursor(dictionary=True)
        sql = "select * from tb_user_info where userId = %(userId)s"
        param = {"userId":userId}
        cursor.execute(sql,param)
        data = cursor.fetchone()
        print(data)
        if data:
            cnct.close()
            return data
        else:
            init_sql = "insert into tb_user_info (userId,welword) values (%(userId)s,%(welword)s)"
            init_param = {
                'userId':userId,
                'welword':''
            }
            cursor.execute(init_sql,init_param)
            cnct.commit()
            cnct.close()
            return init_param

    def updateUserInfo(self,userInfo):
        cnct = mysql.connector.connect(host=dbconf['host'],port=dbconf['port'],user=dbconf['user'],password=dbconf['password'],database=dbconf['database'])
        cursor = cnct.cursor()
        sql = "update tb_user_info set welword = %(welword)s,jiecao = %(jiecao)s,jiecaoLimit = %(jiecaoLimit)s,jiecaoDate = %(jiecaoDate)s where userId = %(userId)s"
        param = {
            "userId":userInfo['userId'],
            "welword":userInfo['welword'],
            "jiecao":userInfo['jiecao'],
            "jiecaoLimit":userInfo['jiecaoLimit'],
            "jiecaoDate":userInfo['jiecaoDate']
        }
        print(param)
        cursor.execute(sql,param)
        cnct.commit()
        cnct.close()

    def getTd2UserByUserId(self,userId) -> object:
        cnct = mysql.connector.connect(host=dbconf['host'],port=dbconf['port'],user=dbconf['user'],password=dbconf['password'],database=dbconf['database'])
        cursor = cnct.cursor(dictionary=True)
        sql = "select * from tb_td2_user where userId = %(userId)s"
        param = {"userId":userId}
        cursor.execute(sql,param)
        data = cursor.fetchone()
        print(data)
        if data:
            cnct.close()
            return data
        else:
            init_sql = "insert into tb_td2_user (userId,td2name) values (%(userId)s,%(td2name)s)"
            init_param = {
                'userId':userId,
                'td2name':''
            }
            cursor.execute(init_sql,init_param)
            cnct.commit()
            cnct.close()
            return init_param

    def updateTd2nameByUserId(self,userId,name):
        cnct = mysql.connector.connect(host=dbconf['host'],port=dbconf['port'],user=dbconf['user'],password=dbconf['password'],database=dbconf['database'])
        cursor = cnct.cursor()
        sql = "update tb_td2_user set td2name = %(td2name)s where userId = %(userId)s"
        param = {
            "userId":userId,
            "td2name":name
        }
        print(param)
        cursor.execute(sql,param)
        cnct.commit()
        cnct.close()

    def getTd2nameByUserId(self,userId) -> str:
        cnct = mysql.connector.connect(host=dbconf['host'],port=dbconf['port'],user=dbconf['user'],password=dbconf['password'],database=dbconf['database'])
        cursor = cnct.cursor(dictionary=True)
        sql = "select * from tb_td2_user where userId = %(userId)s"
        param = {"userId":userId}
        cursor.execute(sql,param)
        data = cursor.fetchone()
        print(data)
        cnct.close()
        if data:
            return data['td2name']
        else:
            return ''

    def getSigninByUserId(self,userId) -> object:
        cnct = mysql.connector.connect(host=dbconf['host'],port=dbconf['port'],user=dbconf['user'],password=dbconf['password'],database=dbconf['database'])
        cursor = cnct.cursor(dictionary=True)
        sql = "select * from tb_signin where userId = %(userId)s"
        param = {"userId":userId}
        cursor.execute(sql,param)
        data = cursor.fetchone()
        print(data)
        if data:
            cnct.close()
            return data
        else:
            init_sql = "insert into tb_signin (userId,total,consecutive,record,prop) values (%(userId)s,%(total)s,%(consecutive)s,%(record)s,%(prop)s)"
            init_param = {
                'userId':userId,
                'total':0,
                'consecutive':0,
                'record':'',
                'prop':0
            }
            cursor.execute(init_sql,init_param)
            cnct.commit()
            cnct.close()
            return init_param

    def updateSigninByUserId(self,signinfo):
        cnct = mysql.connector.connect(host=dbconf['host'],port=dbconf['port'],user=dbconf['user'],password=dbconf['password'],database=dbconf['database'])
        cursor = cnct.cursor()
        sql = "update tb_signin set total = %(total)s , consecutive = %(consecutive)s , record = %(record)s , prop = %(prop)s where userId = %(userId)s"
        param = {
            "userId":signinfo['userId'],
            'total':signinfo['total'],
            'consecutive':signinfo['consecutive'],
            'record':signinfo['record'],
            'prop':signinfo['prop']
        }
        print(param)
        cursor.execute(sql,param)
        cnct.commit()
        cnct.close()
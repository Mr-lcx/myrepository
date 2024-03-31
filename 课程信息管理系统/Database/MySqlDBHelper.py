# 本文件用来执行具体的sql命令

import pymysql
import traceback


# from Util.Properties import Properties
# from DBUtils.PooledDB import PooledDB


class MySqlDBHelper:
    def __init__(self):
        self.conn = None

    def Conn(self):
        self.conn = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="lu121511",
            database="教务系统",
            charset="utf8"
        )

    # def Conn(self):
    #         self.conn = pymysql.connect(
    #             host="212.64.9.5",
    #             port=3306,
    #             database='teaching2',
    #             user='root',
    #             password='20200501Fromzyh!',
    #             charset='utf8'
    #         )

    # 通过一条sql语句 从数据库中获取一条纪录
    def get_one(self, sqlstr, param=None):
        self.Conn()
        try:
            with self.conn.cursor() as cursor:
                if param is None:
                    count = cursor.execute(sqlstr, ())
                else:
                    count = cursor.execute(sqlstr, param)
                if count > 0:
                    result = cursor.fetchone()
                else:
                    result = False
                return result
        except pymysql.DatabaseError:
            self.conn.rollback()
        finally:
            self.conn.close()

    def get_many(self, sqlstr, param):
        self.Conn()
        try:
            with self.conn.cursor() as cursor:
                mydata = []
                if param == "":
                    cursor.execute(sqlstr, ())
                else:
                    cursor.execute(sqlstr, (param))

                result_list = cursor.fetchall()
                print("**********************************")
                for item in result_list:
                    print(item)
                    mydata.append(item)
                return mydata
        except pymysql.DatabaseError:
            self.conn.rollback()
        finally:
            self.conn.close()

    def UpdataorInsert(self, sqlstr, param):
        self.Conn()
        try:
            print("11")
            with self.conn.cursor() as cursor:
                result = cursor.execute(sqlstr, param)
                print("22")
                self.conn.commit()
                print(result)
                return result
        except pymysql.DatabaseError:
            self.conn.rollback()
        finally:
            self.conn.close()

    # 删除表中一条纪录
    def DeleteOne(self, sqlstr, id):
        self.Conn()
        try:
            with self.conn.cursor() as cursor:
                result = cursor.execute(sqlstr, id)
                self.conn.commit()
                return result
        except pymysql.DatabaseError:
            self.conn.rollback()
        finally:
            self.conn.close()

            #####################

    # 管理员 新添加
    # 查询所有数据,返回列表
    '''
    获取一列数据
    '''
    def get_oneCol(self, sql, param=None):
        tmp = self.get_all(sql, param)
        if tmp is False:
            return False
        lst = []
        for i in tmp:
            lst.append(i[0])
        return lst

        # 查询所有数据

    def get_all(self, sql, param=None):
        self.Conn()
        try:
            with self.conn.cursor() as cursor:
                if param is None:
                    count = cursor.execute(sql)
                else:
                    count = cursor.execute(sql, param)
                if count > 0:
                    result = cursor.fetchall()
                else:
                    result = False
                return result
        except Exception as e:
            traceback.print_exc(e)

    def get_oneValue(self, sql, param=None):
        return self.get_oneCol(sql, param)[0]

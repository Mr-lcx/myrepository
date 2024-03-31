
# 本文件用来编写需要执行的sql语句，通过函数的形式返回结果给调用者

from Database.MySqlDBHelper import MySqlDBHelper

class DBManager(object):
    db = None

    def __init__(self):
        # 构造一个MySqlDBHelper类的实例属性
        self.db = MySqlDBHelper()

    # 登录
    def loginStudent(self, id, password):
        sql = "select * from 学生表 where 学号= %s and 密码 = %s"
        return self.db.get_one(sql, (id, password))

    def loginTeacher(self, id, password):
        sql = "select * from 教师表 where 教工号 = %s and 密码 = %s"
        return self.db.get_one(sql, (id, password))

    def loginAdmin(self, id, password):
        sql = "select count(*) from admin where id = %s and password = %s"
        return self.db.get_one(sql, (id, password))[0]

    # admin
    def adminSelectById(self, id):
        sql = "select * from admin where id = %s"
        return self.db.get_one(sql, (id))

    # 注册教师账号
    def InsertTeacher(self,id,name,sex,password1,password2,xueyuan,classes):
        sqlstr = """
                    insert into 教师表(教工号,姓名,性别,密码,找回密码,学院,联系方式)
                       values(%s,%s,%s,%s,%s,%s,%s)
                                    """
        return self.db.UpdataorInsert(sqlstr, (id,name,sex,password1,password2,xueyuan,classes))

    # 注册学生账号
    def InsertStudent(self, id, name, sex, password1, password2, xueyuan, classes):
        sqlstr = """
                    insert into 学生表(学号,姓名,性别,密码,找回密码,学院,班级)
                       values(%s,%s,%s,%s,%s,%s,%s)
                                    """
        return self.db.UpdataorInsert(sqlstr, (id, name, sex, password1, password2, xueyuan, classes))

    # 获得教师表的一条纪录
    def GetTeacherOne(self, id):
        sql = "select * from 教师表 where 教工号 = %s"
        return self.db.get_one(sql, (id))

    # 获得学生表的一条纪录
    def GetStudentOne(self, id):
        sql = "select * from 学生表 where 学号 = %s"
        return self.db.get_one(sql, (id))

    # 教师表更新基本信息
    def teacherUpdate(self,id, phone,xueyuan):
        sql = "update 教师表 set 联系方式=%s,学院= %s where 教工号=%s"
        return self.db.UpdataorInsert(sql, (phone,xueyuan,id))

    def studentUpdata(self,id, classes,xueyuan):
        sql = "update 学生表 set 班级=%s,学院= %s where 学号=%s"
        return self.db.UpdataorInsert(sql, (classes, xueyuan, id))

     #教师表更新密码
    def TeacherUpdatePassword(self,id,possword):
        sql  = "update 教师表 set 密码=%s where 教工号=%s"
        return self.db.UpdataorInsert(sql, (possword, id))
    # 学生修改密码
    def StudentUpdatePassword(self,id,possword):
        sql  = "update 学生表 set 密码=%s where 学号=%s"
        return self.db.UpdataorInsert(sql, (possword, id))

    # 获得所有开课数据
    def GetAllClassOpen(self):
        sql = "select * from 开课表"
        return self.db.get_many(sql, (""))

    # 查看所有考试安排情况
    def GetAllExam(self):
        sql = "select 课程号,课程名,任课老师,考试时间,考试地点,考试形式 from 开课表"
        return self.db.get_many(sql, (""))

    # 获得自己开课情况
    def GetMyClassOpen(self,name):
        sql = "select * from 开课表 where 任课老师=%s "
        return self.db.get_many(sql, (name))
    # 获得自己所有选课
    def GetMySc(self,myid):
        sql = "select 开课表.课程号,开课表.课程名,开课表.任课老师,开课表.学分 ,开课表.学时,开课表.星期几,开课表.第几节,开课表.教室,开课表.平时成绩占比,开课表.期末成绩占比 ,开课表.评教等级" \
              " from 开课表,选课表  " \
              "where 选课表.课程号=开课表.课程号 and 选课表.学号=%s"
        return self.db.get_many(sql, (myid))
    # 按条件 获得自己所有选课
    def GetMySearchSc(self,myid,selectNum):
        sql = "select 开课表.课程号,开课表.课程名,开课表.任课老师,开课表.学分 ,开课表.学时,开课表.星期几,开课表.第几节,开课表.教室,开课表.平时成绩占比,开课表.期末成绩占比 ,开课表.评教等级" \
              " from 开课表,选课表  " \
              " where 选课表.课程号=开课表.课程号 and 选课表.学号=%s and 开课表.课程号=%s"
        return self.db.get_many(sql, (myid,selectNum))

    # 获得老师的所有考试时间
    def GetMyExam(self,name):
        sql = "select 课程号,课程名,任课老师,考试时间,考试地点,考试形式 from 开课表  where 任课老师=%s"
        return self.db.get_many(sql, (name))

    # 通过 课程号 获得学生所选课程的 考试时间
    def GetStudentExam(self,objectNum):
        sql = "select 课程号,课程名,任课老师,考试时间,考试地点,考试形式 from 开课表  where 课程号=%s"
        return self.db.get_one(sql, (objectNum))

    def ClassesUpdate(self,objectNum,objectName,name,xuefen,xueshi,jiaoshi,week,classes,qimozhanbi):
        sql="update 开课表 set 课程名=%s,任课老师=%s,学分=%s,学时=%s,星期几=%s ,第几节=%s," \
            "教室=%s,平时成绩占比=%s,期末成绩占比=%s where 课程号=%s"
        qizhongzhanbi=str(1-float(qimozhanbi))
        return self.db.UpdataorInsert(sql, (objectName,name,xuefen,xueshi,week,classes,jiaoshi,qizhongzhanbi,qimozhanbi,objectNum))

    # 考试时间更新
    def ExamUpdate(self,objectNum,shijian,didian,way):
        sql = "update 开课表 set 考试时间=%s,考试地点=%s,考试形式=%s where 课程号=%s"
        return self.db.UpdataorInsert(sql, (shijian,didian,way,objectNum))

    def ClassesInsert(self,objectName,name, xuefen, xueshi, jiaoshi, week, classes, qimozhanbi):
        sqlstr="""
                    insert into 开课表(课程名,任课老师,学分,学时,星期几,第几节,教室,平时成绩占比,期末成绩占比)
                      values(%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        qizhongzhanbi = str(100 - float(qimozhanbi))
        return self.db.UpdataorInsert(sqlstr,(objectName,name,xuefen,xueshi,week,classes, jiaoshi, qizhongzhanbi, qimozhanbi))
    # 添加签到纪录
    def QiandaoInsert(self,myid,objectNum,timemain):
        sqlstr = """
                  insert into 签到表(学号,课程号,签到日期)
                     values(%s,%s,%s)
                            """
        return self.db.UpdataorInsert(sqlstr,(myid,objectNum,timemain))
    # 删除签到纪录
    def QiandaoDelete(self,myid, selectNum, time):
        sql = "delete from 签到表 where 学号=%s and 课程号=%s and 签到时间=%s "
        return self.db.DeleteOne(sql, (myid, selectNum, time))

    def ScInsert(self,objectNum,id):
        sqlstr = """
                   insert into 选课表(学号,课程号)
                      values(%s,%s)
                            """
        return self.db.UpdataorInsert(sqlstr, (id,objectNum))

    # 通过课程号删除开课记录
    def ClassesDelete(self,objectId):
        sql = "delete from 开课表 where 课程号=%s "
        return self.db.DeleteOne(sql, (objectId))

    # 通过学号与课程号删除自己选课记录
    def ScDelete(self, myid,objectId):
        sql = "delete from 选课表 where 学号=%s and 课程号=%s"
        return self.db.DeleteOne(sql, (myid,objectId))

    # 获得所有选课纪录（课程号，课程名，学号，姓名，性别，学院，班级）（三表操作）
    def GetAllOpenandSelect(self):
        sqlstr = """
                     select 开课表.课程号,开课表.课程名,学生表.学号,学生表.姓名,学生表.性别,学生表.学院,学生表.班级 
                     from 开课表,选课表,学生表 where 开课表.课程号=选课表.课程号 and 选课表.学号=学生表.学号
                """
        return self.db.get_many(sqlstr, (""))

    # 按条件查询
    # 获得所有选课纪录（课程号，课程名，学号，姓名，性别，学院，班级）（三表操作）
    def GetOpenandSelect(self,selectNum):
        sqlstr = """
                             select 开课表.课程号,开课表.课程名,学生表.学号,学生表.姓名,学生表.性别,学生表.学院,学生表.班级 
                             from 开课表,选课表,学生表 where 开课表.课程号=选课表.课程号 and 选课表.学号=学生表.学号 and 开课表.课程号=%s
                        """
        return self.db.get_many(sqlstr, (selectNum))

    # 获取学生所有签到纪录
    def GetAllQiandao(self):
        sqlstr = """
                     select 开课表.课程号,开课表.课程名,学生表.学号,学生表.姓名,学生表.学院,学生表.班级,签到表.签到时间,签到表.签到次数 
                      from 开课表,签到表,学生表 where 开课表.课程号=签到表.课程号 and 签到表.学号=学生表.学号
                  """
        return self.db.get_many(sqlstr, (""))

    # 获取自己所有签到纪录
    def GetMyAllQiandao(self,id):
        sqlstr = """
                     select 开课表.课程号,开课表.课程名,学生表.学号,学生表.姓名,学生表.学院,学生表.班级,签到表.签到时间,签到表.签到次数 
                      from 开课表,签到表,学生表 where 开课表.课程号=签到表.课程号 and 签到表.学号=学生表.学号 and 签到表.学号=%s 
                  """
        return self.db.get_many(sqlstr, (id))
    # 按条件筛选课程签到情况
    def GetQiandaoSelect(self,selectNum):
        sqlstr = """
                   select 开课表.课程号,开课表.课程名,学生表.学号,学生表.姓名,学生表.学院,学生表.班级,签到表.签到时间,签到表.签到次数 
                     from 开课表,签到表,学生表 where 开课表.课程号=签到表.课程号 and 签到表.学号=学生表.学号 and 开课表.课程号=%s
                  """
        return self.db.get_many(sqlstr, (selectNum))

    # 按条件筛选自己的课程签到情况
    def GetMyQiandaoSelect(self, selectNum,myid):
        sqlstr = """
                   select 开课表.课程号,开课表.课程名,学生表.学号,学生表.姓名,学生表.学院,学生表.班级,签到表.签到时间,签到表.签到次数 
                     from 开课表,签到表,学生表 where 开课表.课程号=签到表.课程号 and 签到表.学号=学生表.学号 and 开课表.课程号=%s and 签到表.学号=%s
                  """
        return self.db.get_many(sqlstr, (selectNum,myid))

    # 获得所有课程成绩
    def GetAllGrade(self):
        sqlstr = """
                   select 开课表.课程号,开课表.课程名,学生表.学号,学生表.姓名,学生表.学院,学生表.班级,选课表.平时成绩,选课表.期末成绩,选课表.总评 
                      from 开课表,选课表,学生表 where 开课表.课程号=选课表.课程号 and 选课表.学号=学生表.学号
                 """
        return self.db.get_many(sqlstr, (""))

    # 获得所有课程成绩
    def GetMyAllGrade(self,myid):
        sqlstr = """
                   select 开课表.课程号,开课表.课程名,学生表.学号,学生表.姓名,学生表.学院,学生表.班级,选课表.平时成绩,选课表.期末成绩,选课表.总评 
                      from 开课表,选课表,学生表 where 开课表.课程号=选课表.课程号 and 选课表.学号=学生表.学号 and 选课表.学号=%s 
                 """
        return self.db.get_many(sqlstr, (myid))

    # 按条件获得课程成绩
    def GetGradeSelect(self,selectNum):
        sqlstr = """
                   select 开课表.课程号,开课表.课程名,学生表.学号,学生表.姓名,学生表.学院,学生表.班级,选课表.平时成绩,选课表.期末成绩,选课表.总评  
                      from 开课表,选课表,学生表 where 开课表.课程号=选课表.课程号 and 选课表.学号=学生表.学号 and 开课表.课程号=%s
                 """
        return self.db.get_many(sqlstr, (selectNum))

    # 导入大量成绩
    def InsertGrade(self,datalist):
        sqlstr = """
                  insert into 选课表(学号,课程号,平时成绩,期末成绩,总评)
                    values(%s,%s,%s,%s,%s)
               """
        return self.db.UpdataorInsert(sqlstr, datalist)

        # 导入大量学生名单
    def InsertStudents(self, datalist):
        sqlstr = """
                     insert into 学生表(学号,姓名,性别,密码,找回密码,学院,班级)
                       values(%s,%s,%s,%s,%s,%s,%s)
                  """
        return self.db.UpdataorInsert(sqlstr, datalist)

    # 获得所有课程成绩 里面的 所有课程号
    def GetAllClassOfGrade(self):
        sql = "select distinct 课程号 from 选课表 "
        return self.db.get_many(sql, (""))

    # 获取全校所有的课程的全部成绩
    def GetSchoolAllGrade(self):
        sql = "select 学号,课程号,平时成绩,期末成绩,总评 from 选课表 "
        return self.db.get_many(sql, (""))
    # 按一定条件查询全校成绩
    def GetSchoolGradeSelect(self,selectNum):
        sql = "select 学号,课程号,平时成绩,期末成绩,总评 from 选课表 where 课程号 =%s "
        return self.db.get_many(sql, (selectNum))

    # 获取全校的评教
    def GetTeacherComment(self):
        sql = "select 课程号,课程名,任课老师,学分,学时,评教等级 from 开课表 "
        return self.db.get_many(sql, (""))

    # 发布公告
    def noticeInsert(self,text,name):
        sqlstr = """
                   insert into 公告表(内容,发布者)
                     values(%s,%s)
                """
        return self.db.UpdataorInsert(sqlstr, (text,name))

    def noticeSelectAll(self):
        sql = "select * from 公告表"
        return self.db.get_many(sql, (""))

    def GoodorBadInsert(self,selectNum,count):
        sql = "update 开课表 set 评教等级=%s where 课程号=%s "
        print("好评：：：：：",count,selectNum)
        return self.db.UpdataorInsert(sql, (count,selectNum))


    ###################################################
    ## 管理员部分
    # college
    def collegeSelectAll(self):
        sql = "select * from college"
        data = self.db.get_many(sql,(""))
        if data is False:
            return [['', '']]
        return data
    # def collegeUpdate(self):
    #     pass
# department
    def departmentSelectAll(self):
        sql = "select * from department"
        return self.db.get_many(sql,(""))

    def collegeSelectById(self, id):
        sql = "select * from college where id = %s"
        return self.db.get_one(sql, (id))

    def teacherSelectById(self, id):
        if id is None or id is '':
            return ['', '']
        sql = "select * from teacher where id = %s"
        return self.db.get_one(sql, (id))

    def collegeSelectAllName(self):
        sql = "select name from college"
        return self.db.get_oneCol(sql)

    def collegeSelectIdByName(self, name):
        sql = "select id from college where name = %s"
        return self.db.get_oneValue(sql, (name))

    def TeacherSelectAllNameByCollegeId(self, collegeId):
        sql = "select name " \
              "from teacher t," \
              "(select id from department where collegeid = %s ) tmp " \
              "where t.departmentid = tmp.id"
        return self.db.get_oneCol(sql, (collegeId))

        # Teacher
    def teacherSelectAll(self, collegeName, departmentName):
        if collegeName is None and departmentName is None:
            sql = "select * from teacher"
            return self.db.get_all(sql)
        elif collegeName is not None and departmentName is None:
            sql = "select t.* from teacher t,college c,department d " \
                  "where t.departmentid = d.id " \
                  "and d.collegeid = c.id " \
                  "and c.name= %s"
            return self.db.get_all(sql, (collegeName))
        else:
            sql = "select t.* from teacher t,college c,department d " \
                  "where t.departmentid = d.id " \
                  "and d.collegeid = c.id " \
                  "and c.name = %s " \
                  "and d.name = %s"
            return self.db.get_all(sql, (collegeName, departmentName))

    def departmentSelectById(self, id):
        sql = "select * from department where id = %s"
        return self.db.get_one(sql, (id))

    def departmentSelectIdByName(self, name):
        sql = "select id from department where name = %s"
        return self.db.get_oneValue(sql, (name))

    def departmentSelectByCollegeId(self, collegeId):
        sql = "select name from department where collegeid = %s"
        return self.db.get_oneCol(sql, (collegeId))

    # class
    def classSelectAll(self, collegeName, departmentName):
        if collegeName is None and departmentName is None:
            sql = "select * from class"
            data = self.db.get_all(sql)
            if data is False:
                return [['', '', '', '', '']]
            return data
        elif collegeName is not None and departmentName is None:
            sql = "select class.* from class ,college c ,department d " \
                  "where class.departmentid = d.id " \
                  "and d.collegeid = c.id " \
                  "and c.name= %s"
            data = self.db.get_all(sql, (collegeName))
            if data is False:
                return [['', '', '', '', '']]
            return data
        else:
            sql = "select class.* from class ,college c ,department d " \
                  "where class.departmentid = d.id " \
                  "and d.collegeid = c.id " \
                  "and c.name= %s " \
                  "and d.name = %s"
            data = self.db.get_all(sql, (collegeName, departmentName))
            if data is False:
                return [['', '', '', '', '']]
            return data

# Student
    def studentSelectAll(self, collegeName, departmentName, className):
        if collegeName is None and departmentName is None and className is None:
            sql = "select * from student"
            return self.db.get_all(sql)
        elif collegeName is not None and departmentName is None and className is None:
            sql = "select s.* from student s,department d,college c ,class " \
                  "where s.classid = class.id " \
                  "and class.departmentid = d.id " \
                  "and d.collegeid = c.id " \
                  "and c.name = %s"
            return self.db.get_all(sql, (collegeName))
        elif collegeName is not None and departmentName is not None and className is None:
            sql = "select s.* from student s,department d,college c ,class " \
                  "where s.classid = class.id " \
                  "and class.departmentid = d.id " \
                  "and d.collegeid = c.id " \
                  "and c.name = %s " \
                  "and d.name = %s"
            return self.db.get_all(sql, (collegeName, departmentName))
        else:
            sql = "select s.* from student s,department d,college c ,class " \
                  "where s.classid = class.id " \
                  "and class.departmentid = d.id " \
                  "and d.collegeid = c.id " \
                  "and c.name = %s " \
                  "and d.name = %s " \
                  "and class.name = %s"
            return self.db.get_all(sql, (collegeName, departmentName, className))

    def classSelectById(self, id):
        sql = "select * from class where id = %s"
        return self.db.get_one(sql, (id))

    def classSelectIdByName(self, name):
        sql = "select id from class where name = %s"
        return self.db.get_oneCol(sql, (name))

    def classSelectByDepartmentId(self, departmentId):
        sql = "select name from class where departmentid = %s"
        return self.db.get_oneCol(sql, (departmentId))

    def classUpdate(self, id, grade, name, departmentId, teacher):
        sql = "update class set grade = %s,name = %s, departmentId = %s ,teacher= %s where id = %s"
        return self.db.UpdataorInsert(sql, (grade, name, departmentId, teacher, id))

    def classInsert(self, id, grade, name, departmentId, teacher):
        sql = "insert into class values(%s,%s,%s,%s,%s)"
        return self.db.UpdataorInsert(sql, (id, grade, name, departmentId, teacher))

    def classDelete(self, id):
        sql = "delete from class where id = %s"
        return self.db.DeleteOne(sql, (id))
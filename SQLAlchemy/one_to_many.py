# -*- coding : utf-8
# @Time: 2025-05-01
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session, relationship

# 声明基类
Base = declarative_base()
# 创建引擎，连接到数据库
username = "root"
pwd = "123456"
ip = "127.0.0.1"
port = "3306"
database = "bms"
engine = create_engine(f'mysql+pymysql://{username}:{pwd}@{ip}:{port}/{database}')
# 创建session对象，绑定到数据库引擎上
DBSession = sessionmaker(bind=engine)
db_session: Session = DBSession()


# 班级表
class ClassInfo(Base):
    __tablename__ = "class_info"
    # 班级ID
    id = Column(Integer, primary_key=True)
    # 班级名称
    name = Column(String(30))

    def __repr__(self):
        return f"<Class id: {self.id}, name: {self.name}>"


# 学生表
class StudentInfo(Base):
    __tablename__ = "student_info"
    # 学生ID
    id = Column(Integer, primary_key=True)
    # 学生姓名
    name = Column(String(30))
    # 通过外键建立对应的关系
    class_id = Column(Integer, ForeignKey("class_info.id"))
    # 反射关系
    class_info = relationship("ClassInfo", backref="student_info")

    def __repr__(self):
        return f"<Student id: {self.id}, name: {self.name}, class_id: {self.class_id}>"


if __name__ == '__main__':
    # 创建表
    Base.metadata.create_all(engine)
    # 添加数据，在班级表中添加两条数据
    # class1 = ClassInfo(id=1, name="测试开发班1期")
    # class2 = ClassInfo(id=2, name="测试开发班2期")
    # db_session.add_all([class1, class2])
    # 在学生表中添加四条数据
    # stu1 = StudentInfo(id=1, name="张三", class_id=1)
    # stu2 = StudentInfo(id=2, name="李四", class_id=1)
    # stu3 = StudentInfo(id=3, name="王五", class_id=2)
    # stu4 = StudentInfo(id=4, name="Tom", class_id=2)
    # db_session.add_all([stu1, stu2, stu3, stu4])

    # 多查一：通过student 查询 class
    # stu_info = db_session.query(StudentInfo).filter_by(id=4).first()
    # print(stu_info)
    # # 直接访问学生对象的班级id属性
    # print(stu_info.class_id)
    # # 通过反向关联，获取到关联表（ClassInfo）的属性
    # print(stu_info.class_info.id)
    # print(stu_info.class_info.name)

    # 一查多：通过班级查询学生信息
    # my_class = db_session.query(ClassInfo).filter_by(id=1).first()
    # print(my_class)
    # # 查询班级 id 为1 的班级中所有的学生
    # print(my_class.student_info)
    # # 获取到某个学生
    # print(my_class.student_info[0].name)

    # 通过一改多
    # 查找班级--找到要修改的学生  -- 修改对应学生的属性
    # my_class.student_info[0].name = "张三-修改"
    # print(my_class.student_info[0].name)

    # 通过多改一
    # 查找学生 -- 找到对应的班级 -- 修改班级属性
    # stu = db_session.query(StudentInfo).filter_by(id=2).first()
    # print(stu.class_info.name)
    # stu.class_info.name = "测试开发进阶1班"
    # print(stu.class_info.name)

    # 删除
    # 删除多，删除一个学生，不影响班级
    # stu = db_session.query(StudentInfo).filter_by(id=3).first()
    # db_session.delete(stu)

    # 删除一个班级下所有学生
    my_class = db_session.query(ClassInfo).filter_by(id=1).first()
    print(my_class.student_info)
    db_session.query(StudentInfo).filter_by(class_id=my_class.id).delete()

    # 提交操作
    db_session.commit()
    # 关闭连接
    db_session.close()

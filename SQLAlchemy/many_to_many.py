# -*- coding : utf-8
# @Time: 2025-05-01
# 声明基类
from sqlalchemy import Column, Integer, String, Table, ForeignKey
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

# 定义中间表
teacher_student_rel = Table(
    # 指定中间表的表名
    "teacher_student",
    Base.metadata,
    # 中间表id,自己的主键
    Column("id", Integer, primary_key=True),
    # 设置外键，关联两张主表
    Column("teacher_id", Integer, ForeignKey("teacher.id")),
    Column("student_id", Integer, ForeignKey("student.id"))
)


# 定义教师表
class Teacher(Base):
    __tablename__ = "teacher"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    # 定义表关联关系
    # 第一个参数：指向另一张主表，传入学生表的类名
    # 第二个参数：通过secondary指向中间表
    # 第三个参数：反向指定，backref指向当前表
    students = relationship(
        "Student",
        secondary=teacher_student_rel,
        backref="teachers"
    )

    def __repr__(self):
        return f"<Teacher id: {self.id}, name: {self.name}>"


# 定义学生表
class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"<Student id: {self.id}, name: {self.name}>"


if __name__ == '__main__':
    # 创建表
    # Base.metadata.create_all(engine)
    # 添加数据
    # stu1 = Student(name="张三")
    # stu2 = Student(name="李四")
    # stu3 = Student(name="王五")
    # tea1 = Teacher(name="张老师")
    # tea2 = Teacher(name="李老师")
    # tea3 = Teacher(name="王老师")
    # # 批量添加到表中
    # db_session.add_all([stu1, stu2, stu3, tea1, tea2, tea3])
    # # 建立关联关系
    # tea1.students = [stu1, stu2]
    # tea2.students = [stu3, stu2]
    # tea3.students = [stu1, stu2, stu3]

    # 通过学生查询老师
    # stu = db_session.query(Student).filter_by(id=1).first()
    # print(stu.teachers)
    # print(stu.teachers[0].name)
    # 通过老师查学生
    # tea = db_session.query(Teacher).filter_by(id=3).first()
    # print(tea.students)
    # print(tea.students[2].name)

    # 更新数据
    # 修改某位同学对应老师的属性
    # stu1 = db_session.query(Student).filter_by(id=2).first()
    # print(stu1.teachers)
    # stu1.teachers[0].name = "钱老师"

    # 修改某位老师对应的学生的属性
    # tea1 = db_session.query(Teacher).filter_by(id=1).first()
    # print(tea1.students)
    # tea1.students[1].name = "Tom"

    # 删除数据
    # 删除学生
    # stu2 = db_session.query(Student).filter_by(id=3).first()
    # db_session.delete(stu2)

    # 删除老师
    tea2 = db_session.query(Teacher).filter_by(id=1).first()
    db_session.delete(tea2)

    # 提交操作
    db_session.commit()
    # 关闭连接
    db_session.close()

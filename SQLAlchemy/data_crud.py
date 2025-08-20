# -*- coding : utf-8
# @Time: 2025-05-01
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# 声明基类
Base = declarative_base()
# 创建引擎，连接到mysql数据库
username = "root"
pwd = "123456"
ip = "127.0.0.1"
port = "3306"
database = "bms"
engine = create_engine(f'mysql+pymysql://{username}:{pwd}@{ip}:{port}/{database}')
# 创建session对象，绑定到数据库引擎上
DBSession = sessionmaker(bind=engine)
# 获取会话实例
db_session: Session = DBSession()


# 定义数据库表结构，需要继承Base
class UserInfo(Base):
    # 自定义表名
    __tablename__ = "user"
    # 定义表字段（表列名）
    # 第一个参数指定数据的类型，后面指定其他列选项，primary_key=True 设置为主键
    id = Column(Integer, primary_key=True, comment="用户ID")
    # nullable=False 不可以为空，unique=True 不可重复
    username = Column(String(80), nullable=False, unique=True, comment="用户名")
    email = Column(String(120), nullable=False, unique=True, comment="用户邮箱")
    gender = Column(String(4), comment="性别")

    def __repr__(self):
        # 魔法方法，直观展示类或者对象的数据（自我描述方法）
        return f"<UserInfo {self.username}>"


if __name__ == '__main__':
    # 创建表
    # Base.metadata.create_all(engine)

    # 新增单条数据
    # 实例化表的类
    # user1 = UserInfo(id=1, username="张三", email="zhangsan@163.com")
    # 把数据添加到session中
    # 批量添加
    # user2 = UserInfo(id=2, username="里斯", email="lisi@163.com", gender="男")
    # user3 = UserInfo(id=3, username="Jack", email="Jack@163.com", gender="女")
    # 第一种批量添加的方法
    # db_session.add(user2)
    # db_session.add(user3)
    # 第二种批量添加的方式
    # user4 = UserInfo(id=4, username="成龙", email="chenglong@163.com", gender="男")
    # user5 = UserInfo(id=5, username="杰伦", email="jielun@163.com", gender="女")
    # 批量添加
    # db_session.add_all([user4, user5])
    # 提交操作
    # db_session.commit()

    # 查询
    # 查询所有数据
    # datas = db_session.query(UserInfo).all()
    # print(datas)
    # # 通过单个条件查询单条数据
    # user = db_session.query(UserInfo).filter_by(username="张三").all()
    # print(user)
    # # 多条件查询多条数据
    # users_more = db_session.query(UserInfo).filter_by(username="杰伦").filter_by(id=5).all()
    # print(users_more)
    # # 多条件查询单条数据
    # user_more = db_session.query(UserInfo).filter_by(username="杰伦").filter_by(id=5).first()
    # print(user_more)
    # # 获取查询对象的属性
    # user_email = user_more.email
    # print(user_email)
    # user_name = users_more[0].username
    # print(user_name)

    # 更新
    # 第一种更新方式
    # user = db_session.query(UserInfo).filter_by(id=1).first()
    # user.username = "Lily"
    # 第二种更新方式
    # db_session.query(UserInfo).filter_by(id=4).update({"username": "Tom"})

    # 删除
    # 第一种删除方式
    # user = db_session.query(UserInfo).filter_by(id=5).first()
    # 删除对应的对象
    # db_session.delete(user)
    # 第二种删除方式
    db_session.query(UserInfo).filter_by(id=4).delete()
    # 提交操作
    db_session.commit()
    # 关闭连接
    db_session.close()

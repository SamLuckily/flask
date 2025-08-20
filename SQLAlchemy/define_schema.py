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
    Base.metadata.create_all(engine)

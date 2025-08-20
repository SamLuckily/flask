# -*- coding : utf-8
# @Time: 2025-04-28
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


# 定义表结构
class User(Base):
    # 自定义表名
    __tablename__ = "user"

    # 定义表字段
    id = Column(Integer, primary_key=True)
    username = Column(String(80))
    password = Column(String(80))


if __name__ == '__main__':
    # 创建表
    # Base.metadata.create_all(engine)
    # 删除表
    Base.metadata.drop_all(engine)

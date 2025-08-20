# -*- coding : utf-8
# @Time: 2025-05-07
# 导入要创建的表
from backend_arc_design.do.course_do import CourseDo
from backend_arc_design.server import engine, Base

if __name__ == '__main__':
    # 创建表
    Base.metadata.create_all(engine)

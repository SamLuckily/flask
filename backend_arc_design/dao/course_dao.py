# -*- coding : utf-8
# @Time: 2025-05-07
# 处理数据库相关的操作
from backend_arc_design.do.course_do import CourseDo
from backend_arc_design.server import db_session


class CourseDao:
    def get(self, course_id: int) -> CourseDo:
        """
        通过id查询单条记录
        :param course_id: 课程 id
        :return: 课程对象
        """
        course = db_session.query(CourseDo).filter_by(id=course_id).first()
        return course

    def list(self) -> [CourseDo]:
        """
        查询表中所有记录
        :return: 课程对象列表
        """
        course_list = db_session.query(CourseDo).all()
        return course_list

    def create(self, course: CourseDo):
        """
        课程表中添加数据
        :param course: 课程对象
        :return: 课程id
        """
        # 添加表
        db_session.add(course)
        # 提交操作
        db_session.commit()
        # 返回添加的课程id
        return course.id

    def update(self, course_info: dict):
        """
        更新课程表中的数据
        :param course_info: 课程信息， 使用字典格式
        :return: 课程id
        """
        # 获取要更新的课程id
        course_id = course_info.get("id")
        # 通过课程id更新课程数据
        db_session.query(CourseDo).filter_by(id=course_id).update(course_info)
        # 提交操作
        db_session.commit()
        return course_id

    def delete(self, course_id: int):
        """
        删除课程表中的数据
        :param course_id: 课程id
        :return:
        """
        # 删除课程
        db_session.query(CourseDo).filter_by(id=course_id).delete()
        # 提交操作
        db_session.commit()
        return course_id

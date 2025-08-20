# -*- coding : utf-8
# @Time: 2025-05-08
import logging

from backend_arc_design.dao.course_dao import CourseDao

# 获取基础数据库操作实例
from backend_arc_design.do.course_do import CourseDo

course_dao: CourseDao = CourseDao()


class CourseService:
    # 实现业务方法，复杂的业务逻辑放在这一层
    def get(self, course_id: int):
        """
        通过课程id 获取课程信息
        :param course_id: 课程id
        :return: 课程对象
        """
        # 通过id 查询课程
        course = course_dao.get(course_id)
        # 返回课程对象
        return course

    def create(self, course_info: dict):
        """
        新增课程
        :param course_info: 字典格式的课程信息
        :return: 课程id
        """
        logging.info(f"要添加的课程信息为 {course_info}")
        # 创建课程对象
        course = CourseDo(**course_info)
        # 新增课程
        course_id = course_dao.create(course)
        # 返回课程id
        return course_id

    def list(self):
        """
        获取所有课程信息
        :return: 课程列表
        """
        course_list = course_dao.list()
        return course_list

    def update(self, course_info: dict):
        """
        更新课程
        :param course_info: 字典格式的课程信息
        :return:
        """
        course_id = course_dao.update(course_info)
        return course_id

    def delete(self, course_id: int):
        """
        删除课程
        :param course_id: 要删除的课程的id
        :return: 课程id
        """
        course_id = course_dao.delete(course_id)
        return course_id

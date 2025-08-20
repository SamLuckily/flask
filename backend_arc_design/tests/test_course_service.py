# -*- coding : utf-8
# @Time: 2025-05-08
from backend_arc_design.service.course_service import CourseService


class TestCourseService:
    def setup_class(self):
        self.cs = CourseService()

    def test_create(self):
        """
        测试新增方法
        :return:
        """
        course_info = {
            "id": 2,
            "name": "Java测试开发",
            "detail": "Java测试开发进阶班级"
        }
        course_id = self.cs.create(course_info)
        assert course_id == 2

    def test_get(self):
        """
        查询测试方法
        :return:
        """
        course = self.cs.get(1)
        print(course)
        assert course.name == "python测试开发"

    def test_list(self):
        """
        测试获取全部课程方法
        :return:
        """
        course_list = self.cs.list()
        print(course_list)
        # 获取全部课程 id 的列表
        course_id_list = [c.id for c in course_list]
        print(course_id_list)
        assert 1 in course_id_list

    def test_update(self):
        """
        测试更新课程方法
        :return:
        """
        course_info = {
            "id": 2,
            "name": "Java测试开发工程师",
            "detail": "Java测试开发进阶班"
        }
        course_id = self.cs.update(course_info)
        assert course_id == 2
        course = self.cs.get(2)
        assert course.detail == "Java测试开发进阶班"

    def test_delete(self):
        """
        测试删除课程方法
        """
        course_id = self.cs.delete(2)
        course_list = self.cs.list()
        course_id_list = [c.id for c in course_list]
        print(course_id_list)
        assert course_id not in course_id_list

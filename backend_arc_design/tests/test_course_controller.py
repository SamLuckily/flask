# -*- coding : utf-8
# @Time: 2025-05-10
import json

import requests as requests


class TestCourseController:
    def setup_class(self):
        self.base_url = "http://127.0.0.1:5055/course"
        self.course_id = 66

    def test_create_course(self):
        """
        添加课程
        :return:
        """
        data = {
            "id": self.course_id,
            "name": "Java测试开发",
            "detail": "Java测试开发从入门到精通"
        }
        r = requests.post(self.base_url, json=data)
        print(r.json())
        assert r.status_code == 200
        assert r.json().get("errcode") == 0

    def test_get_course(self):
        """
        查询课程
        :return:
        """
        get_url = f"{self.base_url}/{self.course_id}"
        r = requests.get(get_url)
        data = json.loads(r.text)
        print(json.dumps(data, ensure_ascii=False))
        assert r.status_code == 200
        assert r.json().get("errcode") == 0

    def test_list_course(self):
        """
        获取全部课程
        :return:
        """
        list_url = f"{self.base_url}/list"
        r = requests.get(list_url)
        data = json.loads(r.text)
        print(json.dumps(data, ensure_ascii=False))
        assert r.status_code == 200
        assert r.json().get("errcode") == 0

    def test_update_course(self):
        """
        更新课程
        :return:
        """
        data = {
            "id": self.course_id,
            "name": "python测试开发啦",
            "detail": "测试开发进阶班级啦"
        }
        r = requests.put(self.base_url, json=data)
        data = json.loads(r.text)
        print(json.dumps(data, ensure_ascii=False))
        assert r.status_code == 200
        assert r.json().get("errcode") == 0

    def test_delete_course(self):
        """
        删除课程
        :return:
        """
        delete_url = f"{self.base_url}/{self.course_id}"
        r = requests.delete(delete_url)
        data = json.loads(r.text)
        print(json.dumps(data, ensure_ascii=False))
        assert r.status_code == 200
        assert r.json().get("errcode") == 0

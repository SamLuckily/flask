# -*- coding : utf-8
# @Time: 2025-05-08
# 定义pydantic对象，用于数据验证与解析
from typing import Optional

from pydantic import BaseModel, ConfigDict, constr


class CourseDto(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: constr(max_length=30)
    detail: Optional[constr(max_length=255)] = ""

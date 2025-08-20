# -*- coding : utf-8
# @Time: 2025-05-07
from typing import Optional
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from backend_arc_design.server import Base


# 定义orm对象用于操作数据库
class CourseDo(Base):
    __tablename__ = "t_course"

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    detail: Mapped[Optional[str]] = mapped_column(String(255), default='')

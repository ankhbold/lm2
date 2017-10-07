__author__ = 'ankhbold'

from sqlalchemy import Column, String, Integer
from Base import *


class VaTypeIrrigation(Base):

    __tablename__ = 'cl_type_irrigation_system'

    code = Column(Integer, primary_key=True)
    description = Column(String)
    description_en = Column(String)


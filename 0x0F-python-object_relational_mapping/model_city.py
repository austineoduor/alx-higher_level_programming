#!/usr/bin/python3
"""
python file that contains the class definition of a
Cities and an instance Base = declarative_base()
"""
#!/usr/bin/python3
"""
contains the class City
"""

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """Representation of a city"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
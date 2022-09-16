#!/usr/bin/python3

""" City Module for HBNB project """

from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models import storage_type


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = "cities"

    if storage_type == "db":

        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)

        name = Column(String(128), nullable=False)

        places = relationship("Place", cascade="all, delete", backref="cities")

    else:

        state_id = ""

        name = ""

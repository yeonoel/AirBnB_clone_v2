#!/usr/bin/python3
""" state Module for HBNB project """

from os import getenv
import models
from models import storage_type
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"

    if storage_type == "db":

        name = Column(String(128), nullable=False)

        cities = relationship("City", cascade="all, delete", backref="state")

    else:

        name = ""

        @property
        def cities(self):

            """ Returns the list of City instances with

            state_id equals to the current State.id """

            cities = models.storage.all(City)

            lst = []

            for city in cities.values():

                if city.state_id == self.id:

                    lst.append(city)
            return lst


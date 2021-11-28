from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.base import Base


class League(Base):
    __tablename__ = 'leagues'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    short_name = Column(String(255))

    games = relationship("Game", back_populates="league")

    def __repr__(self):
        return f"<League: {self.name}>"


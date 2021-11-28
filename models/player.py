from sqlalchemy import Column, Integer, String
from models.base import Base


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    def __repr__(self):
        return f"<Player: {self.name}>"

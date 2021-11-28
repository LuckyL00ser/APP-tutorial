from sqlalchemy import Column, Integer, String, ForeignKey, Float
from models.base import Base


class Shot(Base):
    __tablename__ = 'shots'

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer,ForeignKey('games.id'))
    shooter_id = Column(Integer, ForeignKey('players.id'))
    assister_id = Column(Integer, ForeignKey('players.id'))
    minute = Column(Integer)
    situation = Column(String(255))
    last_action = Column(String(255))
    shot_type = Column(String(255))
    shot_result = Column(String(255))
    x_goal = Column(Float)
    position_x = Column(Float)
    position_y = Column(Float)


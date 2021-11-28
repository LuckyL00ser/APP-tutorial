from sqlalchemy import Column, Integer, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base


class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    league_id = Column(Integer, ForeignKey('leagues.id'))
    home_team_id = Column(Integer, ForeignKey('teams.id'))
    away_team_id = Column(Integer, ForeignKey('teams.id'))
    season = Column(Integer)
    date = Column(DateTime)
    home_goals = Column(Integer)
    away_goals = Column(Integer)
    home_probability = Column(Float)
    draw_probability = Column(Float)

    league = relationship("League", back_populates="games")
    home_team = relationship("Team", foreign_keys=[home_team_id])
    away_team = relationship("Team", foreign_keys=[away_team_id])

    def __repr__(self):
        return f"<Game: id={self.id}>"





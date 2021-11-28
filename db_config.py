from sqlalchemy import create_engine

#https://www.kaggle.com/technika148/football-database

username = "library"
password = "SuperDifficultPassword_5"
host = "localhost"
port = "3306"
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/library", echo=True)

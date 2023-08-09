from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP,MetaData,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql://:@localhost/postgres"
engine = create_engine(DATABASE_URL)

metadata = MetaData()
metadata.reflect(engine)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base(metadata=metadata)

class User(Base):
    __tablename__ = 'users'

    def __init__(self,user_id, username, email, password):
        self.user_id=user_id
        self.username = username
        self.email = email 
        self.password = password

    def to_json(self):
        print("Did we call this badla")
        return {
            'id': self.user_id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat()
        }

User.__table__ = Table('users', metadata, autoload=True, autoload_with=engine)


def get_by_username(username_to_fetch):
    user = session.query(User).filter_by(username=username_to_fetch).first()
    return user.to_json()

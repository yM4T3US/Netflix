from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class BancoDados:

    engine = create_engine("sqlite:///netflix.db", echo=True)
    Session = sessionmaker(bind=engine)
    Base = declarative_base()

    def __init__(self):

        self.Base.metadata.create_all(self.engine)
        self.session = self.Session()

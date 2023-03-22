from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .entidades import Base

class DBConnHandler():
    
    def __init__(self, DBparams:dict) -> None:
        self._params = DBparams
        self._endpointDB = f"{self._params['dialectDB']}+{self._params['driverDB']}://{self._params['userDB']}:{self._params['password']}@{self._params['host']}:{self._params['port']}/{self._params['database']}"
        self.engine = create_engine(self._endpointDB)
        self.session = self.dbSession()
    
    def addTableDB(self):
        return Base.metadata.create_all(self.engine)

    def dbSession(self):
        session_maker = sessionmaker(bind=self.engine)
        self.session = session_maker()
        return self.session
    
    


    

    

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Float,Text


''' Mapeando entidades '''

Base = declarative_base()
class CinemaBr(Base):
    
    __tablename__ = 'cinemabr'

    id = Column(Integer, primary_key=True)
    titulo_br = Column(String(100), nullable=False)
    titulo_original = Column(String(100))
    data_estreia = Column(String(20), nullable=False)
    rating = Column(Float, nullable=False)
    num_avaliacoes = Column(Float)




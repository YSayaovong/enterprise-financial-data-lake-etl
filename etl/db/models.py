from sqlalchemy import create_engine, Column, Integer, String, Date, Numeric, BigInteger, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from etl.settings import settings

Base = declarative_base()
engine = create_engine(settings.db_url)
SessionLocal = sessionmaker(bind=engine)

class Instrument(Base):
    __tablename__ = 'instruments'
    id = Column(Integer, primary_key=True)
    symbol = Column(String(10), unique=True, nullable=False)
    name = Column(String)
    type = Column(String(20))
    currency = Column(String(10))

class DailyPrice(Base):
    __tablename__ = 'daily_prices'
    id = Column(Integer, primary_key=True)
    instrument_id = Column(Integer, ForeignKey('instruments.id'))
    date = Column(Date, nullable=False)
    open = Column(Numeric)
    high = Column(Numeric)
    low = Column(Numeric)
    close = Column(Numeric)
    volume = Column(BigInteger)

def init_db():
    Base.metadata.create_all(engine)

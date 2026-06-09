from sqlalchemy import Column, Integer, String, Float
from app.database import Base


class Trace(Base):
    __tablename__ = "traces"

    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(String)
    response = Column(String)
    time_taken = Column(Float)
    model_name = Column(String)
    timestamp = Column(Float)
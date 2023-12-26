from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class DatabaseModel(Base):
    __tablename__ = 'invoice_data'

    id = Column(Integer, primary_key=True)
    client_number = Column(Float)
    month_ref = Column(String(10))
    electricity_quantity = Column(Float)
    electricity_total_value = Column(Float)
    sceee_quantity = Column(Float)
    sceee_total_value = Column(Float)
    comp_gd_i_quantity = Column(Float)
    comp_gd_i_total_value = Column(Float)
    cont_public_ilu_value = Column(String)
    file_name = Column(String)

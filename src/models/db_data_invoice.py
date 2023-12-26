from src.configs.base import Base
from sqlalchemy import Column, Integer, String, Float


class InvoiceDB(Base):
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

    def __repr__(self):
        return f"Invoice [numero do cliente={self.client_number}, Mes de referencia={self.month_ref}, " \
               f"Energia Eletrica={self.electricity_quantity, self.electricity_total_value}, " \
               f"Energia SCEEE s/ICMS={self.sceee_quantity, self.sceee_total_value}," \
               f"Energia Compensada GD I]={self.comp_gd_i_quantity, self.comp_gd_i_total_value}," \
               f"Contrib Ilum Publica Municipal={self.cont_public_ilu_value}, Nome do pdf={self.file_name}"
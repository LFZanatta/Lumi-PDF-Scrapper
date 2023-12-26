import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.configs.base import Base
from src.configs.connection import DBConnectionHandler
from src.repository import invoice


class DatabaseController:
    def __init__(self):
        load_dotenv()
        self.engine = create_engine(os.environ.get('DATABASE_URL'))
        self.Base = Base
        self.Session = sessionmaker(bind=self.engine)
        self.session = None

    def initialize_database(self):
        self.Base.metadata.create_all(self.engine)

    @staticmethod
    def insert_invoice(data):
        with DBConnectionHandler() as db:
            try:
                invoice.InvoiceData.insert(**data)
            except Exception as e:
                print(f"Error inserting data: {e}")

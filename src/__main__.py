import os
from dotenv import load_dotenv

from controllers.database import DatabaseController
from models import ScrapperModel


def main():
    load_dotenv()

    db_controller = DatabaseController()

    # Inicia o banco e cria tabela
    db_controller.initialize_database()

    scrapper_instance = ScrapperModel()

    pdf_path = os.environ.get('FILES_PATH')
    invoice_data = scrapper_instance.get_invoice_data(pdf_path)

    for data in invoice_data:
        DatabaseController.insert_invoice(data)


if __name__ == "__main__":
    main()

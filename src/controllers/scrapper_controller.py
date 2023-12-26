import re
import os
import PyPDF2


class ScrapperController:

    @staticmethod
    def get_pdf_text(pdf_path):

        # Lendo doc em modo binario
        with open(pdf_path, 'rb') as file:
            main_page = PyPDF2.PdfReader(file).pages[0]
            text = main_page.extract_text()

        return text

    @staticmethod
    def get_files_from_path(path):
        file_path = []
        for filename in os.listdir(path):
            if filename.endswith(".pdf"):
                file_path.append(os.path.join(path, filename))

        return file_path

    @staticmethod
    def extract_client_number(text):
        find_client_numb = re.search(r'N[º\s]*[DO\s]*CLIENTE\D*(\d+)', text, re.IGNORECASE)

        if find_client_numb:
            client_number = find_client_numb.group(1)

        return client_number

    @staticmethod
    def extract_month_ref(text):
        find_month_ref = re.search(r'Referente\s+a\D*([a-zA-Z]{3}/\d{4})', text)

        if find_month_ref:
            month_ref = find_month_ref.group(1)

        return month_ref

    @staticmethod
    def extract_public_ilum(text):
        find_public_ilum = re.search(r'Contrib Ilum Publica Municipal\s+(\d+,\d+)', text)

        if find_public_ilum:
            public_ilum = find_public_ilum.group(1)

        return public_ilum

    @staticmethod
    def match_energy_value(energy_value, energy_type):
        extract_energy_data_formatted = re.findall(r'(-?\d+(?:,\d+)?(?:\.\d+)?)', energy_value)

        energy_data = {
            'type': energy_type,
            'quantity': float(extract_energy_data_formatted[0].replace('.', '')),
            'price_unit': float(extract_energy_data_formatted[1].replace(',', '.')),
            'total_value': float(extract_energy_data_formatted[2].replace(',', '.')),
        }

        return energy_data

import re
from src.controllers.scrapper_controller import ScrapperController


class ScrapperModel:

    @staticmethod
    def extract_energy_data(text):
        energy_value = []
        scrapper_instance = ScrapperController()

        scee_energy = re.search(r'Energia SCEE s/ ICMS kWh\s+(\d.+)\s+([\d.,-]+)\s+([\d.,-]+)\s+([\d.,-]+)',
                                text).group(0)
        eletric = re.search(r'Energia\s+(\w+\s+\w+)\s+(\d+)\s+([\d.,-]+)\s+([\d.,-]+)\s+([\d.,-]+)', text).group(0)
        compe_energy = re.search(r'Energia compensada GD I kWh\s+(\D.+)', text).group(1)

        energy_value.append(scrapper_instance.match_energy_value(eletric, " Energia Elétrica "))
        energy_value.append(scrapper_instance.match_energy_value(scee_energy, " Energia SCEE s/ ICMS "))
        energy_value.append(scrapper_instance.match_energy_value(compe_energy, " Energia compensada GD I "))

        return energy_value

    @staticmethod
    def get_invoice_data(path):
        all_data = []
        scrapper_instance = ScrapperController()
        model_instance = ScrapperModel()

        origin_pdf_file = scrapper_instance.get_files_from_path(path)
        for pdf_file in origin_pdf_file:
            pdf_text = scrapper_instance.get_pdf_text(pdf_file)

            client_number = scrapper_instance.extract_client_number(pdf_text)
            month_ref = scrapper_instance.extract_month_ref(pdf_text)
            public_ilum = scrapper_instance.extract_public_ilum(pdf_text)
            energy_data = model_instance.extract_energy_data(pdf_text)

            invoice_data = {
                'client_number': client_number,
                'month_ref': month_ref,
                'electricity_quantity': energy_data[0]['quantity'],
                'electricity_total_value': energy_data[0]['total_value'],
                'sceee_quantity': energy_data[1]['quantity'],
                'sceee_total_value': energy_data[1]['total_value'],
                'comp_gd_i_quantity': energy_data[2]['quantity'],
                'comp_gd_i_total_value': energy_data[2]['total_value'],
                'cont_public_ilu_value': public_ilum,
                'file_name': pdf_file
            }

            all_data.append(invoice_data)

        return all_data

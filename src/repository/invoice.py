from src.configs.connection import DBConnectionHandler
from src.models import db_data_invoice


class InvoiceData:

    @staticmethod
    def insert(client_number, month_ref, electricity_quantity, electricity_total_value,
               sceee_quantity, sceee_total_value, comp_gd_i_quantity, comp_gd_i_total_value,
               cont_public_ilu_value, file_name):

        with DBConnectionHandler() as db:
            try:
                data_insert = db_data_invoice.InvoiceDB(client_number=client_number, month_ref=month_ref,
                                                        electricity_quantity=electricity_quantity,
                                                        electricity_total_value=electricity_total_value,
                                                        sceee_quantity=sceee_quantity,
                                                        sceee_total_value=sceee_total_value,
                                                        comp_gd_i_quantity=comp_gd_i_quantity,
                                                        comp_gd_i_total_value=comp_gd_i_total_value,
                                                        cont_public_ilu_value=cont_public_ilu_value,
                                                        file_name=file_name)

                db.session.add(data_insert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

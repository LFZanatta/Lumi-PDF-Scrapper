from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.db_data_invoice import InvoiceDB

session = UnifiedAlchemyMagicMock(
    data=[
        (
            [InvoiceDB(client_number='7202187422', month_ref='JUL/2023', electricity_quantity='50.0',
                       electricity_total_value='47.96', sceee_quantity='297.0', sceee_total_value='152.02',
                       comp_gd_i_quantity='297.0', comp_gd_i_total_value='-144.73', cont_public_ilu_value='49,43',
                       file_name="luminaOTeste.PDF")]
        )
    ]
)


def test_select():
    response = session.query(InvoiceDB).filter(InvoiceDB.client_number == '7202187422')
    print(response)

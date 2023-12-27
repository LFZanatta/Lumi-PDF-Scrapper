from unittest.mock import patch
from src.repository.invoice import InvoiceData


def test_insert():
    with patch('src.repository.invoice.DBConnectionHandler') as mock_db_connection_handler:
        InvoiceData.insert('12345', 'JUL/2023', 50.0, 47.96, 297.0, 152.02, 297.0, -144.73, '49,43', 'test.pdf')

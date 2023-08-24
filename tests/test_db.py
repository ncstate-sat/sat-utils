from unittest import main, mock, TestCase
from unittest.mock import patch
import os

class TestDatabaseConnectivity(TestCase):

    @patch.dict(os.environ, {"SERVER_CONN": "Fake Connection String"}, clear=True)
    def test_get_named_db_connection(self):
        from sat.db import get_named_db_connection, ConnectionType as ctype
        with patch("pyodbc.connect") as mockeddb:
            mockeddb.add = mock.MagicMock(return_value = "Connected")
            conn = get_named_db_connection("SERVER_CONN", ctype.SQL)
        assert conn

    def test_oracle_connection(self):
        pass
        
if __name__ == "__main__":
    main()
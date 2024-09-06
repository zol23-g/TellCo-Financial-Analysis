import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.db_connection import get_db_connection, close_db_connection, load_data

class TestDBConnection(unittest.TestCase):

    @patch('scripts.db_connection.create_engine')
    def test_get_db_connection(self, mock_create_engine):
        # Mock the engine
        mock_engine = MagicMock()
        mock_create_engine.return_value = mock_engine

        db_config = {
            'user': 'test_user',
            'password': 'test_password',
            'host': 'localhost',
            'port': '5432',
            'database': 'test_db'
        }

        engine = get_db_connection(db_config)
        mock_create_engine.assert_called_once_with(
            'postgresql://test_user:test_password@localhost:5432/test_db'
        )
        self.assertEqual(engine, mock_engine)

    @patch('scripts.db_connection.create_engine')
    def test_close_db_connection(self, mock_create_engine):
        # Mock the engine
        mock_engine = MagicMock()
        mock_create_engine.return_value = mock_engine

        db_config = {
            'user': 'test_user',
            'password': 'test_password',
            'host': 'localhost',
            'port': '5432',
            'database': 'test_db'
        }

        engine = get_db_connection(db_config)
        close_db_connection(engine)
        engine.dispose.assert_called_once()

    @patch('scripts.db_connection.create_engine')
    @patch('pandas.read_sql')
    def test_load_data(self, mock_read_sql, mock_create_engine):
        # Mock the engine and the read_sql function
        mock_engine = MagicMock()
        mock_create_engine.return_value = mock_engine
        mock_df = pd.DataFrame({'column1': [1, 2], 'column2': ['a', 'b']})
        mock_read_sql.return_value = mock_df

        db_config = {
            'user': 'test_user',
            'password': 'test_password',
            'host': 'localhost',
            'port': '5432',
            'database': 'test_db'
        }
        query = "SELECT * FROM test_table"

        df = load_data(query, db_config)
        mock_create_engine.assert_called_once_with(
            'postgresql://test_user:test_password@localhost:5432/test_db'
        )
        mock_read_sql.assert_called_once_with(query, mock_engine)
        mock_engine.dispose.assert_called_once()
        pd.testing.assert_frame_equal(df, mock_df)

if __name__ == '__main__':
    unittest.main()

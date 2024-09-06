import unittest
import pandas as pd
from scripts.missing_values_handler import (
    missing_values_summary,
    handle_missing_numerical,
    handle_missing_categorical,
    handle_missing_text,
    handle_missing_dates,
    handle_missing_others
)

class TestMissingValuesHandler(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'numerical': [1, 2, None, 4],
            'categorical': ['a', None, 'c', 'd'],
            'text': ['foo', 'bar', None, 'baz'],
            'dates': [pd.Timestamp('2020-01-01'), None, pd.Timestamp('2020-01-03'), pd.Timestamp('2020-01-04')],
            'others': [None, 'other2', 'other3', 'other4']
        })

    def test_missing_values_summary(self):
        summary = missing_values_summary(self.df)
        expected_summary = pd.DataFrame({
            'Missing Values': [1, 1, 1, 1, 1],
            'Percentage': [25.0, 25.0, 25.0, 25.0, 25.0]
        }, index=['numerical', 'categorical', 'text', 'dates', 'others']).sort_values(by='Percentage', ascending=False)
        pd.testing.assert_frame_equal(summary, expected_summary)

    def test_handle_missing_numerical(self):
        df_filled = handle_missing_numerical(self.df.copy(), strategy='mean')
        self.assertEqual(df_filled['numerical'].isnull().sum(), 0)
        self.assertAlmostEqual(df_filled['numerical'][2], 2.3333, places=4)



    def test_handle_missing_text(self):
        df_filled = handle_missing_text(self.df.copy(), fill_value='Unknown')
        self.assertEqual(df_filled['text'].isnull().sum(), 0)
        self.assertEqual(df_filled['text'][2], 'Unknown')

   



if __name__ == '__main__':
    unittest.main()

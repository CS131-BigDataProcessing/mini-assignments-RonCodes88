import unittest
import os
import pandas as pd
from validate_functions import load_csv, validate_vict_sex, validate_vict_age
from stats_function import calculate_age_statistics

class TestCrimeData(unittest.TestCase):
    def setUp(self):
        # Ensure the test has access to the actual dataset
        self.filepath = 'Crime_Data_from_2020_to_Present.csv'
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"{self.filepath} not found in the current directory.")
        
        self.data = load_csv(self.filepath)

    def test_load_csv(self):
        """Test if CSV loads correctly."""
        self.assertIsInstance(self.data, pd.DataFrame)

    def test_validate_vict_sex(self):
        """Test validation and cleaning of 'Vict Sex' column."""
        try:
            cleaned_data = validate_vict_sex(self.data)
            # Ensure the cleaned data only contains 'M' or 'F' for 'Vict Sex' column
            self.assertTrue(all(cleaned_data['Vict Sex'].isin(['M', 'F'])))
            self.assertEqual(cleaned_data['Vict Sex'].isnull().sum(), 0)  # No missing values
        except ValueError:
            self.fail("Validation failed for 'Vict Sex'.")

    def test_validate_vict_age(self):
        """Test validation and cleaning of 'Vict Age' column."""
        try:
            cleaned_data = validate_vict_age(self.data)
            # Ensure 'Vict Age' is between 1 and 100 for all rows
            self.assertTrue(all(cleaned_data['Vict Age'].between(1, 100)))
            self.assertEqual(cleaned_data['Vict Age'].isnull().sum(), 0)  # No missing values
        except ValueError:
            self.fail("Validation failed for 'Vict Age'.")

    def test_calculate_age_statistics(self):
        """Test statistics calculation."""
        try:
            mean, median = calculate_age_statistics(self.data)
            self.assertTrue(mean > 0)
            self.assertTrue(median > 0)
        except ValueError:
            self.fail("Statistics calculation failed for 'Vict Age'.")

if __name__ == '__main__':
    unittest.main()

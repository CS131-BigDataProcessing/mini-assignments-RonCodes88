import pandas as pd

def load_csv(filepath: str) -> pd.DataFrame:
    """Load a CSV file into a Pandas DataFrame."""
    try:
        return pd.read_csv(filepath)
    except Exception as e:
        raise IOError(f"Error loading CSV file: {e}")

def calculate_age_statistics(dataframe: pd.DataFrame):
    """Calculate the mean and median of the 'Vict Age' column."""
    if 'Vict Age' not in dataframe.columns:
        raise ValueError("'Vict Age' column is missing.")
    if dataframe['Vict Age'].isnull().all():
        raise ValueError("'Vict Age' column has all NULL values.")
    mean_age = dataframe['Vict Age'].mean()
    median_age = dataframe['Vict Age'].median()
    return mean_age, median_age

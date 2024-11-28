import pandas as pd

def load_csv(filepath: str) -> pd.DataFrame:
    """Load a CSV file into a Pandas DataFrame."""
    try:
        return pd.read_csv(filepath)
    except Exception as e:
        raise IOError(f"Error loading CSV file: {e}")

def validate_vict_sex(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Validate and remove rows where 'Vict Sex' is not 'M' or 'F', or is NULL."""
    if 'Vict Sex' not in dataframe.columns:
        raise ValueError("'Vict Sex' column is missing.")
    
    # Remove rows where 'Vict Sex' is not 'M' or 'F' or is NULL
    dataframe = dataframe[dataframe['Vict Sex'].isin(['M', 'F'])]
    
    return dataframe

def validate_vict_age(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Validate and remove rows where 'Vict Age' is not between 1-100 or is NULL."""
    if 'Vict Age' not in dataframe.columns:
        raise ValueError("'Vict Age' column is missing.")
    
    # Remove rows where 'Vict Age' is not between 1 and 100 or is NULL
    dataframe = dataframe[dataframe['Vict Age'].between(1, 100)]
    
    return dataframe





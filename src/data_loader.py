# src/data_loader.py
import pandas as pd

def load_data(file_path):
    """Loads the dataset from the given path."""
    try:
        data = pd.read_csv(file_path, sep='\s+', header=None)
        print(f"✅ Loaded data from {file_path}")
        return data
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None

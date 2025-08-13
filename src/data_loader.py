# src/data_loader.py
import pandas as pd

def load_data(filepath):
    """
    Load dataset from a CSV file
    """
    return pd.read_csv(filepath)

if __name__ == "__main__":
    print("Data loader script - ready to use.")

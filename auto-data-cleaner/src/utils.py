import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def save_data(df, output_path='cleaned_data.csv'):
    df.to_csv(output_path, index=False)

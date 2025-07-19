def load_csv(file_path: str):
    import pandas as pd
    return pd.read_csv(file_path)

def format_data(df):
    # Example formatting function, can be expanded as needed
    df.columns = [col.strip().lower() for col in df.columns]
    return df

def save_csv(df, file_path: str):
    df.to_csv(file_path, index=False)
import pandas as pd
import os

def save_clean_dataset(df, path="cleaned_data/cleaned_twitter_dataset.csv"):
    os.makedirs("cleaned_data", exist_ok=True)
    df.to_csv(path, index=False)
    print(f"Saved cleaned dataset to: {path}")

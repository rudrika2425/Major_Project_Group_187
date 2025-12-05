import pandas as pd

def load_twitter_dataset(path="dataset/tweets.csv"):
    df = pd.read_csv(path, encoding="ISO-8859-1")

    # Rename columns to readable names
    df.columns = ["flag", "tweet_id", "date", "query", "username", "tweet_text"]

    # Convert date to datetime
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Drop duplicate tweets
    df = df.drop_duplicates(subset="tweet_text")

    return df

from load_dataset import load_twitter_dataset
from clean_tweets import clean_tweet_dataframe
from save_data import save_clean_dataset


def main():

    print("Loading dataset...")
    df = load_twitter_dataset()

    print("Cleaning tweets...")
    cleaned_df = clean_tweet_dataframe(df)

    print("Sorting by date...")
    cleaned_df = cleaned_df.sort_values(by="date").reset_index(drop=True)

    print("Saving...")
    save_clean_dataset(cleaned_df)

    print("Done! Clean dataset created.")


if __name__ == "__main__":
    main()

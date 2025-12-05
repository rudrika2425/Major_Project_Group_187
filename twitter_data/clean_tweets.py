import re
import string
import emoji
import pandas as pd


def strip_emoji(text):
    
    emoji_pattern = re.compile(
        "[" 
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags
        "\U00002702-\U000027B0"  # misc symbols
        "\U000024C2-\U0001F251" 
        "]+", 
        flags=re.UNICODE
    )
    return emoji_pattern.sub(r'', str(text))



def strip_all_entities(text):
    text = str(text).replace("\r", "").replace("\n", " ").lower()

    # remove @mentions + URLs
    text = re.sub(r"(?:@|https?://)\S+", "", text)

    # remove non-ASCII characters
    text = re.sub(r"[^\x00-\x7f]", "", text)

    # remove punctuation
    banned = string.punctuation + "Ã±ã¼â»§"
    table = str.maketrans("", "", banned)
    text = text.translate(table)

    return text


def clean_hashtags(tweet):
    # remove hashtags only at end
    t = " ".join(
        word.strip() for word in re.split(
            r"#(?!(?:hashtag)\b)[\w-]+(?=(?:\s+#[\w-]+)*\s*$)", tweet
        )
    )
    t2 = " ".join(word.strip() for word in re.split(r"#|_", t))
    return t2


def filter_chars(text):
    words = []
    for w in text.split(" "):
        if "$" in w or "&" in w:
            continue
        words.append(w)
    return " ".join(words)


def remove_mult_spaces(text):
    return re.sub(r"\s\s+", " ", text).strip()



def clean_tweet_dataframe(df: pd.DataFrame):

    clean_texts = []
    for t in df["tweet_text"]:
        t1 = strip_emoji(t)
        t2 = strip_all_entities(t1)
        t3 = clean_hashtags(t2)
        t4 = filter_chars(t3)
        t5 = remove_mult_spaces(t4)
        clean_texts.append(t5)

    df["clean_text"] = clean_texts
    df["text_len"] = df["clean_text"].apply(lambda x: len(x.split()))

    # Remove tweets with < 5 words
    df = df[df["text_len"] > 4]

    return df

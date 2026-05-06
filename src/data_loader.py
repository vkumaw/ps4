import pandas as pd


def load_content_data():
    return pd.read_csv("data/raw/content.csv")


def load_platform_activity():
    return pd.read_csv("data/raw/platform_activity.csv")


def load_historical_engagement():
    return pd.read_csv("data/raw/historical_engagement.csv")


def load_creators():
    return pd.read_csv("data/raw/creators.csv")


def build_activity_lookup(activity_df):

    lookup = {}

    for _, row in activity_df.iterrows():

        key = (row["platform"], row["time_slot"])

        lookup[key] = row["activity_score"]

    return lookup


def build_history_lookup(history_df):

    lookup = {}

    for _, row in history_df.iterrows():

        key = (
            row["creator_id"],
            row["platform"],
            row["content_type"],
            row["time_slot"]
        )

        lookup[key] = row["avg_engagement"]

    return lookup


if __name__ == "__main__":

    content = load_content_data()

    print(content.head())
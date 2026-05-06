import pandas as pd

from src.data_loader import (
    load_content_data,
    load_platform_activity,
    load_historical_engagement,
    load_creators,
    build_activity_lookup,
    build_history_lookup
)

from src.recommender import generate_recommendation


# -------------------------
# Load datasets
# -------------------------

content_df = load_content_data()

activity_df = load_platform_activity()

history_df = load_historical_engagement()

creators_df = load_creators()


# -------------------------
# Build lookup dictionaries
# -------------------------

activity_lookup = build_activity_lookup(activity_df)

history_lookup = build_history_lookup(history_df)

creator_lookup = dict(
    zip(
        creators_df["creator_id"],
        creators_df["base_engagement"]
    )
)


# -------------------------
# Generate recommendations
# -------------------------

results = []

for _, row in content_df.iterrows():

    content_row = row.to_dict()

    recommendation = generate_recommendation(
        content_row,
        activity_lookup,
        history_lookup,
        creator_lookup
    )

    results.append(recommendation)


# -------------------------
# Save submission
# -------------------------

submission_df = pd.DataFrame(results)

submission_df.to_csv(
    "output/submission.csv",
    index=False
)

print("✅ submission.csv generated successfully")
from fastapi import FastAPI

from src.data_loader import (
    load_content_data,
    load_platform_activity,
    load_historical_engagement,
    load_creators,
    build_activity_lookup,
    build_history_lookup
)

from src.recommender import generate_recommendation

app = FastAPI()

# -------------------------
# Load datasets once
# -------------------------

content_df = load_content_data()

activity_df = load_platform_activity()

history_df = load_historical_engagement()

creators_df = load_creators()

# -------------------------
# Build fast lookups
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
# Home route
# -------------------------

@app.get("/")
def home():

    return {
        "message":
        "Creator Content Optimization System Running"
    }

# -------------------------
# Recommendation route
# -------------------------

@app.get("/get_recommendation/{content_id}")
def get_recommendation(content_id: int):

    content_row = content_df[
        content_df["content_id"] == content_id
    ]

    if content_row.empty:

        return {
            "error": "Content ID not found"
        }

    content_row = content_row.iloc[0].to_dict()

    result = generate_recommendation(
        content_row,
        activity_lookup,
        history_lookup,
        creator_lookup
    )

    return result
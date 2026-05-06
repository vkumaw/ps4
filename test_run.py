from src.recommender import generate_recommendation

# Dummy content item
content_row = {
    "content_id": 1,
    "creator_id": 101,
    "content_type": "SHORT",
    "created_timestamp": 18
}

# Dummy platform activity
activity_lookup = {
    ("Instagram", 18): 1.0,
    ("Instagram", 19): 1.1,
    ("YouTube", 18): 0.7,
    ("YouTube", 19): 0.8
}

# Dummy historical engagement
history_lookup = {
    (101, "Instagram", "SHORT", 18): 1.2,
    (101, "Instagram", "SHORT", 19): 1.3,
    (101, "YouTube", "SHORT", 18): 0.6,
    (101, "YouTube", "SHORT", 19): 0.7
}

# Dummy creator base
creator_lookup = {
    101: 1.1
}

result = generate_recommendation(
    content_row,
    activity_lookup,
    history_lookup,
    creator_lookup
)

print(result)
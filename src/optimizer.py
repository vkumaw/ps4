def calculate_score(
    activity_score,
    historical_engagement,
    creator_base,
    platform,
    content_type
):
    """
    Core optimization scoring function
    """

    # Base score
    score = (
        activity_score *
        historical_engagement *
        creator_base
    )

    # Soft platform preference
    if (
        content_type == "SHORT" and
        platform == "Instagram"
    ):
        score *= 1.05

    elif (
        content_type == "LONG" and
        platform == "YouTube"
    ):
        score *= 1.05

    return round(score, 6)
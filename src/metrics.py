import time


def calculate_metrics(
    submission,
    content_lookup,
    activity_lookup,
    history_lookup,
    creator_lookup,
    latency
):
    """
    Calculate evaluation metrics
    """

    n = len(submission)

    engagement_total = 0
    timing_total = 0
    platform_total = 0

    for row in submission:

        content_id = row["content_id"]

        content_data = content_lookup[content_id]

        creator_id = content_data["creator_id"]
        content_type = content_data["content_type"]

        platform = row["platform"]
        time_slot = row["time_slot"]

        activity = activity_lookup.get(
            (platform, time_slot),
            0.5
        )

        history = history_lookup.get(
            (
                creator_id,
                platform,
                content_type,
                time_slot
            ),
            0.5
        )

        creator_base = creator_lookup.get(
            creator_id,
            1.0
        )

        engagement = (
            activity *
            history *
            creator_base
        )

        engagement_total += engagement

        timing_total += activity

        # Platform quality
        if (
            content_type == "SHORT" and
            platform == "Instagram"
        ):
            platform_total += 1.0

        elif (
            content_type == "LONG" and
            platform == "YouTube"
        ):
            platform_total += 1.0

        else:
            platform_total += 0.8

    engagement_score = (
        min((engagement_total / n), 1.5) / 1.5
    )

    timing_score = timing_total / n

    platform_score = platform_total / n

    efficiency_score = max(0, 1 - latency)

    final_score = (
        0.50 * engagement_score +
        0.20 * timing_score +
        0.15 * platform_score +
        0.15 * efficiency_score
    )

    return {
        "engagement_score": round(engagement_score, 4),
        "timing_score": round(timing_score, 4),
        "platform_score": round(platform_score, 4),
        "efficiency_score": round(efficiency_score, 4),
        "final_score": round(final_score, 4)
    }
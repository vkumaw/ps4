from optimizer import calculate_score
from scheduler import scheduling_decision


PLATFORMS = ["Instagram", "YouTube"]


def generate_recommendation(
    content_row,
    activity_lookup,
    history_lookup,
    creator_lookup
):
    """
    Generate best recommendation
    for a single content item
    """

    creator_id = content_row["creator_id"]
    content_type = content_row["content_type"]
    current_hour = content_row["created_timestamp"]

    creator_base = creator_lookup.get(
        creator_id,
        1.0
    )

    best_result = None
    best_score = -1

    for platform in PLATFORMS:

        for hour in range(24):

            activity_score = activity_lookup.get(
                (platform, hour),
                0.5
            )

            historical_engagement = history_lookup.get(
                (
                    creator_id,
                    platform,
                    content_type,
                    hour
                ),
                0.5
            )

            score = calculate_score(
                activity_score,
                historical_engagement,
                creator_base,
                platform,
                content_type
            )

            # Deterministic tie-breaking
            if (
                score > best_score
            ):

                best_score = score

                best_result = {
                    "platform": platform,
                    "time_slot": hour,
                    "score": score,
                    "activity_score": activity_score
                }

            elif score == best_score:

                # Tie breaker 1
                if (
                    activity_score >
                    best_result["activity_score"]
                ):

                    best_result = {
                        "platform": platform,
                        "time_slot": hour,
                        "score": score,
                        "activity_score": activity_score
                    }

                # Tie breaker 2
                elif (
                    activity_score ==
                    best_result["activity_score"]
                ):

                    if platform == "Instagram":

                        best_result = {
                            "platform": platform,
                            "time_slot": hour,
                            "score": score,
                            "activity_score": activity_score
                        }

    decision = scheduling_decision(
        current_hour,
        best_result["time_slot"]
    )

    return {
        "content_id": content_row["content_id"],
        "platform": best_result["platform"],
        "time_slot": best_result["time_slot"],
        "decision": decision
    }
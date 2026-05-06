def scheduling_decision(current_hour, recommended_hour):
    """
    Decide whether to post now
    or schedule for later
    """

    difference = abs(recommended_hour - current_hour)

    if difference <= 1:
        return "POST_NOW"

    return "SCHEDULE"
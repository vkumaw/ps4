from src.optimizer import calculate_score
from src.scheduler import scheduling_decision


def test_score_positive():

    score = calculate_score(
        1.0,
        1.0,
        1.0,
        "Instagram",
        "SHORT"
    )

    assert score > 0


def test_scheduler_now():

    result = scheduling_decision(18, 19)

    assert result == "POST_NOW"


def test_scheduler_future():

    result = scheduling_decision(10, 20)

    assert result == "SCHEDULE"


def test_long_content_bias():

    score = calculate_score(
        1.0,
        1.0,
        1.0,
        "YouTube",
        "LONG"
    )

    assert score > 1.0
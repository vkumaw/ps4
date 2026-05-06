from src.optimizer import calculate_score


def test_score_positive():

    score = calculate_score(
        1.0,
        1.0,
        1.0,
        "Instagram",
        "SHORT"
    )

    assert score > 0
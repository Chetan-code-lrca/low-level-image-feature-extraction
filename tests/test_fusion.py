from src.fusion.feature_fusion import combine_features


def test_feature_combination():
    colour = [10, 20, 30]
    texture = [40, 50, 60]
    shape = [70, 80]

    combined = combine_features(
        colour,
        texture,
        shape
    )

    assert len(combined) == 8
    assert combined[0] == 10
    assert combined[-1] == 80
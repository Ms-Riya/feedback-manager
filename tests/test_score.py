from score_calculator import calculate_average

def test_normal_average():
    assert calculate_average([4.0, 4.0]) == 4.0

def test_empty_list():
    assert calculate_average([]) == 0.0

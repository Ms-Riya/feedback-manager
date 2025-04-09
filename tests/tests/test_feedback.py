from unittest.mock import patch
from feedback_entry import collect_feedback

def test_feedback_collection():
    with patch('builtins.input', side_effect=['Alice', 'Great course!', '4.5']):
        feedback = collect_feedback()
        assert feedback['name'] == 'Alice'
        assert feedback['rating'] == 4.5

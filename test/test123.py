from unittest.mock import patch
from controller.Controller import get_all

@patch('service.Service.xyz.post_questions_model')
def test(mock_test):
    get_all()
    print("test")

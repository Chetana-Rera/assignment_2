from unittest.mock import patch

from controller.Controller import get_all



@patch('service.Service.xyz.post_questions_model')
def test_get_by_id(service_mock):
    # service_mock.return_value = 'message'
    response = get_all()
    assert response == 'message'
    # assert response == {"data['ResponseMetadata']['HTTPStatusCode'] == 200"}

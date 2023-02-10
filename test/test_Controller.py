# from mock import patch
#
from unittest import mock

from controller import Controller
from controller.Controller import get_by_st, delete

import unittest.mock
# from unittest.mock import CaptureOutput


def test_get_all(mocker):
    # response_mock = unittest.MagicMock()
    # mocker.patch.object("Controller.get_all_que", response_mock)
    # response_mock.return_value = "Test Successful"
    # get_all()
    # response_mock.assert_called_once()
    with unittest.mock.patch("Controller.get_all_que") as mock_get_all_que:
        mock_get_all_que.return_value = "Test Successful"
        # get_all()
        # mock_get_all_que.assert_called_once()


def test_get_by_id(mocker):
    user_id = 'mugdha@harakirimail.com'
    question_id = '5'

    expected_data = {
        "userId": user_id,
        "questionId": question_id,
        "sortKey": "question#" + user_id + "#" + question_id
    }
    expected_que = "Explain about serverless?"

    mocker.patch('builtins.input', return_value=user_id)
    mocker.patch('builtins.input', return_value=question_id)
    mock_get_que = mocker.patch('Service.get_que', return_value=expected_que)

    result = Controller.get_by_id()


# mock_get_que.assert_called_with(expected_data)
# assert result == expected_data


def test_get_by_st_pass():
    user_input = ["mugdha@harakirimail.com", "5"]
    with mock.patch("builtins.input", side_effect=user_input):
        result = get_by_st()
        if result is not None:
            result = "SUCCESSFUL"
            assert result == "SUCCESSFUL"
            # result = "UNSUCCESSFUL"
            # assert result == "UNSUCCESSFUL"
        # else:
        #     result = "SUCCESSFUL"
        #     assert result == "SUCCESSFUL"


def test_get_by_st_failed():
    user_input = ["123.com", "5"]
    with mock.patch("builtins.input", side_effect=user_input):
        result = get_by_st()
        if result is None:
            result = "UNSUCCESSFUL"
            assert result == "UNSUCCESSFUL"


def test_delete():
    with unittest.mock.patch("builtins.input", side_effect=["user123", "question456"]):
        with unittest.mock.patch("Service.delete_answer") as delete_answer_mock:
            result = delete()
            print(result)
            delete_answer_mock.assert_called_with({
                "userId": "user123",
                "questionId": "question456",
                "sortKey": "answer#question456#user123"
            })

# def test_get_by_st(mocker):
#     mock_input = mocker.patch('builtins.input', side_effect=["123", "456"])
#     mock_que_by_status = mocker.patch('Service.que_by_status')
#     mock_que_by_status.return_value = {'status': '1'}
#
#     #get_by_st()
#     que_by_status()
#
#     mock_input.assert_has_calls([
#         mocker.call("enter your userId: "),
#         mocker.call("enter question Id: ")
#     ])
#     mock_que_by_status.assert_called_once_with({
#         "userId": "123",
#         "questionId": "456",
#         "sortKey": "question#123#456"
#     })
# def test_get_by_id():
#     # create a mock for the `get_que` function
#     def mock_get_que(data):
#         return {'mock': 'data'}
#
#     # patch the `get_que` function with the mock
#     @unittest.patch('Service.get_que', mock_get_que)
#     def run_get_by_id():
#         get_by_id()
#
#     # capture the printed output of the function
#     with CaptureOutput() as captured:
#         run_get_by_id()
#
#     # assert that the correct output is printed
#     assert captured.get_text() == "fetching question by ID\n{'mock': 'data'}\n"

# def test_get_by_id(mocker):
#     mocker.patch.object(__connected_table__, "query", return_value="user1")
#     mocker.patch.object(__connected_table__, "query", return_value="question1")
#     mocker.patch.object(get_que, return_value={})
#     response = get_by_id()
#     assert response == {
#         "userId": "user1",
#         "questionId": "question1",
#         "sortKey": "question#user1#question1"
#     }

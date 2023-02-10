from unittest.mock import MagicMock, patch

from _pytest import unittest
from controller.Controller import get_by_id, get_all


def test_get_by_id():
    # Create a mock response object to replace the actual response from the service function
    mock_response = MagicMock
    mock_response.status_code = 200
    mock_response.data = b'Fetching questions successfully'

    # Patch the get_que function in the service class to return the mock response
    with patch('Service.get_que', return_value=mock_response):

        # Call the get_by_id function
        response = get_by_id()

        # Verify the expected response from the get_by_id function
        assert response.status_code == 200
        assert response.data == b'Fetching questions successfully'


# class TestGetById(unittest.TestCase):
#     @patch("__main__.get_que")
#     def test_get_by_id(self, mock_get_que):
#         expected_data = {'userId': 'mugdha@harakirimail.com', 'questionId': '5', 'sortKey': 'question#mugdha@harakirimail.com#5'}
#         expected_response = {'questionId': '5', 'sortKey': 'question#mugdha@harakirimail.com#5', 'userId': 'mugdha@harakirimail.com'}
#         mock_get_que.return_value = expected_response
#         response = get_by_id()
# #         self.assertEqual(response, expected_response)
# #         mock_get_que.assert_called_with(expected_data)
#
# def test_get_by_id_with_valid_input():
#     # Arrange
#     user_id = "123"
#     question_id = "456"
#     expected_response = {
#         "userId": user_id,
#         "questionId": question_id,
#         "sortKey": "question#123#456"
#     }
#
#     # Act
#     response = get_by_id()
#
#     # Assert
#     assert response == expected_response

class TestGetAll(unittest.TestCase):
    @patch('controller.get_all_que')
    def test_get_all(self, mock_get_all_que):
        # Arrange
        mock_get_all_que.return_value.status_code = 200

        # Act
        response = get_all()

        # Assert
        self.assertEqual(response.status_code, 200)











# from datetime import datetime
# from unittest import mock
# from unittest.mock import MagicMock, patch
#
# import pytest
# from flask import Response
# from pytest_mock import mocker
#
# import Controller
# import unittest
# from Controller import get_all
# from Service import get_all_que
# import unittest.mock
#
#
# @pytest.mark.parametrize("user_id, question_id, expected_response" ,[
#     ("123", "456", {"userId": "123", "questionId": "456", "sortKey": "question#123#456"}),
#    ])
# expected_response = Response("Bad Request", status=400)
# def test_get_by_id(user_id, question_id, expected_response):
#     with patch("builtins.input", side_effect=[user_id, question_id]):
#         with patch("Service.get_que", return_value=expected_response):
#             response = Controller.get_by_id()
#             assert response == expected_response

# def test_getall_calls_getallque():
#     # from Controller import get_all
#     mock_get_all_que = MagicMock()
#     mocker.patch.object(mock_get_all_que)
#     with unittest.mock.patch('Service.get_all_que') as mock_get_all_que:
#         get_all()
#         # Assert that the getallque function was called
#         assert mock_get_all_que.called

# def test_get_all(mocker):
#     response = {'ResponseMetadata': {'HTTPStatusCode': 200}}
#     get_all_mock = MagicMock()
#     get_all_mock.return_value = response
#     mocker.patch.object(Controller.get_all, get_all_mock)
#
#     result = Controller.get_all()
#
#     assert result.status_code == 200, "Unexpected status code"
#     #assert result.data == b'Successfully deleted', "Unexpected response data"

# def test_get_all():
#     def mock_get_all_que():
#         return Response(status=200)
#
#     # Replace the `get_all_que` function with the mock function
#     Controller.get_all.get_all_que = mock_get_all_que
#
#     # Call the `get_all` function
#     result = Controller.get_all()
#
#     # Assert the result of the function
#     assert result == Response(status=200)

# def test_get_all(mocker):
#     mock_get_all = MagicMock()
#     mocker.patch.object(mock_get_all)
#     mock_get_all.return_value = {'Items': {}}
#     response = get_all()
#     assert response.status_code == 404

# def test_get_all():
#
#     expected = [{'question': 'What is your name?'},
#                 {'question': 'How are you?'},
#                 {'question': 'What is Serverless'}]
#
#     def mock_get_all_que():
#         return expected
#
#     get_all.get_all_que = mock_get_all_que
#     result = get_all()
#     assert result == expected

# def test_get_all_output():
#     # Call the get_all function
#     Controller.get_all()
#
#     # Verify if the print statement was called with the correct message
#     with patch('builtins.print') as mock_print:
#         Controller.get_all()
#         mock_print.assert_called_with("SUCCESSFUL")


# def test_get_all_return_value():
#     def mock_get_all_que():
#         mock_response = mock.Mock()
#         mock_response.json = None
#         return mock_response
#
#     Controller.get_all.get_all_que = mock_get_all_que
#
#     result = Controller.get_all()
#
#     assert result.json is None


# def test_get_by_st():
#     # Test with valid input
#     user_input = [("123", "456"), ("789", "101112")]
#     expected_output = [
#         {"userId": "123", "questionId": "456", "sortKey": "question#123#456"},
#         {"userId": "789", "questionId": "101112", "sortKey": "question#789#101112"},
#     ]
#
#     for i, inp in enumerate(user_input):
#         with mock.patch("builtins.input", side_effect=inp):
#             response = Controller.get_by_st()
#             assert response is not None, "Function que_by_status is returning None."
#             assert response == expected_output[i]


# def test_delete():
#     test_cases = [
#         {
#             "userId": "user1",
#             "questionId": "question1",
#             "expected_sortKey": "answer#question1#user1"
#         },
#         {
#             "userId": "user2",
#             "questionId": "question2",
#             "expected_sortKey": "answer#question2#user2"
#         },
#     ]
#
#     @pytest.mark.parametrize("userId, questionId, expected_sortKey", test_cases)
#     def delete_test_cases(userId, questionId, expected_sortKey):
#         data = Controller.delete(userId, questionId)
#         assert data['sortKey'] == expected_sortKey
#
#
# class TestUpdate(unittest.TestCase):
#     def test_update(self):
#         # Test case data
#         # test_cases = [
#         #     # Test case 1
#         #     {
#         #         "userId": "user1",
#         #         "questionId": "question1",
#         #         "edited_que": "Edited question 1",
#         #         "expected_sortKey": "question#user1#question1",
#         #         "expected_edited_que": "Edited question 1"
#         #     },
#         # Add more test cases as needed
#           # ]
#         data = {
#                 "userId": "user2",
#                 "questionId": "question2",
#                 "edited_que": "Edited question 2",
#                 "expected_sortKey": "question#user2#question2",
#                 "expected_edited_que": "Edited question 2"
#             },
#
#         def mock_test_update(data):
#             return "Successfully updated"
#
#         ans = mock_test_update(data)
#         self.assertEqual(ans, "Successfully updated")
#         self.assertEqual(data, {
#             "userId": data.userId,
#             "questionId": data.questionId,
#             "sortKey": data.sortKey,
#             "createdAt": data.createdAt,
#             "answer": data.answer
#         })

# for test_case in test_cases:
#     with self.subTest(test_case=test_case):
#         userId = test_case['userId']
#         questionId = test_case['questionId']
#         edited_que = test_case['edited_que']
#         expected_sortKey = test_case['expected_sortKey']
#         expected_edited_que = test_case['expected_edited_que']
#
#         ans = Controller.update(userId, questionId, edited_que)
#
#         self.assertEqual(ans['sortKey'], expected_sortKey)
#         self.assertEqual(ans['edited_que'], expected_edited_que)


# class TestPut(unittest.TestCase):
#     def test_put(self):
#         answer = "This is a sample answer"
#         userId = "12345"
#         questionId = "67890"
#         sortKey = "answer#67890#12345"
#         createdAt = str(datetime.now().date())
#         data = {
#             "userId": userId,
#             "questionId": questionId,
#             "sortKey": sortKey,
#             "createdAt": createdAt,
#             "answer": answer
#         }
#
#         def mock_put_answer(data):
#             return "Successfully added answer to database"
#
#         ans = mock_put_answer(data)
#         self.assertEqual(ans, "Successfully added answer to database")
#         self.assertEqual(data, {
#             "userId": userId,
#             "questionId": questionId,
#             "sortKey": sortKey,
#             "createdAt": createdAt,
#             "answer": answer
#         })

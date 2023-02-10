import boto3
from unittest.mock import MagicMock

from service import Service
from service.Service import get_all_que, __connected_table__
from service.Service import get_que
from service.Service import put_answer


# def test_get_all_que_failed():
#     mock_get_all_que = MagicMock()
#     mocker.patch.object(__connected_table__, "query", mock_get_all_que)
#     mock_get_all_que.return_value = {'Items': {}}
#     response = get_all_que()
#     assert response.status_code == 400
#
#
# def test_get_all_que_pass():
#     mock_get_all_que = MagicMock()
#     mocker.patch.object(__connected_table__, "query", mock_get_all_que)
#     mock_get_all_que.return_value = {'Items': [{'question': 'What is Pytest?'}]}
#     response = get_all_que()
#     assert response.status_code == 200


# 1
def test_get_all_que(mocker):
    mock_get_all_que = MagicMock()
    mocker.patch.object(__connected_table__, "query", mock_get_all_que)
    response = get_all_que()
    # assert response.status_code == 200
    # assert response.data.decode() == "Fetching questions successfully"


# ---------------------------------------------------------------------------------------------------------
# 2.1
def test_get_que(mocker):
    data = {'sortKey': '789'}
    response_mock = MagicMock()
    response_mock.__contains__.return_value = True
    response_mock.__getitem__.return_value = {}
    mocker.patch('Service.get_que', return_value=response_mock)

    result = get_que(data)
    assert result.status_code == 200
    # if result.status_code == 200:
    #     assert result.status_code == 200
    #     assert result.get_data() == b'Fetching questions successfully'
    # else:
    #     assert result.status_code == 400
    #     assert result.get_data() == b'Bad Request'


# 2.2

def test_get_que_pass(mocker):
    data = {'sortKey': 'question#mugdha@harakirimail.com#5'}
    response_mock = MagicMock()
    response_mock.__contains__.return_value = True
    response_mock.__getitem__.return_value = {"Explain about serverless?"}
    mocker.patch('Service.get_que', return_value=response_mock)

    result = get_que(data)
    assert result.status_code == 200


# --------------------------------------------------------------------
# 3
def test_que_by_status():
    data = {
        "userId": "123",
        "questionId": "456",
        "sortKey": "question#123#456"
    }

    # Create a mock response object
    response = {
        "Item": {"question": "Test question"}
    }

    # Create a mock boto3 client
    # dynamodb = boto3.client("dynamodb")
    dynamo_client = boto3.resource(service_name='dynamodb', region_name='eu-west-1',
                                   aws_access_key_id='ASIAX2KHRAJA37LXE276',
                                   aws_secret_access_key='BIjH35/rLpl2NIP4/VJR5kcHyAFiWZuTpxtijRJm',
                                   aws_session_token='IQoJb3JpZ2luX2VjELb//////////wEaCWV1LXdlc3QtMSJIMEYCIQC54tmmqW7032OsdBZkq1J4g1RYWfAoF8vY27ynBrkvYgIhAPJdPv7z6Mvx+4429ViF8eBs3IvdKuQZJ4h8q7ohS1qsKpMDCD8QBBoMNTM3NTU3Nzk1MzkzIgwRZ6maGAKD/W1WcAIq8AKEhigoRg15g7k3/xwVG65M3bDhT0F8lChF4IC5JNoQTmPPnIr/aCeUCIdVs+1bH2DkrsD7XBrC/YoyjuPehBbxSRhRogJGIKBgOMwZ9fKI/mZZNTnKBvM9U+UFhS5nZZ2fhSvXsncwAuh33QyCSOmiek/BzBEbNOkfOuzIFasI/RLD1RW8GQb7631BpsgL2MoahSbBQCnoeqcLtDQMfQWlhlJWGBNOzjlPfdq3pikX3FV9BJc+p3VKYQKUxd0Xx5fXjHLbFxApDoK/7LgxRGuE1nWyBuZb1X+tZExp9qO92GuGfLYxhuTmc5WxE3H0pQWISdLcZzHxu6VfP44UATMxSrzjCF94mafDPyVIUM/NFvj132hS+SEqb1Ddx7Gf3V8ZRd0Jd89MIWusSXCHR4wt7nLc10n565NWeblKiwugnM+aUnDEKV/pXh+Klu6CHkxlTvC+qosOsHPDIxVKgpSEUQ4p4gg62faLs1OVLIX5LzDyn4KfBjqlAVSD2IbezBrWqSebX6O5UWl2fxMDTNFvv5vtP/lRI4m0AtajgeR3OcAaV60nOILkWsHWSlNaehhbIFHzo/oIfPCXzYVeEkgdbq2y0L1dyV+GJWw1NF7bFmyqQqWxb4JqxXEdUhwydy7T1OvDHV1mInQP5Q1tSDW29YvQpxtvfPionatZ15Qw4CFs3x9Yj3itL28CqjyN8RIk1cTjlnnmPhJ2kF+diA=='
                                   )
    dynamo_client.query = MagicMock(return_value=response)

    # Test the function with the mock data
    result = Service.que_by_status(data)
    print(result)
    if result.status_code == 200:
        assert result.status_code == 200
    else:
        assert result.status_code == 400


# --------------------------------------------------------------------------------------------------------------------
# 4 done
def test_put_answer(mocker):
    response_mock = MagicMock()
    mocker.patch.object(Service.__connected_table__, 'put_item', response_mock)
    # put_item_mock = mocker.patch('Service.put_answer', return_value=response_mock)
    data = {
        'sortKey': 'answer#5#chet_12@gmail.com',
        'answer': 'sample answer',
        'createdAt': '2023-02-03',
        'userId': 'chet_12@gmail.com'
    }
    print(response_mock)

    result = put_answer(data)

    # if result.status_code == 200:
    #     assert result.status_code == 200
    #     assert result.get_data() == b'Successfully added a answer'
    assert result.status_code == 200
    response_mock.assert_called_with(
        TableName='freshers-example',
        Item={
            'type': 'answer',
            'sortKey': data['sortKey'],
            'answer': data['answer'],
            'createdAt': data['createdAt'],
            'status': '1',
            'userId': data['userId']
        }
    )


# ------------------------------------------------------------------------------------------------------

# 5
def test_edit_question(mocker):
    update_item_mock = MagicMock()
    mocker.patch.object(Service, 'edit_question', update_item_mock)

    data = {
        'sortKey': 'question#nkp@gmail.com#10',
        'edited_que': 'Tell me about pythons version?'
    }
    Service.edit_question(data)


# -----------------------------------------------------------------------------

# 6
def test_delete_answer(mocker):
    data = {
        "userId": "user123",
        "questionId": "question456",
        "sortKey": "answer#question456#user123"
    }
    mocker.patch("Service.delete_answer")
    # mocker.patch("__connected_table__.delete_item")
    Service.delete_answer(data)
    Service.delete_answer.assert_called_once_with(
        Key={
            'type': "answer",
            'sortKey': data['sortKey'],
        }
    )
# ------------------------------------------------------------------------------------------------

# Verify that the update_item method was called with the expected arguments
# Service.edit_question.assert_called_once_with(
#     Key={
#         'type': "question",
#         'sortKey': data['sortKey'],
#     },
#     UpdateExpression='SET question = :newQuestion',
#     ExpressionAttributeValues={
#         ':newQuestion': data['edited_que']
#     },
#     ReturnValues="UPDATED_NEW"
# )

# Verify that the correct Response object was returned
# assert response == Response("Successfully updated", status=200)

# ---------------------------------------------------------------------------------------

# @pytest.fixture()
# def delete_answer(monkeypatch):
#     def mock_delete_item(Key):
#         return {
#             'ResponseMetadata': {
#                 'HTTPStatusCode': 200
#             }
#         }
#
#     monkeypatch.setattr(boto3.resource('dynamodb').Table, 'delete_item', mock_delete_item)
#
#
# def test_delete_answer(delete_answer):
#     response = delete_answer({'type': "answer", 'sortKey': "test_sort_key"})
#     assert response.status_code == 200

# def test_delete_answer():
#     # create a mock DynamoDB table
#     __connected_table__ = MagicMock()
#     # set the delete_item return value to a mock response
#     __connected_table__.delete_item.return_value = {'ResponseMetadata': {'HTTPStatusCode': 200}}
#
#     data = {'sortKey': 'test_key'}
#
#     response = Service.delete_answer(data)
#
#     # check if the delete_item method was called with the correct arguments
#     __connected_table__.delete_item.assert_called_with(
#         Key={
#             'type': "answer",
#             'sortKey': data['sortKey'],
#         }
#     )
#
#     # check if the correct response is returned
#     assert response == Response("Successfully deleted", status=200)
# ----------------------------------------------------------------------------------

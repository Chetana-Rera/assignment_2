# from unittest.mock import MagicMock
#
# from boto3.dynamodb.conditions import Key, Attr
#
# import Service

#done
# def test_put_answer(mocker):
#     response_mock = MagicMock()
#     mocker.patch.object(Service.__connected_table__, 'put_item', response_mock)
#     # put_item_mock = mocker.patch('Service.put_answer', return_value=response_mock)
#     data = {
#         'sortKey': 'answer#5#chet_12@gmail.com',
#         'answer': 'sample answer',
#         'createdAt': '2023-02-03',
#         'userId': 'chet_12@gmail.com'
#     }
#     print(response_mock)
#
#     result = put_answer(data)
#
#     # if result.status_code == 200:
#     #     assert result.status_code == 200
#     #     assert result.get_data() == b'Successfully added a answer'
#     assert result.status_code == 200
#     response_mock.assert_called_with(
#         TableName='freshers-example',
#         Item={
#             'type': 'answer',
#             'sortKey': data['sortKey'],
#             'answer': data['answer'],
#             'createdAt': data['createdAt'],
#             'status': '1',
#             'userId': data['userId']
#         }
#     )





























# # from Service import table
# from unittest.mock import Mock
# from xmlrpc.client import boolean
#
# import boto3
# import pytest
# from mock import patch
# from moto.s3 import mock_s3
#
# import Service
# from Service import table, __connected_table__
# import store
#
#
# # from moto import mock_dynamodb2
#
#
# def test_my_fun(mocker):
#     # dynamodb = mocker.Mock()
#     # table3 = mocker.Mock()
#     # dynamodb.Table.return_value = table3
#
#     item = {'type': 'answer',
#             'sortKey': 'answer#5#priyanka.juwar@arrkgroup.com',
#             'answer': 'AWS Lambda is a compute service that lets you run code without provisioning or managing servers.',
#             'createdAt': '2022-11-01',
#             'status': 1,
#             'userId': 'priyanka.juwar@arrkgroup.com'
#             }

   # mocker.patch.object(boto3, "resource", return_value=dynamodb)
   #  result = Service.put_answer(item)
#     print(result)
#     #assert not result == True
# =-------------------------------------------------------------------------------------------------------------------------------------------------
# @mock_s3
# def test_get_all():
#     dynamo_client = boto3.resource(service_name='dynamodb', region_name='eu-west-1',
#                                    aws_access_key_id='ASIAX2KHRAJASYMIX6TU',
#                                    aws_secret_access_key='9kVInepOijQ10Iyz7BxQtaXfSgdJJZFN18ECVhSU',
#                                    aws_session_token='IQoJb3JpZ2luX2VjEG0aCWV1LXdlc3QtMSJGMEQCIDZ4miJz1fYhE6hJZtGF+up2xnVcsZcLfXphlFbtxf6VAiBgUFHv8EK3MMRLUqgA412GbwWQuJDs6Q8S1xoDV7Bh4SqcAwjm//////////8BEAMaDDUzNzU1Nzc5NTM5MyIMhuIKHhSS49qMVyN7KvAC4BWWEZvucMWcXzZucNvE4YQf4Ha+Sbh0cZIjtDB+vPjQnLPPdGs2+2/J2we5xprq1yK0RtfX9KGHBb6expEc6KdmiIvIaNCxgFVyEJBdPQN4k9RJZ8UyE0d8BaC/GXMmgS3rGTpAlgr+EtfGGYSDUn8SuY0+crl1UaUTKU78b6a1OhFILilfkwW7FIXotkxblSP4zm14/StjRjGnt8tOQ+YU1H1ZkWR0L+/O+kkE+R+NkwoNPpEEMh+tyTpNclPqa4l0ZTNnwa7b+Uuw6YgtK6dwlkz85740p1fdynXTouOCpfAujniiJG00VcFIj69N+lWamrhGx9dvJPW0TQ6K9gt9lbmvox974MKEN+t5aAFq3aZEg0RuxoLcZ/KbzuFSWVYS+FL49nMgfq08dHfOiyd4lQwYCRcpHKmmj1DwOhtqJzgoE7b1NZX1W+4fJbKYBW2RqDwZlIGiKYfIiFcxcOTxcyMS0OY8yeI1zpKUh+8w9KryngY6pwGnWyY31/pSYn2J0hp5DvH8QSAP3GR2zdrZBcowtje4oYN5uFWOaJIa6iV0N+5g+j8Z/P9nJQp3lSxIO674ovIqQlTxS/2atw29t4oiPTu+6oYWkPuNz7sa30WnpiskETZxwZcNS89DccSagq5eVP1FXy3ZqZlUQ283speokUUTDvRVQEsF7wu+v44VEMKPb86V10BvZlFHJsQesc/zWMM/Qh0wEMHWvA==')
#     dynamo_client = boto3.resource("dynamodb", region_name="eu-west-1")
#     table_name = 'test'
#     table1 = dynamo_client.create_table(TableName=table_name,
#                                         KeySchema=[
#                                             {'AttributeName': 'type', 'KeyType': 'HASH'},
#                                             {"AttributeName": "sortKey", "KeyType": "RANGE"}],
#
#                                         AttributeDefinitions=[
#                                             {'AttributeName': 'type', 'AttributeType': 'S'},
#                                             {"AttributeName": "sortKey", "AttributeType": "S"},
#                                             {"AttributeName": "userID", "AttributeType": "S"}]
#
#                                         )
#     data = {'type': 'answer',
#             'sortKey': 'answer#5#priyanka.juwar@arrkgroup.com',
#             'answer': 'AWS Lambda is a compute service that lets you run code without provisioning or managing servers.',
#             'createdAt': '2022-11-01',
#             'status': 1,
#             'userId': 'priyanka.juwar@arrkgroup.com'
#             }
#     store.get_all_que()
#     # store.put(data, table_name)
#     response = table1.get_item(
#         Key={
#             'type': 'answer'
#         }
#     )
#     actual_output = response['Item']
#     assert actual_output == data

# --------------------------------------------------------------------------------------------------------------------


# @pytest.fixture
# def one():
#     return 1
#
#
# def test_we_are(one):
#     assert one == 1

# content of test_sample.py
# def func(x):
#     return x + 1
#
#
# def test_answer():
#     assert func(3) == 5


# @pytest.fixture
# def dynamodb_table(mocker):
#     # dynamo_client = boto3.resource(service_name='dynamodb', region_name='eu-west-1',
#     #                                aws_access_key_id='ASIAX2KHRAJAWARNJJFC',
#     #                                aws_secret_access_key='R3k5t65iDBDJBerzmorCAvuYuHzzDTmjKpEiZv3z',
#     #                                aws_session_token='IQoJb3JpZ2luX2VjED4aCWV1LXdlc3QtMSJHMEUCIHjfs9G8w80n82FootQKaheiMwXoJiAAYzmCkE06zLV3AiEAt85CseuHja/9N1+i/1QJs2vAf7n4TnhJivp7NMZkaFQqnAMIt///////////ARADGgw1Mzc1NTc3OTUzOTMiDMiqx+6c2gkOXBfGDSrwAnnk+PnYYx33WBqZVkE8MJicd3oN7ElfiwaBbOJSuanIxaeRUpaRM/YnB/FB2WRFP5xQwX5CoEeTdYFF13/pooSv7FxccAvaA/3ICa5aY9HFGe/3oiJbMqYJqkOAafr51sPcsF+lo6zbs6OCJGNV6xReQX0x2JV6u04RYpsxqYxfx1HgI1kc+hQu7NHOoET+bjEra4RicAKc0bGRZgCJZXD5Px15XmuZoyGrMbkzZCdG3JBfgs7vJ/f5pMPQmCv4m4xXKa3OH6UMCjhKZuMmsnBFsZRRGzC1O/cxvRTHBzjEVmt/IWczu8yw6T+7h9+dLgN1UBza9TEsUUbw5qFCWzFmUescfGBgwaf5I75Ja7+/SqqdPhPA6tFlU9cX25UCs/VqiPF+IC10m0kON7EIDPM7sfs3B9k/kJx0QlrXzXTJO3y/SGn0WAY7X0DO89oGHlRvddMLaw28kLlqk23dhrmThr8d6Hh4kmaOHo0ZHsZKMLz6554GOqYBTckjKC+US97eyUGGGxGDahZcrZD4DW6QcCXEXRxXe7smKcHo2DrAYIJPG+4VVjmO77kdrFBEjmiHrFYeKuenLI2MgJzonIPbXZIw4WsG2rajX5uNXBUpC1IIh2vU7vu6thwCFSy9m27dztsF86PujQqpAmBCcu1PvzgE2M8fWTRA35G52a0K5MJlNbXGgWJteXMipHK5elJsiN5C7HALNImJLBLDTA==')
#     # __connected_table__ = dynamo_client.Table("freshers-example")
#     mocker.patch.object(__connected_table__, "get_all_que")
#     return __connected_table__


# def test_get_all_que(dynamodb_table):
#     response = {"Item": {":question": "Explain about serverless?"}}
#     dynamodb_table.get_all_que.return_value = response
#
#     item = dynamodb_table.get_all_que(Key={":type": "question"})
#
#     assert "Item" in item
#     assert item["Item"] is not None

# def test_get_all_que(mocker):
#     # # dynamodb = boto3.client("dynamodb", region_name="us-east-1")
#     # mocker.patch.object(Service, "get_dynamo_client")
#     # Service.get_dynamo_client.return_value = Service.dynamo_client
#
#     db_table = Service.get_all_que()
#     mocker.patch.object(Service, "get_all_que")
#     Service.__connected_table__.return_value = db_table
#
#
# def test_get_que(mocker):
#     data = {
#         "userId": "mugdha@harakirimail",
#         "questionId": "5",
#         "sortKey": "question#mugdha@harakirimail.com#5"
#     }
#     mocker.patch.object(Service, "get_que")
#     Service.__connected_table__.return_value = db_table
#     response  = Service.get_que(data)

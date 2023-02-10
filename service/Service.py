import json
import os

from pprint import pprint

import boto3 as boto3
from boto3.dynamodb.conditions import Key, Attr
from flask import Response, make_response

table = os.getenv("freshers-example")
dynamo_client = boto3.resource(service_name='dynamodb', region_name='eu-west-1',
                               aws_access_key_id='ASIAX2KHRAJAYR5ZVHVM',
                               aws_secret_access_key='lKqeP/xLofAxieQ4AfrlqfkVFN+nwLK81qC+JGao',
                               aws_session_token='IQoJb3JpZ2luX2VjEBYaCWV1LXdlc3QtMSJHMEUCIQCD+cLtlHerpgAmk4JjRuDIWJl+uTMbkvU4PCq9mO8xOgIgLmJDspQVrN1upsQc++saB8VqPGhuJjQ4p4ebprNw2F0qnAMInv//////////ARAEGgw1Mzc1NTc3OTUzOTMiDINBZ1sDTMCgFp5+DirwAnQa1U6efWIU6DG+H6ocVxJ5obNFMQ527M0eFKzYujB32a85H34eTlyP6mnenPIdPLEKPEl0bTJMrFZbi/urIfmSWi+i6USYsbo67LCuqL47KhLk1r0Ggll70aVSlILPtlDKhqAGdYA/RD1VBmVYv1mrB2SSiN/K6mbNMgjd3cWVb1BGiwLNKuUXICn07y8/HX4JR0SHDSzObzX2HFemRhLAR0O8KIwIdrdsrR0ADbtO7eW9Bs8OE2Gmdzq/Mus7d5sRoNY5mNOxiQ29re26gPQvymaWwJQwz9UVG8A4P8hVxVWzeXTQZFXNalpLsM4Zw9zj774mGHZSwR6uZzRInp7Fhaxyegh5jJmAkMijXl9DhhsD3h4BEnm9fDwAf425nrSJBgAmJtmVV815/lF67bVe8HqL2brYt2pevAJv6rFL5fOOzF22ENOipdO7GqxWHsdwBXlXgHr00gKvOeYNiqFOvhrF1rF4zXnMK+NQM/uUMMuol58GOqYBkXDyVDBfQQO5ZIbhyo9BRUNetyfkvxYt9u2dnda67+TqxoI9dUME5c23414BUH5EsmT7hMMQBSpnpj1FqwXockVNsgW93SceyYNJ7h8/PPN8BIT+JWXE3dEPDFLsp54S1Bn1f9FA6SDsFmcIfra8cGuPCjCBT9eU1mUs8Kko99Qd4AAwylKG0yJS8xhS1ZHbFodC0tk+2+WGrE/9/S24mJlCkjCb7g=='
                               )
__connected_table__ = dynamo_client.Table("freshers-example")
print(__connected_table__.table_status)


class xyz():
    def post_questions_model(self):
        print("xyz")


# 1
def get_all_que():
    response = __connected_table__.query(
        KeyConditionExpression="#type = :type",
        ProjectionExpression='question',

        ExpressionAttributeNames={
            "#type": "type",

        },
        ExpressionAttributeValues={
            ":type": "question",

        }
    )
    pprint(response)
    # return Response("Fetching questions successfully", status=200)
    if 'Items' in response and response['Items'] != {}:
        print(response)
        print("SUCCESSFUL")
        return Response(status=200)
    else:
        return Response(status=404)


# 2
def get_que(data):
    response = __connected_table__.get_item(
        TableName="freshers-example",
        Key={
            'type': 'question',
            'sortKey': data['sortKey'],
        },

        ProjectionExpression="question"
    )
    pprint(response)

    if "Item" in response and response["Item"] != {}:
        print("SUCCESSFUL")
        return Response("Fetching questions successfully", status=200)
    else:
        print("INVALID UserId and QuestionID ")
        return Response("Bad Request", status=400)


# ----------------------------------------------------


# 3
def que_by_status(data):
    response = __connected_table__.query(
        KeyConditionExpression='#type = :typeval and sortKey = :sortKey',
        FilterExpression='#status = :statusval',  # and userId = :useridval ',
        ExpressionAttributeNames={
            '#type': 'type',

            '#status': 'status'
        },
        ExpressionAttributeValues={
            ':typeval': 'question',
            ':sortKey': data['sortKey'],
            # ':useridval': data['userId'],
            ':statusval': "1"
        },
        ProjectionExpression="question"
    )

    if 'Items' in response and response['Items'] != {}:
        print(response)
        print("SUCCESSFUL")
        return Response("Fetching questions successfully", status=200)
    else:
        print("INVALID UserId and QuestionID ")
        return Response("Bad Request", status=400)


# 4
def put_answer(data):
    item = {
        'type': 'answer',
        'sortKey': data['sortKey'],
        'answer': data['answer'],
        'createdAt': data['createdAt'],
        'status': '1',
        'userId': data['userId']

    }

    print(item)
    response = __connected_table__.put_item(
        TableName='freshers-example',
        Item=item
    )
    print(response)
    return Response("Successfully added a answer", status=200)


# 5
def edit_question(data):
    response = __connected_table__.update_item(
        Key={
            'type': "question",
            'sortKey': data['sortKey'],

        },
        UpdateExpression='SET question = :newQuestion',
        ExpressionAttributeValues={
            ':newQuestion': data['edited_que']
        },
        ReturnValues="UPDATED_NEW"
    )
    print(response)
    return Response("Successfully updated", status=200)


# 6
def delete_answer(data):
    response = __connected_table__.delete_item(
        Key={
            'type': "answer",
            'sortKey': data['sortKey'],

        }

    )

    pprint(response)
    return Response("Successfully deleted", status=200)

    # response = make_response("Successfully deleted", 200)
    # return response
    # if "Item" in response and response["Item"] != {}:
    #     print("SUCCESSFUL deleted")
    #     return Response("Deleted questions successfully", status=200)
    # else:
    #     print("INVALID UserId and QuestionID ")
    #     return Response("Bad Request", status=400)

# --------------------------------------------------------------------------------

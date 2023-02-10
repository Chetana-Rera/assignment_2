from datetime import date

from service.Service import get_que, put_answer, delete_answer, get_all_que, edit_question, que_by_status, xyz


def get_all():
    print("fetching all questions")
    # return get_all_que()
    # print(que)
    # get_all_que()
    xyz.post_questions_model("xyz")
    return "message"
    # print(Response("Fetching questions successfully", status=200))

# 1
# def get_all():
#     print("fetching all questions")
#     que = get_all_que()
#     print(que)
#     print(Response("Fetching questions successfully", status=200))


get_all()


# 2
def get_by_id( ):
    print("fetching question by ID")
    userId = input("enter your userId: ")
    questionId = str(input("enter question Id: "))
    sortKey = "question#" + userId + "#" + questionId
    data = {
        "userId": userId,
        "questionId": questionId,
        "sortKey": sortKey
    }
    response = get_que(data)
    # print(response)
    return 'SUCCESS'



#get_by_id()

# 3
def get_by_st():
    print("fetching active questions")
    userId = input("enter your userId: ")
    questionId = input("enter question Id: ")
    sortKey = "question#" + userId + "#" + questionId
    data = {
        "userId": userId,
        "questionId": str(questionId),
        "sortKey": sortKey
    }
    return que_by_status(data)
    # que = que_by_status(data)
    # print(que)


#get_by_st()

# 4
def put():
    print("Enter your data")
    answer = input("enter answer: ")
    userId = input("enter your userId: ")
    questionId = input("enter question Id: ")
    sortKey = "answer#" + questionId + "#" + userId
    createdAt = str(date.today())
    data = {
        "userId": userId,
        "questionId": questionId,
        "sortKey": sortKey,
        "createdAt": createdAt,
        "answer": answer
    }
    return put_answer(data)
    # print(ans)
    # print(Response("Successfully Enter", status=200))


# put()

# 5
def update():
    print("Enter your data")
    userId = input("enter your userId: ")
    questionId = input("enter question Id: ")
    edited_que = input("edited question: ")
    sortKey = "question#" + userId + "#" + questionId
    data = {
        "userId": userId,
        "questionId": questionId,
        "sortKey": sortKey,
        "edited_que": edited_que
    }
    return edit_question(data)
    # ans = edit_question(data)
    # print(ans)


#update()

# 6
def delete():
    print("Enter your data")
    userId = str(input("enter your userId: "))
    questionId = str(input("enter question Id: "))
    sortKey = "answer#" + questionId + "#" + userId
    data = {
        "userId": userId,
        "questionId": questionId,
        "sortKey": sortKey
    }
    return delete_answer(data)

#delete()

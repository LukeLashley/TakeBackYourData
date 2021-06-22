import json
from Users import Users
import operator
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route("/")
def index():
    return "hello world"


f = open('conversation.json', encoding='utf-8')
data = json.load(f)
dictionary = {}
for i in data['members']:
    user = Users(i['name'], i['user_id'], i['nickname'], i['muted'], i['image_url'], 0)
    dictionary[i['user_id']] = user

f = open('message.json', encoding='utf-8')
data = json.load(f)
totalMessages = 0
for i in data['messages']:
    if i['system']:
        if i['event']['type'] == "membership.announce.added":
            if str(i['event']['data']['adder_user']['id']) not in dictionary:
                user = Users(i['event']['data']['adder_user']['nickname'], str(i['event']['data']['adder_user']['id']),
                             i['event']['data']['adder_user']['nickname'], False, '', 0)
                dictionary[str(i['event']['data']['adder_user']['id'])] = user
            for j in i['event']['data']['added_users']:
                dictionary[str(i['event']['data']['adder_user']['id'])].increaseAddedMembers()
                if str(j['id']) not in dictionary:
                    user = Users(j['nickname'],
                                 str(j['id']),
                                 j['nickname'], False, '', 0)
                    dictionary[str(j['id'])] = user
        if i['event']['type'] == "membership.notifications.exited":
            if str(i['event']['data']['removed_user']['id']) not in dictionary:
                user = Users(i['event']['data']['removed_user']['nickname'], str(i['event']['data']['removed_user']['id']),
                             i['event']['data']['removed_user']['nickname'], False, '', 0)
                dictionary[str(i['event']['data']['removed_user']['id'])] = user
            dictionary[str(i['event']['data']['removed_user']['id'])].increaseLeft()
        if i['event']['type'] == "membership.notifications.removed":
            if str(i['event']['data']['removed_user']['id']) not in dictionary:
                user = Users(i['event']['data']['removed_user']['nickname'], str(i['event']['data']['removed_user']['id']),
                             i['event']['data']['removed_user']['nickname'], False, '', 0)
                dictionary[str(i['event']['data']['removed_user']['id'])] = user
            dictionary[str(i['event']['data']['removed_user']['id'])].increaseRemoved()
            dictionary[str(i['event']['data']['remover_user']['id'])].increaseRemoving()
        if i['event']['type'] == "membership.nickname_changed":
            dictionary[str(i['event']['data']['user']['id'])].increaseNickNameChange()
        if i['event']['type'] == "group.name_change":
            dictionary[str(i['event']['data']['user']['id'])].increaseGroupNameChange()

    if i['sender_id'] not in dictionary:
        user = Users(i['name'], i['sender_id'], i['name'], False, i['avatar_url'], 0)
        dictionary[i['sender_id']] = user
        print("fail" + i['sender_id'])
    totalMessages = totalMessages + 1
    dictionary[i['sender_id']].addMessage()
    if dictionary[i['sender_id']].getMostLikes() < len(i['favorited_by']):
        dictionary[i['sender_id']].setMostLikes(len(i['favorited_by']))
        dictionary[i['sender_id']].setMostLikedPost(i['source_guid'])
    dictionary[i['sender_id']].setTotalLikes(len(i['favorited_by']))
    for j in i['favorited_by']:
        if j == i['sender_id']:
            dictionary[j].increaseSelfLike()
            dictionary[j].increaseFavorites()

    if "hi " in str(i['text']).lower():
        if "i'm " in str(i['text']).lower():
            print(i['text'])        


print(totalMessages)
highestVal = [0, 0, 0, 0, 0]
highestValUser = ["", "", "", "", ""]
for i in dictionary:
    for j in range(5):
        if dictionary[i].getTotalMessages() > highestVal[j]:
            temp = highestVal[j]
            tempVal = j
            for k in range(4 - j):
                if highestVal[4 - k] < temp:
                    temp = highestVal[4 - k]
                    tempVal = 4 - k
            highestVal[tempVal] = dictionary[i].getTotalMessages()
            highestValUser[tempVal] = dictionary[i].getName()
            break

print(highestValUser)
print(highestVal)
highestVal = [0, 0, 0, 0, 0]
highestValUser = ["", "", "", "", ""]
for i in dictionary:
    for j in range(5):
        if dictionary[i].getTotalLikes() > highestVal[j]:
            temp = highestVal[j]
            tempVal = j
            for k in range(4 - j):
                if highestVal[4 - k] < temp:
                    temp = highestVal[4 - k]
                    tempVal = 4 - k
            highestVal[tempVal] = dictionary[i].getTotalLikes()
            highestValUser[tempVal] = dictionary[i].getName()
            break
print(highestValUser)
print(highestVal)
bestPost = ["", "", "", "", ""]
highestVal = [0, 0, 0, 0, 0]
highestValUser = ["", "", "", "", ""]
for i in dictionary:
    for j in range(5):
        if dictionary[i].getMostLikes() > highestVal[j]:
            temp = highestVal[j]
            tempVal = j
            for k in range(4 - j):
                if highestVal[4 - k] < temp:
                    temp = highestVal[4 - k]
                    tempVal = 4 - k
            highestVal[tempVal] = dictionary[i].getMostLikes()
            highestValUser[tempVal] = dictionary[i].getName()
            bestPost[tempVal] = dictionary[i].getMostLikedPost()
            break
print(highestValUser)
print(highestVal)
print(bestPost)
highestVal = [0, 0, 0, 0, 0]
highestValUser = ["", "", "", "", ""]
for i in dictionary:
    for j in range(5):
        if dictionary[i].getAddedMembers() > highestVal[j]:
            temp = highestVal[j]
            tempVal = j
            for k in range(4 - j):
                if highestVal[4 - k] < temp:
                    temp = highestVal[4 - k]
                    tempVal = 4 - k
            highestVal[tempVal] = dictionary[i].getAddedMembers()
            highestValUser[tempVal] = dictionary[i].getName()
            break
print(highestValUser)
print(highestVal)
print(totalMessages)


@app.route("/test")
@cross_origin(supports_credentials=True)
def returnUsers():
    arr = []
    for i in dictionary:
        arr.append(dictionary[i].serialize())
        
    return json.dumps(arr)

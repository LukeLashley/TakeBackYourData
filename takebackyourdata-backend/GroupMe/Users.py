class Users():
    totalMessages = 0

    def __init__(self, name, user_id, nickname, muted, image, totalMessages):
        self.name = name
        self.user_id = user_id
        self.nickname = nickname
        self.muted = muted
        self.image = image
        self.totalMessages = totalMessages
        self.totalLikes = 0
        self.mostLikes = 0
        self.mostLikedPost = ""
        self.addedMember = 0
        self.removedMember = 0
        self.leftGroup = 0
        self.removed = 0
        self.likedMessages = 0
        self.nameChanges = 0
        self.groupNameChanges = 0
        self.messageToLikes = 0
        self.mostWeightedLikes = 0
        self.mostWeightedLikedPost = ""
        self.totalWeightedLikes = 0
        self.selfLikes = 0

    def printUser(self):
        print("Name: " + self.name)
        print("User_id: " + self.user_id)
        print("Nickname: " + self.nickname)
        print("muted:" + str(self.muted))
        print("total messages: " + str(self.totalMessages))
        if self.image is not None:
            print("Image: " + self.image)

    def addMessage(self):
        self.totalMessages += 1

    def getName(self):
        return self.name

    def getTotalMessages(self):
        return self.totalMessages

    def getTotalLikes(self):
        return self.totalLikes

    def getMostLikes(self):
        return self.mostLikes

    def getMostLikedPost(self):
        return self.mostLikedPost

    def setMostLikedPost(self, post):
        self.mostLikedPost = post

    def setMostLikes(self, number):
        self.mostLikes = number

    def setTotalLikes(self, number):
        self.totalLikes += number

    def increaseAddedMembers(self):
        self.addedMember += 1

    def getAddedMembers(self):
        return self.addedMember

    def increaseLeft(self):
        self.leftGroup += 1

    def increaseRemoved(self):
        self.removed += 1

    def increaseRemoving(self):
        self.removedMember += 1

    def calcMLRatio(self):
        if self.totalMessages != 0:
            self.messageToLikes = self.totalLikes / self.totalMessages

    # def calcMessagesPerDay(self):


    def increaseNickNameChange(self):
        self.nameChanges += 1

    def increaseGroupNameChange(self):
        self.groupNameChanges += 1

    def increaseFavorites(self):
        self.likedMessages += 1

    def increaseSelfLike(self):
        self.selfLikes += 1

    def serialize(self):
        self.calcMLRatio()
        return {
            'name': self.name,
            'id': self.user_id,
            'nickname': self.nickname,
            'muted': self.muted,
            'image': self.image,
            'removed': self.removed,
            'totalMessages': self.totalMessages,
            'totalLikes': self.totalLikes,
            'mostLikes': self.mostLikes,
            'mostLikedPost': self.mostLikedPost,
            'addedMember': self.addedMember,
            'removedMember': self.removedMember,
            'leftGroup': self.leftGroup,
            'likedMessages': self.likedMessages,
            'nameChanges': self.nameChanges,
            'groupNameChanges': self.groupNameChanges,
            'messagesToLikes': self.messageToLikes,
            'selfLikes': self.selfLikes
        }

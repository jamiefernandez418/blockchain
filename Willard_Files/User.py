import random

class User:
    def __init__(self, firstName, lastName):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__randVal = random.randint(1, 123456789)
        self.__userID = hash(firstName+lastName+str(self.__randVal))
    
    def getName(self):
        return (self.__firstName + ' ' + self.__lastName)
    
    def getUserId(self):
        return self.__userID

    def __getUserRandVal(self):
        return self.__randVal
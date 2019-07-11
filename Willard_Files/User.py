import random

class User:

	__requestID = {}
	
    def __init__(self, firstName, lastName):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__randVal = random.randint(1, 123456789)
        self.__userID = hash(firstName+lastName+str(self.__randVal)
    
    def getName(self):
        return (self.__firstName + ' ' + self.__lastName)
    
    def getUserId(self):
        return self.__userID

    def __getUserRandVal(self):
        return self.__randVal
    
    def __getRequestId(self, book):
    	return self.__requestId.get(book)
    #ASSERT: Will return the corresponding request id when given the book as a parameter
    
    def __addRequestID(self, book, id):
    	self.__requestId[book] = id
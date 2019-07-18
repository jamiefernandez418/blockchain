import User
import Book
import BChain
import Block
import BookShelf


class Regulator:

	
	__masterLedger = {} #dictionary of each book's blockchain 
	
	def _init_(self):
	#TO BE IMPLEMENTED
	
	
'User Management Methods-----------------------------------------------------------------'
	
	def removeUser():
	'''
		PURPOSE: REMOVE USER FROM DATABASE
	'''
	#TO BE IMPLEMENTED
	
	def validUser(self, person):
	'''
		PURPOSE: CHECKS DATABASE TO SEE IF PERSON IS PART OF THE NETWORK
    '''
    #TO BE IMPLEMENTED

'Request Management Methods--------------------------------------------------------------'
	
	def setRequestId(self):
	'''
		PURPOSE: GENERATE REQUEST ID WITH 3 DIGITS
	'''
        id= random(3)
        return id

'''
    def request(self, username, isbn):
        requestID = self.setRequestId()
        if(self.requestinfo("name") == ''):
            self.requestinfo(username, isbn)
            self.unconfirmed_transactions.append(self.requestinfo)

        if(self.requestinfo("name") == username):
            User.getUser(username).requestID = requestID
            return "The request was generated here is your Request ID: " + requestID

        else:
            return "fail"
    
              
      def requestIDpublish(self, requestid, name):
        if(name == self.requestinfo("name")):
            self.requestinfo("requestidpval").set(requestid)
            self.unconfirmed_transactions.append(self.requestinfo)
            return "Success"
        else:
            return "fail"
'''

	
'Ledger Management Methods---------------------------------------------------------------'
	
	def __updateLedger(self, isbn, nbchain):
	'''
		PURPOSE: UPDATE MASTER LEDGER WITH NEW BLOCKCHAIN FOR THE CORRESPONDING BOOK
	'''
		self.__masterLedger[isbn] = nbchain
		
	def getbookLedger(self)
	'''
		PURPOSE: RETURN COPY OF THE MASTERLEDGER SO THAT USER CAN UPDATE PERSONAL LEDGER
	'''
		return self.__masterLedger
	
	
'Transaction Validation Methods----------------------------------------------------------'
	def validateTransaction(self, isbn, rid, pblock):
	'''
		PURPOSE: VALIDATE THE CREATED BLOCK BY CREATING A VALID BLOCK USING TRANSACTION INFORMATION
		(EX. REQUEST ID AND PREVIOUS TRANSACTION KEY FOR THE BOOK) AND COMPARING THE KEYS OF 
		BOTH BLOCKS. IF THE CREATED BLOCK IS CORRECT THEN TRANSACTION WILL BE ADDED TO BCHAIN
	'''
	
		blckchain = self.__masterLedger[isbn]           #book's blockchain
		lastKey = blckchain.lastblock().getBlockHash()  #last block in blockchain
		validBlock(lastKey, rid)
		if pblock.getBlockHash() == validBlock.getBlockHash()
			self.__addTransaction(isbn, pblock)
        	return true 
        else 
        	self.__blockTransaction()
        	return false
        	
        	

	def __addTransaction(self, isbn, nblock): 
	'''
		PURPOSE: ADD TRANSACTION TO BLOCK CHAIN AND UPDATE MASTER LEDGER
	'''
		book = shelf.findBook(isbn) 
		book = addtoBlockChain(nblock)
		self.__updateLedger(isbn, book.getBlockChain())
		
		#METHODS .findBook(), addtoBlockChain(), && getBlockChain() ARE NOT IMPLEMENTED 
		#THEY WOULD CORRESPOND TO bookshelf.py && Book.py FILES
		

	
	def blockTransaction(self):
			#TO BE IMPLEMENTED

		
		
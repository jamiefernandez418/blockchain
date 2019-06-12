class Block:
    'Basic Block for our Blockchain'
    # Basic class attributes of Block
    __previousHash = ''
    __blockData = ()
    __blockHash = ''

    # Constructor for Block Class
    def __init__(self, prevHash, blockData):
        self.__previousHash = prevHash
        self.__blockData = blockData
        self.__blockHash = self.setBlockHash(self.__previousHash, self.__blockData)
        # TODO: Create a system generated Timestamp based on the linux EPOCH
        # TODO: Look into Possibly using the Timestamp as a means of validation for adding to the chain
        # SystemGenerated TimeStamp 

    # Returns the Previous Hash that is stored on the current Block
    def getPreviousHash(self):
        return self.__previousHash

    # Returns the data
    def getTransactionData(self):
        return self.__blockData

    # Returns The Hash of the Current Block
    def getBlockHash(self):
        return self.__blockHash

    # Sets the Blocks Hash. Currently using the basic python hash function
    # TODO: Research SHA256 Hashing Algorithm and if that needs to be implemented for this project
    def setBlockHash(self, data, prevhash):
        return hash((data, prevhash))
    
    # Returns all of the Pertinent Information of the Block
    def retriveBlockInfo(self):
        print('\nPrevious Hash:', self.__previousHash, '\nData:', self.__blockData, '\nBlock Hash:', self.__blockHash, '\n')

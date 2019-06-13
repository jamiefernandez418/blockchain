import Block
import BChain
import time
import Book
import hashlib



def main():
    myBlockChain = BChain.BlockChain()
    book1 = Book.Book('My Book', ['Willard Joseph'], ['Mystery', 'Crime', 'Suspense'], '123-2345-4567', 'B15464646')
    book2 = Book.Book('Our Book', ['Jessica', 'Jaime', 'Aiza'], ['Suspense'], '987-8765-765', 'B32352342')

    GenesisBlock = Block.Block('0', book1)
    SecondBlock = Block.Block(GenesisBlock.getBlockHash(), book2 )
    myBlockChain.addValidBlock(GenesisBlock)
    myBlockChain.addValidBlock(SecondBlock)
    
    myBlockChain.printChainInfo()
    

    # Tested against an online SHA256 Generator
    # print(hashlib.sha256('Willard'.encode('utf-8')).hexdigest())
    

main()
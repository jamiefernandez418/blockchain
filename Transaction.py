import Block
import Book
import BChain
import RequestSystem
import random

def new_transaction(self, requestor, recipient, requestID, bookname):
    """
    Creates a new transaction to go into the next mined Block
    :param sender: Address of the Sender
    :param recipient: Address of the Recipient
    :param requestID: ID number given to the
    :return: The index of the Block that will hold this transaction
    """
    self.current_transactions.append({
        'Username': requestor,
        'Bookname': bookname,
        'requestID': requestID,
    })
    return BChain.last_block['index'] + 1







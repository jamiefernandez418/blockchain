import Block
import BChain
import time
import Transaction
import Book
import hashlib
import json

class Mining:
    """
    def proof_of_work(self, block):

        Function that get the requestID and  to get a hash
        that satisfies our difficulty criteria.

        difficulty = Book.requestID
        previous_Hash = Block.getPreviousHash()

        computed_hash = Block.setBlockHash256(difficulty,previous_Hash)

        return computed_hash
    def __init__(self):

        last_block = BChain.last_block()
        proof = Mining.proof_of_work(last_block)

        # We must receive a reward for finding the proof.
        # The sender is "0" to signify that this node has mined a new coin.
        Transaction.new_transaction(
            sender="0",
            recipient=node_identifier,


            )
    """

    def proof_of_work(self, block):
            """
            Simple Proof of Work Algorithm:

            :param last_proof: <int>
            :return: <int>
            """

            startingvalue = 0
            while self.valid_proof(block, startingvalue) is False:
                startingvalue += 1

            return startingvalue

    @staticmethod
    def valid_proof(block, startingvalue):
            """
            Validates the Proof: Does hash(last_proof, proof) contain the requestID?

            """

            validatingHash = Block.setBlockHash256(startingvalue, block)
            return validatingHash[:6] == Book.requestinfo("requestid")

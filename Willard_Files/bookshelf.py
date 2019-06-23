import Book 


class Bookshelf:

    index= {}

    #Initialization of object with possibility of adding genre
    def __init__(self,genre=None):
        self.genre = genre

    #Adds a book to the shelf
    def addBook(self,isbn,book): 
        self.index[isbn]= book

   

        





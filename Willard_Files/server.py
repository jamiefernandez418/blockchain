from flask import Flask
import bookshelf, Book
app = Flask(__name__)

@app.route('/')
def hello_world():
    
   # shelf=Bookshelf()
    
    book = Book.Book('The Talisman', ['Stephen King', 'Peter Straub'], [
            'Fantasy', 'Thriller'], '978-1451697216', 'B0000000002')
    shelf=bookshelf.Bookshelf()
    shelf.addBook(book.getISBN(),book)
    
    print(shelf.index[book.getISBN()])
    #print(book.getISBN())
    print("Hello terminal test")
    return 'Hello World!'
    #render_template('index.html', bookshelf=bookshelf)

from flask import Flask, render_template, request
import bookshelf, Book
app = Flask(__name__)

@app.route('/')
def hello_world():
    
        # shelf=Bookshelf()
    
        book1 = Book.Book('To Kill A Mockingbird', ['Harper Lee'], [
                      'Novel', 'Bildungsroman', 'Southern Gothic', 'Thriller', 'Domestic Fiction', 'Legal Story'], '978-0446310789', 'B0000000001')
        book2 = Book.Book('The Talisman', ['Stephen King', 'Peter Straub'], [
                      'Fantasy', 'Thriller'], '978-1451697216', 'B0000000002')
        book3 = Book.Book('The Bad President', ['Donald Trump'], [
                       'Impeachment', 'Delusional'], '978-1sdfasdfasdff', 'B0000000003')

        shelf=bookshelf.Bookshelf()

        #Adds a Book into the shelf
        shelf.addBook(book1)
        shelf.addBook(book2)
        shelf.addBook(book3)
       # print(shelf.index[book.getISBN()])

        books=shelf.index

        #Prints every book inside index. 
        for isbn in books:
                print(isbn)
                print(books[isbn].getAuthor())

       
        #print(book.getISBN())
        print("Hello terminal test")
        return render_template('index.html', books= books)

#Takes isbn and will make the request for the book
@app.route('/request')
def request_class():
        isbn = request.args.get('book')
        print(isbn)
        return isbn
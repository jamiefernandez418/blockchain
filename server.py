from flask import Flask, render_template, request,url_for,session,redirect
from library import bookshelf
from library import Book
import os
from . import db 
app= Flask(__name__)
app.secret_key = os.urandom(16)

@app.route('/')
def index():
        if 'username' in session:

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
                return render_template('index.html', books= books,  username= session['username'])

        return redirect(url_for('login'))  
#Takes isbn and will make the request for the book
@app.route('/request', methods=['GET', 'POST'])
def request_class():
        if request.method =='GET':
                isbn = request.args.get('book')
                print(isbn)

                return isbn 
@app.route('/login', methods=['GET', 'POST'])
def login():
        if request.method=='POST':
                session['username'] = request.form['username']
                return redirect(url_for('index'))
        return render_template('login.html')

@app.route('/profile')
def profile():
        return 'Profile'
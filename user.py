from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class User(db.model):
    __tablename__='user'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),unique=True,nullable=False)
    password = db.Column(db.String,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    authenticated = db.Column(db.Boolean,default = False)
    
    def __init__(self,username,email,active=True):
        self.username=username
        self.email=email
        self.active=active
        


    def is_active(self):
        return self.active

    #def is_authenticated (self):
        #check if password is same as stored 

    #def get_id(self):
        #return id of user

    #def is_anonymous(self: (optional)
        #Returns if user anonymous
    


        
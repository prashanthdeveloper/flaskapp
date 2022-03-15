from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()





class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))
    profilepicture = db.Column(db.String(80))
    image = db.Column(db.String())
    
    


# class Register(db.Model):

#     id = db.Column(db.Integer, primary_key=True)
#     email=db.Column(db.Integer,unique=True)
#     password=db.Column(db.Integer())
#     repeatpassword=db.Column(db.Integer())

# class Login(db.Model):

#     id = db.Column(db.Integer, primary_key=True)
#     username=db.Column(db.String(),unique=True)    
#     password=db.Column(db.Integer())

    # def __init__(self,uname,pwd):
        
    #     self.username = uname
    #     self.password= pwd
        


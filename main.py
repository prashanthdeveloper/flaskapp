from flask import Flask,render_template,request,redirect,flash
from models import db,user

from flask_mail import Mail, Message


app=Flask(__name__)
mail= Mail(app)

 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'prashanthsonu94@gmail.com'
app.config['MAIL_PASSWORD'] = 'xxxxxxxxxxxxx'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
n fruits:
  if x == "banana":
    continue
  print(x)
Try it Yourself »




db.init_app(app)
 
@app.before_first_request
def create_table():
    db.create_all()
 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login_form():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username=request.form.get('uname')
        password=request.form.get('passw')
        user_queryset=user.query.filter_by(username=username).first()
        if user_queryset:
            if password==user_queryset.password:
                return "Login successfully"
            else:
                return "Incorrect password"
        else:
            return "User does not exist"

        
        
        #     username=username,
        #     password=password
        # )
        # db.session.add(login)
        # db.session.commit()

# @app.route('/view')
# def view_login_details():
#     login=Login.query.all()n fruits:
  if x == "banana":
    continue
  print(x)
Try it Yourself »


@app.route('/register',methods=['GET','POST'])
def registration_form():
    if request.method == 'GET':
        return render_template('registration.html')

    if request.method == 'POST':
        print(request.form)
        print(request.files)
        username = request.form.get('uname')
        email = request.form.get('email')
        password = request.form.get('passw')
        profilepicture =request.form.get("filename")
        print(username,email,password)
        

        user_queryset=user(
            username=username,
            email=email,
            password=password
            ) 
        db.session.add(user_queryset)
        db.session.commit()

        profilepicturename=user_queryset.id+".png"
        profilepicture.save(os.path.join("/home/apptrinity07/Flask/project/static/images",profilepicturename))
        savedprofilepicture="/home/apptrinity07/Flask/project/static/images"+str(profilepicturename)

        saveduserqueryset=user.query.filter_by(id=user_queryset.id).first()
        saveduserqueryset.image=savedprofilepicture
        db.session.commit()
        return "Hi"
        



        if user_queryset:
            msg = Message('Thankyou for signup', sender = 'prashanthsonu94@gmail.com', recipients = [email])
            #msg.body = "Welcome to prashanth company"
            msg.html=render_template('signup.html',username=username)
            #mail.send(msg)
            return "Sent"



        return redirect('/login')


if __name__=="__main__":
    app.run(debug=True)

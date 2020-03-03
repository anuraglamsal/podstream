from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import SignUp, Login

                #Here, we have imported our 'forms.py' module to actually use
                #the features of wtforms and the entities initialized in that
                #module by creating objects of the specific classes in this
                #module.

app = Flask(__name__)

                #__name__ returns the name of the module--here
                #the name is "main"--when it is used in some other module.
                #In the module itself however, it returns "__main__".
                #You can use this property to prevent your code
                #from running in other modules i.e. indicating that
                #this particular code is the "main code" like creating
                #the main function in C. We do this at the bottom here.

                #In this particular scenario, Flask uses the name of the module
                #to figure out where all the things like templates,
                #static files, etc. of the application are stored. It basically
                #sets up our app. How it does it is black box to me.

app.config['SECRET_KEY'] = 'CLFA58C61A'

                #Go to this link for information regarding the use of this
                #secret key - https://imgur.com/a/t3bnRj5

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

                #There are different models that have been made to work with
                #data. One of them is the 'relational' model. A database created
                #with the relational model is a relational database. A system
                #created to "manage" data i.e. create, read, update, delete,
                #under the relational paradigm is called a 'Relational Database
                #Management System'. These systems are basically languages that
                #you use to work with a relational database. One of them is
                #SQL (Structured Query Language). Just like there are different
                #frameworks for backend stuff in Python like Django and Flask,
                #there are different "frameworks" within the SQL paradigm to
                #work with relational databases. These "frameworks" have their
                #own pros and cons, just like Django and Flask. One of them is
                #'sqlite'. From what I've read, sqlite is very good for
                #databases pertaining to applications that are not used by
                #many users. But it starts running into problems when the user
                #number starts to increase. Thus, apparently, it is good to
                #use during development. And the 'SQLAlchemy' library that we
                #are using makes it easy to shift between different "frameworks"
                #,thus, giving us the ability to use different suited "frameworks"
                #during different steps of development.

                #Here, we are basically configuring a database for our app by
                #providing the app the URI of the database. If we haven't manually
                #created one, this creates one for us. Here, praticularly, we
                #have created a database named 'site.db' which works under the
                #sqlite "framework".

db = SQLAlchemy(app)

                #Here, we have created an object of the 'SQLAlchemy' class and
                #have provided our 'app' object as an attribute of this 'db'
                #object. This basically configures our app such that now, we
                #can work with data under the relational model, using the
                #SQL language, within the sqlite "framework" by using the
                #object-oriented setup put together by the SQLAlchemy library.
                #We are basically exploiting the object-oriented paradigm to
                #work with relational databases relatively easily using
                #SQLAlchemy.

class User(db.Model):

                #Here, we create a class that acts as a "model" of our database
                #i.e. we specify the types of data that we can add on particular
                #columns. For that, we inherit the 'Model' attribute of the
                #'SQLAlchemy' class that works with the 'sqlalchemy' library in
                #some black box way to provides us all the required classes and
                #functions of that library.

            id = db.Column(db.Integer, primary_key=True)

                #We specify the 'id' "field" or column here. We do that
                #by creating an object of the 'Column' class that was made
                #accessible by the inheritance that was done above. We could also
                #directly import the 'Column' class from the 'sqlalchemy' library
                #if we wanted to, but that would be a hassle compared to this.
                #The whole point of 'flask_sqlalchemy' is to remove removable
                #hassles. Regardless, as a value of an attribute of the 'Column'
                #class, another class 'Integer' is sent. It seems to me that the
                #whole class is sent rather than an instance of it. IDK why. But the
                #application of that is to specify the data type permissible in
                #this field--which is integer here. Another attribute at play here
                #is the 'primary_key' attribute whose value is returned as 'True'.
                #Now, this field's been initiated to store the primary keys for
                #data in each row. The use of primary keys is to make each data
                #unique. This is especially helpful when different user data contain
                #simlar information and we need only one of them to do whatever we
                #want to do. The primary key for each data is assigned by the
                #system itself.

                #For this database, we could technically use users' usernames as
                #primary keys which we'll set later to be unique for each user,
                #but that would make things way slower. Thus, an integer primary
                #key is preferred. Also, if a user changes their username later,
                #that could also apparently cause problems.

            firstname = db.Column(db.String(50), nullable=False)

                #Here, we create a field to store the first names of users.
                #For that, we send an instance of the 'String' class as a value
                #of an attribute of our 'firstname' object. This specifies that
                #only strings are permissible in this field. We also send '50'
                #as a value of an attribute of the 'String' class which specifies
                #the maximum length of string permissible. As our first name
                #field shouldn't be empty, we also pass 'False' as a value of the
                #'nullable' attribute of the 'Column' class. These act as double
                #validation for data sent through the web app, and also as the
                #first validation if user data is directly inserted in the database.

            middlename = db.Column(db.String(50))

                #Doing the same for middle names of users. We don't specifically
                #define 'nullable' here as there might not be any middle name.
                #The default value of 'nullable' is 'True'. Thus, it works out
                #anyways.

            lastname = db.Column(db.String(50), nullable=False)
            email = db.Column(db.String(100), unique=True, nullable=False)

                #As we want each user to have a unique email associated with
                #their account, we send the value of the 'unique' attribute to be
                #'True'. By default it's 'False'. This prevents repetition of
                #emails in different user data.

           username = db.Column(db.String(20), unique=True, nullable=False)
           password = db.Column(db.String(60), nullable=False)

                #We set the maximum length of the password field to be '60'
                #because passwords are stored as hashes in databases for
                #security purposes. They are converted to hashes using
                #ideally the latest and greatest hashing algorthims. The reason
                #of doing so is elaborated in the link below:
                #https://imgur.com/a/oRtiLDm

                #'Usernames' should be unique for each user to remove general
                #confusion, prevent identity theft, etc. Thus, this enables
                #passwords for each user to not be unique as the combination of
                #username/email and password turns out to be a good login
                #credential format. But that doesn't get rid of the fact that
                #passwords should be made super difficult to presume.

@app.route("/", methods = ['GET', 'POST'])

                #This creates a path. Here particularly, if there is
                #nothing written after '/' in the URL, the function under
                #this is returned. It may be '/home' or '/about' or anything
                #that you want. Flask uses decorators for this. Again,
                #black box.

                #We also mention the methods of requests here as the same path
                #can receive requests made with different request methods.
                #Here, we write 'GET' for when a user initially requests this
                #path to view the form. We write 'POST' for when a user makes
                #request to submit their filled form.

def signup():   #Now, everything that you need to do for that particular
                #path of the web app is done under this function.

  up = SignUp() #As we have imported the 'forms.py' module in this module, we
                #create an object of the 'SignUp' class here to be able
                #to access all the direct or indirect attributes pertaining
                #to that class. Now, we can send this object to our html
                #to work with fields and labels, manipulate submitted
                #data, use validators, etc.

  if up.validate_on_submit():

                #validate_on_submit() is a function that checks if the data
                #entered by the user is valid according to the conditions that
                #we set on 'forms.py'. It is a function of the 'FlaskForm'
                #class that we inherited in our 'SignUp' class.

           flash(f'Account for {up.Username.data} has been created. Sign in from here.')

                #The 'flash' function is used to return a string for one
                #request only i.e. after the string is seen once on a page,
                #we don't see it if we refresh it or specifically, we don't
                #see it if another request is made. This is especially useful
                #if we want to tell the user about their success or failure in
                #regards to the creation of their account on a pre-existing page
                #rather than creating a completely different page for it. But
                #if we use a pre-existing page whose purpose is not to only
                #show the message of success or failure, we want it to be a one
                #time thing only--thus, the usage of 'flash'.

           return redirect(url_for('login'))

                #The 'redirect' function is used to redirect the user to a
                #particular path. The argument is the URL address of the path.
                #If we don't want to type the whole URL, we can just use the
                #'url_for' function which builds the URL pertaining to the
                #function given as argument for us.

  return render_template('signup.html', up=up)

                #Here, we use the 'render_template' function to provide the
                #name of the html page pertaining to this path that it will
                #search in the 'templates' folder to send to the browser when
                #a user tries to access the path. The 'up=up' is used to
                #notify the template engine i.e 'Jinja' that this 'up' object
                #has been used in the html and it requires the interpretation
                #of the engine to actually work on the html.

                #Jinja is a template engine that gives us the ability to use
                #Python commands in html. We can use variables that we declared
                #in our Python program and manipulate them using commands like
                #"for" statetments, "if" statements, etc. in our html with the
                #aid of Jinja. It has its own syntax structure that we must
                #follow. This is how we are able to use the fields and
                #such that we declared in 'forms.py' in our html.

@app.route("/login", methods = ['GET', 'POST'])
def login():
     log = Login()
     if log.validate_on_submit():
         flash(f'You are logged in.')
     return render_template('login.html', log=log)

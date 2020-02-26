from flask import Flask, render_template
from forms import SignUp, Login

                #Here, we have imported our forms.py module to actually use
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

@app.route("/")

                #This creates a path. Here particularly, if there is
                #nothing written after '/' in the URL, the function under
                #this is returned. It may be '/home' or '/about' or anything
                #that you want. Flask uses decorators for this. Again,
                #black box.

def signup():   #Now, everything that you need to do for that particular
                #path of the web app is done under this function.

  up = SignUp() #As we have imported the forms.py module in this module, we
                #create an object of the SignUp class here to be able
                #to access all the entities pertaining to that class.
                #Now, we can send this object to our html to work with
                #fields and labels, manipulate data entered in the fields,
                #use validators, etc.

  return render_template('index.hmtl', up=up)

                #Here, we use the 'render_template' function to provide the
                #name of the html page pertaining to this path that it will
                #search in the 'templates' folder to send to the browser when
                #a user tries to access the path. And the object 'up' that we
                #want to use in the html to access the entities made in the
                #'SignUp' class in 'forms.py' is sent through render_template
                #too.

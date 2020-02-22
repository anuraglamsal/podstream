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

                # Session: Session is the time interval from when a client logs
                # into a server till they log out of it.

                #Now, to start a session, the server needs to send
                #user-specific data to the browser. That data and the secret-
                #key are mashed up using a cryptographic algorithm to
                #create a signature string that makes the data "official". Now,
                #that official data is sent to the browser. Anyone can access
                #it, but to change it, you need the signature string. To
                #figure out the signature string, you need both the secret-key
                #and the data. As the secret-key itself is never sent along
                #with the data, someone who is trying to make changes to some
                #data can't do it until they figure out the secret-key.
                #Thus, a very strong secret-key is configured such that data
                #is not altered without the volition of the actual client.

                #Here, the kind of data we are talking about is especially 
                #the data that is not supposed to be changed; we're not talking
                #about data like a profile picture for example that is supposed
                #to have an option to change. 

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

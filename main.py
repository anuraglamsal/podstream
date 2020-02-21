from flask import Flask, render_template
app = Flask(__name__)

                #__name__ returns the name of the module--here
                #it's "main"--when it is used in some other module.
                #In the module itself however, it returns "__main__".
                #You can use this property to prevent your code
                #from running in other modules i.e. indicating that
                #the particular code is the "main code" like creating
                #the main function in C. In this particular scenario,
                #Flask uses the name of the module to figure out where
                #all the things like templates, static files, etc.
                #of the application are stored. It basically sets up
                #our app. How it does it is black box to me.

@app.route("/")
                #This creates a path. Here particularly, if there is
                #nothing written after '/' in the URL, the function under
                #this is returned. It may be '/home' or '/about' or anything
                #that you want. Flask uses decorators for this. Again,
                #black box.

def signup():   #Now, everything that you need to do for that particular
                #path of the web app is done under this function.

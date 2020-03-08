from main import db
from flask_login import UserMixin

class User(db.Model, UserMixin):

                #Here, we create a class that acts as a "model" of our database
                #i.e. we specify the types of data that we can add on particular
                #columns. For that, we inherit the 'Model' attribute of the
                #'SQLAlchemy' class that works with the 'sqlalchemy' library in
                #some black box way to provides us all the required classes and
                #functions of that library.

                #For 'UserMixin', refer to this:
                #imgur.com/a/Q8X0oLa

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
                #security purposes. They are converted to hashes usingS
                #ideally the latest and greatest hashing algorthims. The reason
                #of doing so is elaborated in the link below:
                #https://imgur.com/a/oRtiLDm

                #'Usernames' should be unique for each user to remove general
                #confusion, prevent identity theft, etc. Thus, this enables
                #passwords for each user to not be unique as the combination of
                #username/email and password turns out to be a good login
                #credential format. But that doesn't get rid of the fact that
                #passwords should be made super difficult to presume.

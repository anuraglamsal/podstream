from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField

                         #Used to import classes that provide fields
                         #to do stuff like text boxes, submit buttons,
                         #check boxes, etc.

                         # 1. StringField is for info that is written
                         # as strings like names and such.

                         # 2. PasswordField is for fields to enter
                         # passwords securely. When you enter something
                         # in a password field, it shows up as bullet
                         # points of sorts.

                         # 3. SubmitField is used to generate the submit
                         # button.

                         # 4. BooleanField is used to generate a
                         # checkbox. If you check it, the value is
                         # True. If it is unchecked, the value is False.
                         # The default value is False i.e unchecked.

from wtforms.validators import DataRequired, Length, Email, EqualTo

                         #Here, we are importing classes for
                         #validation. Validators are used
                         #to set conditions in our fields and
                         #check if they are followed.

                         # 1. DataRequired enables compulsa-
                         # ry requirement of data i.e. you
                         # cannot leave the field empty.

                         # 2. Length enables you to set
                         # maximum and minimum length bounds
                         # for text entered in the field.

                         # 3. The Email validator checks for
                         # accuracy in terms of structure of
                         # the given email.

                         # 4. The EqualTo validator checks if
                         # the value entered in the field is
                         # equal to the value entered in some
                         # other field.

class SignUp(FlaskForm): #In wtforms, all the magic that gives
                         #us the ability to access the data
                         #entered on the fields and submitted
                         #using the submit button is done
                         #internally, which is essentially just
                         #black box. This internal mechanism
                         #is dependent upon us making a unique
                         #class for every form such that each
                         #class consists of its own fields and
                         #buttons. This is why, we cannot use
                         #the same submit button for both login
                         #and sign-up, for example. This
                         #mechanism is also contingent upon us
                         #inheriting the 'FlaskForm' class.

                         #Below, we define the attributes of the
                         #class. We define them straightforwardly
                         #as they are evidently going to be
                         #constant for every user.

    FirstName = StringField('First Name', validators=[DataRequired(),
                                                        Length(min=1, max=50)])

                         #As our signup form should contain
                         #a field to write 'First Name' in
                         #, we create a string field for that
                         #i.e. we create an object of the
                         #class 'StringField' that we imported.
                         #Now, we need to pass the required
                         #values for attributes in that class.

                         #'First Name' inside the brackets is
                         #the label of the string field
                         #typically written to indicate what
                         #you should write in the string field.
                         #We can explicitely use that label
                         #in our html.

                         #Next, we use validators. We pass on
                         #a variable named 'validators'
                         #containing a list of validator classes
                         #required for validation. It is also
                         #an attribute of the StringField class.
                         #I have explained the use of all the
                         #validator classes I've used in the import
                         #section of the code.

    MiddleName = StringField('Middle Name (if any)', validators=[Length(max=50)])

                         #As there might not be a middle name,
                         #data is not compulsarily required. But
                         #we do specify the maximum length of middle
                         #name allowed.

    LastName = StringField('Last Name', validators=[DataRequired(),
                                                    Length(min=1, max=50)])

    email = StringField('Email', validators=[DataRequired(), Email()])

                         #Here, we've used a pre-built
                         #email validator class to check
                         #for the validity of
                         #the entered email.

    Username = StringField('Username', validators=[DataRequired(),
                                                   Length(min=5, max=20)])

    Password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(min=9, max=20)])

                         #Here, we create an object
                         #of the PasswordField class
                         #that we have imported above.
                         #Now, the field is suited to
                         #enter passwords.

    ConfirmPassword = PasswordField('Confirm Password', validators=[
                                                  EqualTo('Password')])

                         #Here, we've used the EqualTo
                         #validator class to check if
                         #the value entered in the
                         #'ConfirmPassword' password field
                         #is equal to the value entered
                         #in the 'Password' password field
                         #that we've made above.

    Submit = SubmitField('Sign Up')

                         #Here, we have used the SubmitField
                         #class to generate the 'Submit'
                         #button used to submit the entered
                         #values and make them ready for
                         #validation.


class Login(FlaskForm):  #Here, we are creating another class that inherits
                         #from the FlaskForm class imported above for our
                         #login form. A login form typically requires a Email
                         #field, a password field and a submit field.
                         #A 'Remember me' tickbox is also typically used.

    email = StringField('Email', validators=[DataRequired(), Email()])
    Password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(min=9, max=20)])
    Remember = BooleanField('Remember me')

                         #Added a 'Remember me' checkbox.
                         #We can use this to automatically
                         #open our logged in page without
                         #actually logging in every time. For
                         #that, we need to write extra code
                         #which we'll do in main and html.

    Submit = SubmitField('Sign In')

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

                                #Used to import classes for the boxes
                                #in forms to write the required info in or
                                #buttons to submit.

                                # 1. StringField is for info that is written
                                # as strings like names and such.

                                # 2. PasswordField is for fields to enter
                                # passwords securely. When you enter something
                                # in a password field, it shows up as bullet
                                # points of sorts.

                                # 3. SubmitField is used to generate the submit
                                # button.

from wtforms.validators import DataRequired, Length, Email, EqualTo

                                        #Here, we are mporting classes for
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

                                        # 4. The EqualTo validtor checks if
                                        # the value entered in the field is
                                        # equal to the value entered in some
                                        # other field.

class SignUp(FlaskForm): #In wtforms, if we want to use the resources
                         #that it provides, we need to create a class that
                         #inherits from the FlaskForm class imported from
                         #the flask_wtf package. That is fundamental to do.
                         #Why? The developers of wtforms know.

    FirstName = StringField('First Name', validators=[DataRequired(),
                                                        Length(min=1, max=50)])

                                    #As our signup form should contain
                                    #a field to write 'First Name' in
                                    #, we create a string field for that.
                                    #For that, we create an object of the
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
                                    #validator classes used in the import
                                    #section of the code.

    MiddleName = StringField('Middle Name (if any)')

                                        #As there might not be a
                                        #middle name, we are not
                                        #using any validators here.

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

    ConfirmPassword = PasswordField('Password', validators=[DataRequired(),
                                                  Length(min=9, max=20),
                                                  EqualTo('Password')])

                                        #Here, we've used the EqualTo
                                        #validator class to check if
                                        #the value entered in the
                                        #'ConfirmPassword' password field
                                        #is equal to the value entered
                                        #in the 'Password' password field
                                        #that we've made above.

    Submit = SubmitField('Sign Up!')

                                        #Here, we have used the SubmitField
                                        #class to generate the 'Submit'
                                        #button used to submit the entered
                                        #values and make them ready for
                                        #validation.

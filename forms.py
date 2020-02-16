from flask_wtf import FlaskForm
from wtforms import StringField #Used to import classes for the boxes
                                #in forms to write the required info in.

                                # 1.) StringField is for info that is written
                                # as strings like Names and such.

from wtforms.validators import DataRequired #importing classes required for
                                            #validation. Validators are used
                                            #to set conditions in our fields and
                                            #check if they are followed.

                                            # 1.) DataRequired enables compulsa-
                                            # ry requirement of data i.e. you
                                            # cannot leave the field empty.

class SignUp(FlaskForm): #In wtforms, if we want to use the resources
                         #that it provides, we need to create a class that
                         #inherits from the FlaskForm class imported from
                         #the flask_wtf package. That is fundamental to do.
                         #Why? The developers of wtforms know.

    FirstName = StringField('First Name', validators=[DataRequired()])
                                          #As our signup form should contain
                                          #a field to write First Name in
                                          #, we create a string field for that.
                                          #For that, we create an object of the
                                          #class 'StringField' that we imported.
                                          #Now, we need to pass the required
                                          #values for attributes in that class.

                                          #'First Name' inside the brackets is
                                          #the label of the String Field
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

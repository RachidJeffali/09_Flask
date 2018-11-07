from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Regexp

class SignupForm(Form):
	regex = (
    '^'            # start line
    '(?=.*\d)'     # must contain one digit from 0-9
    '(?=.*[a-z])'  # must contain one lowercase characters
    '(?=.*[A-Z])'  # must contain one uppercase characters
    '[a-zA-Z\d]'   # permitted characters (alphanumeric only)
    '{6,}'         # length at least 6 chars
    '$'            # end line
)
	first_name = StringField('First name', validators = [DataRequired("Please enter your first name.")])
	last_name = StringField('Last name', validators = [DataRequired("Please enter your last name.")])
	email = StringField('Email', validators = [DataRequired("Please enter your email."), 
		Email("Please enter a valid email.")])
	password = PasswordField('password', validators = [Regexp(regex, message="must contain one digit from 0-9, one lowercase characters, one uppercase characters"),
		DataRequired(), Length(min=6, message = "Password must be 6 characters or more")])
	submit = SubmitField('Sign up')

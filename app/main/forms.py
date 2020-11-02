from flask_wtf import FlaskForm
from wtforms import RadioField, TextAreaField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Required, Email, EqualTo
from wtforms import ValidationError

class UpdateProfile(FlaskForm):
    bio= TextAreaField('Tell us about yourself', validators=[Required()])
    submit= SubmitField("submit here")

class AddBlog(FlaskForm):
    name = TextAreaField('Blog title', validators=[Required()])
    details = TextAreaField('Add your pitch', validators=[Required()])
    submit = SubmitField('Submit')

class CommentsForm(FlaskForm):
    details= TextAreaField("You can add your comment here", validators=[Required()])
    submit=SubmitField('submit')

class UpvoteForm(FlaskForm):
    submit = SubmitField('submit')

class DownvoteForm(FlaskForm):
    submit=SubmitField('submit')
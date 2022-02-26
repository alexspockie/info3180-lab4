from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, Email, Optional

class UploadForm(FlaskForm):
    photo=FileField('File Upload',validators=[FileRequired(),FileAllowed(['jpg','png','Images only!'])])
    
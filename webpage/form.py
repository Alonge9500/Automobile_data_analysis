from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField,DecimalField,SelectField,IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import json

""" 
'width',
 'height',
 'curb_weight',
 'engine_size',
 'highway_mpg',
 'make',
 'body_style',
 'drive_wheels',
 'engine_location',
 'engine_type']
 """
 
with open("webpage/feature_dictionary_encoding.json", "r") as outfile:
    feature_dictionary_encoding = json.load(outfile)

def converttuple(dataa):
  lst = []
  for key,val in dataa.items():
    lst.append((val,key))
  
  return lst

make_list = converttuple(feature_dictionary_encoding['make'])
body_style_dict = converttuple(feature_dictionary_encoding['body_style'])
drive_wheels_dict = converttuple(feature_dictionary_encoding['drive_wheels'])
engine_location_dict = converttuple(feature_dictionary_encoding['engine_location'])
engine_type_dict = converttuple(feature_dictionary_encoding['engine_type'])

class PredictionForm(FlaskForm):
    width = IntegerField('Width', validators=[DataRequired()])
    height = IntegerField('Height', validators=[DataRequired()])
    curb_weight = IntegerField('Curb_weight', validators=[DataRequired()])
    engine_size = IntegerField('Engine_size', validators=[DataRequired()])
    highway_mpg = IntegerField('Highway_mpg', validators=[DataRequired()])
    make = SelectField('Make',choices=make_list,validators=[DataRequired()])
    body_style = SelectField('Body Style',choices=body_style_dict,validators=[DataRequired()])
    drive_wheels = SelectField('Drive Wheels',choices=drive_wheels_dict,validators=[DataRequired()])
    engine_location = SelectField('Engine Location',choices=engine_location_dict,validators=[DataRequired()])
    engine_type_dict = SelectField('Engine Location',choices=engine_type_dict,validators=[DataRequired()])
    
    
    
    submit = SubmitField('Predict')

    # def validate_username(self, username):
    #     user = User.query.filter_by(username=username.data).first()
    #     if user:
    #         raise ValidationError('That user name is taken choose a different one')

    # def validate_email(self, email):
    #     user = User.query.filter_by(email=email.data).first()
    #     if user:
    #         raise ValidationError('User Already Exist')
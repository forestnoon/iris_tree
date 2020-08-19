from flask_wtf import FlaskForm
from wtforms import Form, FloatField, SubmitField, validators, ValidationError

class iris_form(Form):
  sepal_length = FloatField('ガクの長さ（cm）', [validators.InputRequired("all parameters are required!")])
  sepal_width = FloatField('ガクの幅（cm）',[validators.InputRequired("all parameters are required!")])
  petal_length = FloatField('花弁の長さ（cm）',[validators.InputRequired("all parameters are required!")])
  petal_width = FloatField('花弁の幅（cm）',[validators.InputRequired("all parameters are required!")])
  submit = SubmitField('予測する')
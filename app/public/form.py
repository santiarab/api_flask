from flask_wtf import FlaskForm
from sqlalchemy import Integer, Boolean
from wtforms import StringField, SubmitField
from wtforms.fields.datetime import DateField
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import BooleanField
from wtforms.validators import DataRequired, Length, Optional


class CreateTask(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=256)])
    description = StringField('Description', validators=[Optional()])
    due_date = DateField('Due Date', format='%Y-%m-%d',validators=[Optional()])
    submit = SubmitField('Create Task')

class GetTaskByTitle(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=256)])
    submit = SubmitField('Get Task')

class GetTaskById(FlaskForm):
    id = IntegerField('Id', validators=[DataRequired()])
    submit = SubmitField('Get Task')

class UpdateTask(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=256)])
    description = StringField('Description', validators=[Optional()])
    due_date = DateField('Due Date', format='%Y-%m-%d', validators=[Optional()])
    status = BooleanField('Status', validators=[Optional()])
    submit = SubmitField('Update Task')
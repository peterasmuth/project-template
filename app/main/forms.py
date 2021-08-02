from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, HiddenField, IntegerField, SelectField, DecimalField, TextAreaField
from wtforms.fields.html5 import DateTimeField, DateField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Optional, Length, InputRequired
from app.models import Location, Game


class CreateLocation(FlaskForm):
	user_id = HiddenField('user_id')
	location_name = StringField('Location Name', validators=[DataRequired()])
	submit = SubmitField('Create Location')

	def validate_location_name(self, location_name):
		location = Location.query.filter_by(user_id = self.user_id.data, name = self.location_name.data).first()
		if location is not None:
			raise ValidationError('Location with this name already exists')


class CreateGame(FlaskForm):
	user_id = HiddenField('user_id')
	format = SelectField('Game Format', choices=[('Hold''em','Hold''em'), ('Omaha','Omaha'), ('7-card Stud','7-card Stud')])
	limit = SelectField('Limit Type', choices = [('No-limit','No-limit'), ('Pot-Limit','Pot-limit'), ('Fixed Limit','Fixed Limit')])
	small_blind = IntegerField('Small Blind', validators = [DataRequired()])
	big_blind = IntegerField('Big Blind', validators = [DataRequired()])
	straddle = IntegerField('Straddle')
	ante = IntegerField('Ante')
	submit = SubmitField('Create Game Type')


class CreateSession(FlaskForm):
	user_id = HiddenField('user_id')
	buy_in = IntegerField('Buy-in', validators = [DataRequired()])
	cash_out = IntegerField('Cashout', validators = [InputRequired()])
	date = DateField('Start Time', validators = [DataRequired()])
	duration = DecimalField('Duration', validators = [DataRequired()])
	location = SelectField('Session Location', coerce = int, validators = [DataRequired()])
	game_type = SelectField('Session Game Type', coerce = int, validators = [DataRequired()])
	submit = SubmitField('Create Session')


class DashboardFilters(FlaskForm):
	user_id = HiddenField('user_id')
	start_date = DateField('Start Date', validators = [Optional()])
	end_date = DateField('End Date', validators = [Optional()])
	location = SelectField('Location', coerce = int, validators = [Optional()])
	game_type = SelectField('Game Type', coerce = int, validators = [Optional()])
	submit = SubmitField('Report')

	def validate_end_date(self, end_date):
		if self.start_date.data and self.end_date.data:
			if self.start_date.data > end_date.data:
				raise ValidationError('End date is before start date')


class CreateNote(FlaskForm):
	user_id = HiddenField('user_id')
	date = DateField('Date', validators = [DataRequired()])
	subject = StringField('Subject', validators = [DataRequired(), Length(max = 50)])
	note_text = TextAreaField('Note Text', render_kw={'class': 'form-control', 'rows': 7}, validators = [DataRequired(), Length(max = 500)])
	submit = SubmitField('Save')


class CreatePlayer(FlaskForm):
	user_id = HiddenField('user_id')
	first_name = StringField('First Name', validators = [DataRequired(), Length(max = 50)])
	last_name = StringField('Last Name', validators = [Length(max = 50)])
	nick_name = StringField('Nick Name', validators = [Length(max = 50)])
	bio = TextAreaField('Player Bio', validators = [DataRequired(), Length(max = 500)])
	submit = SubmitField('Save')

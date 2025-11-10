import pandas as pd  # type: ignore
from flask_wtf import FlaskForm #type: ignore
data=pd.read_csv('matches.csv')

from wtforms import SelectField,TimeField,IntegerField,SubmitField # type: ignore
from wtforms.validators import DataRequired # type: ignore


class MatchForm(FlaskForm):
    time=TimeField(
        label='Match Time',
        format='%H:%M',
        validators=[DataRequired()],
        
        )
    comp=SelectField(
        label='Competition',
        choices=data['comp'].unique().tolist(),
        validators=[DataRequired()]
    )
    round=SelectField(
        label='Round',
        choices=data['round'].unique().tolist(),
        validators=[DataRequired()]
    )
    day=SelectField(
        label = 'day',
        choices=data['day'].unique().tolist(),
        validators=[DataRequired()]
    )
    venue=SelectField(
        label='Venue',
        choices=data['venue'].unique().tolist(),
        validators=[DataRequired()]
    )
    opponent=SelectField(
        label='Opponent',
        choices=data['opponent'].unique().tolist(),
        validators=[DataRequired()]
    )
    captain=SelectField(
        label='Captain',
        choices=data['captain'].unique().tolist(),
        validators=[DataRequired()]
    )
    referee=SelectField(
        label='Referee',
        choices=data['referee'].unique().tolist(),
        validators=[DataRequired()]
    )
    match_report=SelectField(
        label='Match Report',
        choices=data['match report'].unique().tolist(),
        validators=[DataRequired()]
    )
    sot=IntegerField(
        label='Shots on Target',
        validators=[DataRequired()]

    )
    fk=IntegerField(
        label='Free Kicks',
        validators=[DataRequired()]
    )
    pk=IntegerField(
        label='Penalty Kicks',
        validators=[DataRequired()]
    )
    pkatt=IntegerField(
        label="Penalty kick attempts",
        validators=[DataRequired()]
    )
    season=SelectField(
        label='Season',
        choices=data['season'].unique().tolist(),
        validators=[DataRequired()]
    )
    team=SelectField(
        label='Team',
        choices=data['team'].unique().tolist(),
        validators=[DataRequired()]
    )
    Submit=SubmitField('Predict')
""" time	comp	round		venue	opponent
captain	referee	match report	sot	fk	pk	
pkatt	season	team"""
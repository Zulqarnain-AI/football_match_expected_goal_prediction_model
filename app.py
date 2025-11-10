from flask import Flask, render_template, url_for
from forms import MatchForm
import pandas as pd
import joblib

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

model = joblib.load('model.joblib')

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    form = MatchForm()
    if form.validate_on_submit():

        
        x_new = pd.DataFrame({
            'time': [form.time.data.strftime('%H:%M')],
            'comp': [form.comp.data],
            'round': [form.round.data],
            'day': [form.day.data],
            'venue': [form.venue.data],
            'opponent': [form.opponent.data],
            'captain': [form.captain.data],
            'referee': [form.referee.data],
            'match report': [form.match_report.data],
            'sot': [form.sot.data],
            'fk': [form.fk.data],
            'pk': [form.pk.data],
            'pkatt': [form.pkatt.data],
            'season': [form.season.data],
            'team': [form.team.data],
            'xg_roll_5': [1.2],
            'poss_roll_5': [1.2],
            'sh_roll_5': [1.2],
            'xg_roll_10': [1.5],
            'poss_roll_10': [1.5],
            'sh_roll_10': [1.5]
        })
        # Predict
        prediction = model.predict(x_new)[0]
        return f"Predicted Expected Goals: {prediction:.2f}"

    return render_template('predict.html', title='Predict Match', form=form)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)


# Load model
with open('model2.pkl', 'rb') as file:
    model = pickle.load(file)


# Features used during training
features = [
    'hour',
    'minute',
    'day',
    'month',
    'year',
    'dayofweek',
    'dayofyear'
]


# Feature engineering
def create_f(df):

    df = df.copy()

    df['hour'] = df.index.hour
    df['minute'] = df.index.minute
    df['day'] = df.index.day
    df['month'] = df.index.month
    df['year'] = df.index.year
    df['dayofweek'] = df.index.dayofweek
    df['dayofyear'] = df.index.dayofyear
    df['weekofyear'] = df.index.isocalendar().week

    return df


# Home page
@app.route('/', methods=['GET', 'POST'])
def home():

    prediction = None

    if request.method == 'POST':

        date = request.form.get('date')
        time = request.form.get('time')

        print("FORM DATA:", request.form)
        print("DATE:", date)
        print("TIME:", time)
        datetime_value = pd.to_datetime(
            date + ' ' + time
        )

        new = pd.DataFrame(
            index=[datetime_value]
        )

        new = create_f(new)

        prediction = model.predict(
            new[features]
        )[0]

        prediction = round(prediction, 2)

    return render_template(
        'index.html',
        prediction=prediction
    )


if __name__ == '__main__':
    app.run(debug=True)
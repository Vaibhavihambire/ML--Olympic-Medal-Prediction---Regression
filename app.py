import joblib
from flask import Flask, render_template, request

app = Flask(__name__)

# Load model
model = joblib.load('olympic_medal_predictor.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get inputs
    num_athletes = float(request.form['athletes'])
    prev_medals = float(request.form['prev_medals'])

    # Predict
    prediction = model.predict([[num_athletes, prev_medals]])
    output = round(prediction[0], 2)

    return render_template('result.html', prediction=output)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request

from models import run_prediction
from template import convert_to_template

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/predict', methods=['GET'])
def predict():
    return run_prediction({
        "snowfall": request.args.get("snowfall"),
        "windspeed": request.args.get("windspeed"),
        "temperature": request.args.get("temperature"),
        "visibility": request.args.get("visibility")
    })


@app.route('/results')
def results():
    template = convert_to_template(run_prediction({
        "snowfall": request.args.get("snowfall"),
        "windspeed": request.args.get("windspeed"),
        "temperature": request.args.get("temperature"),
        "visibility": request.args.get("visibility")
    }))
    return render_template('results.html', results=template)


if __name__ == '__main__':
    app.run()

from flask import Flask, render_template, request

from models import run_prediction
from template import convert_trip_to_template, convert_model_to_template

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
    model_results = run_prediction({
        "snowfall": request.args.get("snowfall"),
        "windspeed": request.args.get("windspeed"),
        "temperature": request.args.get("temperature"),
        "visibility": request.args.get("visibility")
    })
    model_results_template = convert_model_to_template(model_results)
    trip_times_template = convert_trip_to_template(model_results, request.args.get("cartrip"),
                                                   request.args.get("mbtatrip"))
    return render_template('results.html', results=model_results_template, times=trip_times_template)


if __name__ == '__main__':
    app.run()

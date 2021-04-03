import pickle

import numpy as np
import sklearn  # for models load

with open('quantile_models.pkl', 'rb') as f:
    quantile_models = pickle.load(f)

with open('quantile_models_no_vis.pkl', 'rb') as f:
    quantile_models_no_vis = pickle.load(f)


def get_bounds(x, model):
    low = model["lower_model"].predict(x)[0]
    high = model["upper_model"].predict(x)[0]
    return low, high


def run_prediction(inputs):
    results = {}
    if inputs["visibility"] is None or inputs["visibility"] == '':
        x = np.array([inputs["snowfall"], inputs["windspeed"], inputs["temperature"]])
        for model in quantile_models:
            results[model] = get_bounds(x.reshape(1, -1), quantile_models_no_vis[model])
    else:
        x = np.array([inputs["snowfall"], inputs["windspeed"], inputs["temperature"], inputs["visibility"]])
        for model in quantile_models:
            results[model] = get_bounds(x.reshape(1, -1), quantile_models[model])
    return results

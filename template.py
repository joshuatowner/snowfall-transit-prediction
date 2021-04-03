display_names = {
    'traffic_speed': 'Car speed',
    'traffic_accidents': 'Car accident rate',
    'mbta_speed': 'MBTA speed'
}


def convert_to_template(model_results):
    return [{
        'display_name': display_names[model],
        'low_percentage': "%.0f" % (model_results[model][0] * 100),
        'high_percentage': "%.0f" % (model_results[model][1] * 100)
    } for model in model_results]

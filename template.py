display_names = {
    'traffic_speed': 'Car speed',
    'traffic_accidents': 'Car accident rate',
    'mbta_speed': 'MBTA speed'
}


def convert_model_to_template(model_results):
    return [{
        'display_name': display_names[model],
        'low_percentage': "%.0f" % (model_results[model][0] * 100),
        'high_percentage': "%.0f" % (model_results[model][1] * 100)
    } for model in model_results]


def trip_result_template(name, model, trip_time):
    results = [
        model[0] ** -1 * trip_time,
        model[1] ** -1 * trip_time
    ]
    low_value = min(results)
    high_value = max(results)
    return {
        'low_{}_trip_time'.format(name): "%.2f" % low_value,
        'high_{}_trip_time'.format(name): "%.2f" % high_value
    }


def convert_trip_to_template(model_results, cartrip, mbtatrip):
    show_mbta = mbtatrip is not None and mbtatrip != ''
    show_car = cartrip is not None and cartrip != ''
    car_results = model_results['traffic_speed']
    mbta_results = model_results['mbta_speed']
    template = {}
    if show_car:
        template = trip_result_template('car', car_results, float(cartrip)) | template
    if show_mbta:
        template = trip_result_template('mbta', mbta_results, float(mbtatrip)) | template
    return template

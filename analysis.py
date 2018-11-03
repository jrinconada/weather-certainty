
def rain_certainty(days, params=[], references=[], thresholds=[]):
    # Error check
    if len(params) != len(thresholds):
        print('Params and thresholds must be the same length')
        return

    rain = 'totalprecip_mm'
    week_certainty = [0.0] * 7
    samples = [0] * 7 # Actual number of samples being processed

    for day in days: # For every day in the data
        for i in range(7): # For every day in the 7 day forecast
            forecast = days[day][i]
            if filter(forecast, params, references, thresholds):
                continue
            if rain in forecast and rain in days[day][-1]: # Make sure there is rain data
                was_rainy = days[day][-1][rain] != 0 # It was rainy (last day is the actual weather)
                # Forecast was correct
                if (was_rainy and (forecast[rain] != 0)) or (not was_rainy and (forecast[rain] == 0)):
                    week_certainty[i] += 1
                samples[i] += 1
    # Divide correct hits by number of samples to compute certainty
    for i in range(7):
        if samples[i] != 0:
            week_certainty[i] = week_certainty[i] / samples[i]
    return week_certainty

# Returns True if forecast is between the thresholds and should be included
def filter(forecast, params, references, thresholds):
    if not params:
        return False
    for param in params:
        if abs(references[params] - forecast[param]) > thresholds:
            return False
    return True

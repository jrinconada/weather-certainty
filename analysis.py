
def rain_certainty(days):
    rain = 'totalprecip_mm'
    week_certainty = [0.0] * 7
    samples = 0 # Actual number of samples being processed

    for day in days: # For every day in the data
        for i in range(7): # For every day in the 7 day forecast
            forecast = days[day][i]
            if rain in forecast and rain in days[day][-1]: # Make sure there is rain data
                was_rainy = days[day][-1][rain] != 0 # It was rainy (last day is the actual weather)
                # Forecast was correct
                if (was_rainy and (forecast[rain] != 0)) or (not was_rainy and (forecast[rain] == 0)):
                    week_certainty[i] += 1
                samples += 1
    # Divide correct hits by number of samples to compute certainty
    return [i / samples for i in week_certainty]

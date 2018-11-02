import weather  # Weather API for updating data
import date     # Date formatting
import storage  # File storage
import display  # Printing and plotting data

max_days = 7
location = 'Madrid'

# Read data from file
def read_data():
    days = storage.read(location)
    if type(days) is not dict: # If there is no data yet, create a empty dictionary
        days = {}
    return days

# Get forecast for the next 7 days
def update_data(days):
    forecasts = weather.forecast_in(location, max_days).json()
    for i in range(max_days):
        day = date.add(i)
        if day not in days: # If there is no day for this day, create it
            days[day] = [{} for j in range(max_days)]

        days[day][-(i+1)] = forecasts['forecast']['forecastday'][i]['day']
    return days

# Save forecasts in file
def save_data(days):
    storage.write(location, days)

days = read_data()
display.show(days, 'avgtemp_c')
display.show_for(days, '2018-11-08', 'avgtemp_c')
display.graph(days, '2018-11-08', 'avgtemp_c')

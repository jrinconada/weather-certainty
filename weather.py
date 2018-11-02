import requests
import date

base_url = 'https://api.apixu.com/v1/'
current_url = base_url + 'current.json'
forecast_url = base_url + 'forecast.json'
history_url = base_url + 'history.json'
key = '0e56cee34bc44a168ea192404183110'
params = {'key': key}

def current():
    return current_in('Madrid')

def current_in(location):
    params['q'] = location
    return requests.get(current_url, params=params)

def forecast():
    return forecast_in('Madrid', '7')

def forecast_in(location, days):
    params['q'] = location
    params['days'] = days
    return requests.get(forecast_url, params=params)

def history():
    return history_in('Madrid', date.now())

def history_in(location, date):
    params['q'] = location
    params['dt'] = date # Ex: '2018-11-01'
    return requests.get(history_url, params=params)

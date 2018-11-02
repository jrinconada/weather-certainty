import datetime

def format(date):
    return date.strftime('%Y-%m-%d')

def from_str(date):
    return datetime.datetime.strptime(date, '%Y-%m-%d')

def now():
    return format(datetime.datetime.now())

def add(days):
    return format(datetime.datetime.now() + datetime.timedelta(days=days))

def add_to(date, days):
    return format(date + datetime.timedelta(days=days))

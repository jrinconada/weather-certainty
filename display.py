import matplotlib.pyplot as plt
import date

def show(days, what):
    for day in days:
        print(day, end=': ')
        for forecast in days[day]:
            if what in forecast:
                print(forecast[what], end=' ')
        print('')

def show_for(days, day, what):
    if day not in days:
        print(day, 'not found')
        return

    print(day)
    for forecast in days[day]:
        if what in forecast:
            print('\t', what, end=' ')
            print(forecast[what])

def graph(days, day, what):
    if day not in days:
        print(day, 'not found')
        return

    # Populate x with the previous dates
    first_date = date.from_str(day)
    x_labels = [date.add_to(first_date, -i) for i in reversed(range(7))]
    x = range(7)

    # Populate y with the values of the field forecast
    y = [0.0 for x in range(7)]
    for i in range(7):
        forecast = days[day][i]
        print(i, forecast)
        if what in forecast:
            y[i] = float(forecast[what])

    # Plot it
    plt.title(what + ' predictions for ' + day)
    plt.plot(x, y)
    plt.xticks(x, x_labels, rotation=45)
    plt.show()

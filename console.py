
def menu():
    print('')
    print('--- Weather certainty ---')
    print('Type your command (or just the first letter):')
    print('- menu   \t: Show menu again')
    print('- update \t: Update data')
    print('- show   \t: Show data')
    print('- compute\t: Compute certainty')
    print('- params \t: Show parameter names')
    print('- quit   \t: Exit the programm')

# Returns the first letter in lowercase
def command():
    print('')
    commands = input('> ').split(' ')
    main = commands[0][:1].lower()
    # Error check
    if main == 's' and len(commands) < 2:
        show_help()
        return '-', '', ''
    if len(commands) < 2: # command without params
        return main, '', ''
    elif len(commands) < 3: # command with param
        return main, commands[1], ''
    else: # command with param and date
        return main, commands[1], commands[2]

def show_help():
    print('show command must have a weather parameter.')
    print('Examples: ')
    print('\tshow avgtemp_c')
    print('\tshow avgtemp_c 2018-11-04')

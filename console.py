
def menu():
    print('')
    print('--- Weather certainty ---')
    print('Type your command (or just the first letter):')
    print('- menu   \t: Show menu again')
    print('- update \t: Update data')
    print('- show   \t: Show data')
    print('- compute\t: Compute certainty')
    print('- params \t: Show parameter names')
    print('- quit   \t: Exit the programme')

# Returns the first letter in lowercase
def command():
    print('')
    return input('> ')[:1].lower()

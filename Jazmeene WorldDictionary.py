World_map = {
    'SCE': {
        'NAME': "Sports complex entrance",
        "DESCRIPTION": "This is a building with two doors. On the west side of the building there is an entrance door. "
                       "On the south side there is an exit. ",
        'PATHS': {
            'EAST': 'FIELDONE',

        }
    },
    'FIELDONE': {
        'NAME': 'SOUTH OF HOUSE',
        'DESCRIPTION': "INSERT DESCRIPTION HERE",
        'PATH': {

            'SOUTH': 'WESTHOUSE'
           }
      }
}
current_node = World_map['WESTHOUSE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = World_map[name_of_node]
        except KeyError:
            print("You cannot go this way")
    else:

        print('Command not Recognized')
        print()








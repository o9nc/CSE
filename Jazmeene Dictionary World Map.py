world_map = {
    'WESTHOUSE': {
        'NAME': "West of House",
        'DESCRIPTION': "You are west of a white house",
        'PATHS': {
            'NORTH': 'NORTHHOUSE',
            'SOUTH': 'SOUTHHOUSE'
        }
    },
    'NORTHHOUSE': {
        'NAME': 'North of House',
        'DESCRIPTION': "Insert Description here"
        'PATHS': {
        'SOUTH': 'WESTHOUSE',
           }
      }
}

current_node = world_map['WESTHOUSE']
print(current_node)

while True:
    command = input('>_')
if command == 'quit':
    quit(0)
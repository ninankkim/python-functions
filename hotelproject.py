hotel = {
     '101': {
        'guest': {
            'name': 'Elliot Alderson',
            'phone': 8675309
        }
    },
    '102': {},
    '103': {},
    '104': {
        'guest': {
            'name': 'Darlene Alderson',
            'phone': 4567890
         }
    },
    '105': {},
}

#first small
def is_vacant (hotel, room):
    guest = 0
    for key in hotel.keys():
        if key == 'guest':
            guest += 1
    print(hotel[room])
    if 'guest' in hotel[room]:
        print ("The room is not vacant.")
        return False
    else: 
        print ("The room is vacant.")
        return True
is_vacant(hotel, '102')

#assign a person
new_guest = 'Issa Rae'
guest_phone = '12345678'
def check_in (room, guest_dictionary):
    if is_vacant(hotel, room) == True:
        hotel[room] = guest_dictionary
        print(f'{guest_dictionary} is checked into room number {room}.')
    else:
        print ('The room is not available.')
        return False
check_in('102', new_guest)

#return person dictionary in that room
def check_out(room):
    #print(hotel)
    if is_vacant(hotel, room) == True:
        person = hotel[room]
        hotel[room] = {}
        print(f'{person} just checked out.')
        print(hotel)
    else:
        print('The room is empty, nobody needs to be checked out.')
        return False 
check_out('102')












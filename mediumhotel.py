hotel=[    
    {
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
    },

    {
        '101': {
            'guest': {
                'name': 'Justin Bieber',
                'phone': 1234567
            }
        },
        '102': {},
        '103': {},
        '104': {
            'guest': {
                'name': 'Hailey Baldwin',
                'phone': 7654321
            }
        },
        '105': {},
    },

    {
        '101': {
            'guest': {
                'name': 'The Weeknd',
                'phone': 9876543
            }
        },
        '102': {},
        '103': {},
        '104': {
            'guest': {
                'name': 'Selena Gomez',
                'phone': 2345678
            }
        },
        '105': {},
    }
]
def print_room_status ():
    #print(hotel)
    for guest_list1 in hotel:
       # print(guest_list1)

       for guest_list1rooms in guest_list1.keys():
           #print(guest_list1rooms,guest_list1[guest_list1rooms])
            if guest_list1[guest_list1rooms]: 
                print(guest_list1rooms,guest_list1[guest_list1rooms]['guest'])
            else:
                print(f'The {guest_list1rooms} is empty')

while True:
    option = input ('''What would you like to choose from the following menu?
1 Print hotel room status
2 Check in customer 
3 Check out customer 
4 Quit\n''')
    if option == '1':
        print_room_status()

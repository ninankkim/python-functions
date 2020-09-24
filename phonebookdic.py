phonebook_dict = {
  'Alice': {
    'phonenumber' : '678-575-9449',
    'color' : 'blue'

  },
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'

  
}
person = phonebook_dict['Elizabeth']
print(person)

phonebook_dict['Kareem'] = '938-489-1234'
print(phonebook_dict)

del phonebook_dict['Alice']
print(phonebook_dict)



phonebook_dict['Bob'] = '968-345-2345'
print(phonebook_dict)


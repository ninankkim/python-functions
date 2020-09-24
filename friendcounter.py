ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ],
}

def countFriends(dict):
    count = 0
    for friend in dict['friends']:
        count = count + 1
    dict['The friend count is: '] = count

    return dict 
print(countFriends(ramit))
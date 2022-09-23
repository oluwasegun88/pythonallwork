users = [
    {
     'name': 'Hadiza',
     'age': 21,
     'gender': 'Female',
     'username':'deezah',
     'is_verified':True,
     'tweets':[
        {'content':'PO for President','likes': 450, 'retweets':233},
        {'content':'Atiku is our man','likes': 4, 'retweets': 2},
        ]
    },

{
     'name': 'James',
     'age': 25,
     'gender': 'Male',
     'username':'jamesbond',
     'is_verified':False,
     'tweets':[
        {'content':'Love is life','likes': 40, 'retweets':23},
        {'content':'Atiku is a goat','likes': 300, 'retweets': 250},
    ]
    },

{
     'name': 'Racheal',
     'age': 20,
     'gender': 'Female',
     'username':'betty',
     'is_verified':True,
     'tweets':[
        {'content':'Tinubu for President','likes': 750, 'retweets':500},
        {'content':'Atiku is our man','likes': 4, 'retweets': 1},
    ]
    },

{
     'name': 'Elijah',
     'age': 23,
     'gender': 'Male',
     'username':'fireman',
     'is_verified':True,
     'tweets':[
        {'content':'PO for President','likes': 450, 'retweets':233},
        {'content':'Atiku is our man','likes': 4, 'retweets': 2},
    ]
    },

{
     'name': 'Dorris',
     'age': 31,
     'gender': 'Female',
     'username':'mama',
     'is_verified':True,
     'tweets':[
        {'content':'Chinamada','likes': 60, 'retweets':43},
        {'content':'Chukwudebelu Orji','likes': 54, 'retweets': 22},
    ]
    },

{
     'name': 'Jacob',
     'age': 47,
     'gender': 'Female',
     'username':'elder',
     'is_verified':True,
     'tweets':[
        {'content':'Writing is fun','likes': 70, 'retweets':7},
        {'content':'Study reward','likes': 90, 'retweets': 50},
    ]
    },

{
     'name': 'Derrick',
     'age': 29,
     'gender': 'Male',
     'username':'olonsho',
     'is_verified':True,
     'tweets':[
        {'content':'Cool is cool','likes': 40, 'retweets':3},
        {'content':'Code is cool','likes': 10, 'retweets': 5},
    ]
    },

{
     'name': 'Mubarak',
     'age': 47,
     'gender': 'Male',
     'username':'whistle',
     'is_verified':True,
     'tweets':[
         ]
    },

{
     'name': 'Ibrahim',
     'age': 31,
     'gender': 'Female',
     'username':'ibro',
     'is_verified':True,
     'tweets':[
        {'content':'Life is cool','likes': 50, 'retweets':33},
        {'content':'I love Jesus','likes': 100, 'retweets': 79},
    ]
    },

    ]

no_of_users = len(users)
usernames = {user['username'] for user in users}
female_users = [user['name'] for user in users if user['gender'] == 'Female']
inactive_users = [users for users in users if len(users['tweets']) == 0]
name_and_age = [{'name': user['name'],'age': user['age']} for user in users]
average_age_of_users = round(sum(user['age']  for user in users) / len(users))
print(usernames)
print(female_users)
print(inactive_users)
print(name_and_age)
print(average_age_of_users)

print(max(users,key=lambda x:x['age']))
print(max(users,key=lambda x: len(x['tweets'])))
print(max([user['age'] for user in users]))
print(sum([user['age'] for user in users]) /len(users))


print(any(user['is_verified'] for user in users))
print(all(user['is_verified'] for user in users))

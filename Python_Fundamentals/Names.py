#part 1- create a program that returns first & last names only from dictionary

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

for x in students:
    print x["first_name"], x["last_name"]


#part 2- create a program that prints students & instructors 
#numbered & number of char in name

users = {
    'Students': [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
       {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
    'Instructors': [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
}

for key in users:
    numID = 1
    print key
    for user in users[key]:
        print numID, "-", user["first_name"], user["last_name"], "-", (len(user["first_name"]) + len(user["last_name"]))
        numID += 1
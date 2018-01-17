#create dictionary with info about myself, include: name, age, country of birth, fave lang

my_info = {
    "name": "Nicki Hays",
    "age": 30,
    "country of birth": "United States",
    "favorite language": "Python"
}

def myInfo(x):
    for key, data in x.items():
        print "My", key, "is", data

print myInfo(my_info)
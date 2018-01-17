#create function that takes 2 lists & creates single dictionary
#1st list contains keys & 2nd list contains values

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
fave_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(list1, list2):
    new_dict = dict(zip(list1, list2))
    return new_dict

print make_dict(name, fave_animal)



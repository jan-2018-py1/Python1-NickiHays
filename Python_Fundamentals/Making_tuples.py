#write function that takes dictionary & returns list of tuples
#first tuple = key, second tuple = value

my_dict = {
    "Speros": "(555) 555-5555",
    "Michael": "(999) 999-9999",
    "Jay": "(777) 777-7777"
}

def dictTuple(x):
    print x.items()

print dictTuple(my_dict)
#part 1- create function draw_stars() that takes a list of numbers & printss *


x = [4,6,1,3,5,7,25]

def draw_stars(list):
    for i in range(len(list)):
        print (list[i] * '*') 

print draw_stars(x)


#part 2- modify part 1 function to allow list to contain integers & strings
#when string is passed display first letter of string, may use .lower()

a = [4,"Tom",1,"Michael",5,7,"Jimmy Smith"]

def draw_stars(list):
    for i in list:
        if isinstance(i, str):
            print (i[0].lower() * len(i))
        elif isinstance(i, int):
            print (i * '*')
        else:
            continue

print draw_stars(a)
#Given a value, test the value for its type
#1- for int if >= 100 print "That's a big number!"; if <100 print "That's a small number"
#2- for str if >= 50 characters print "Long sentence"; if < 50 char print "Short sentence"
#3- for list if >= 10 print "Big list!"; if , 10 print "Short list"

#Test using these examples
sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name', 'address', 'phone number', 'social security number']


def typeFilter(value):
    if isinstance(value, int) and value >= 100:#checking if integer is greater or equal to 100
        print "That's a big number!"
    elif isinstance(value, int) and value < 100:#checking if integer is less than 100
        print "That's a small number."
    elif isinstance(value, str) and len(value) >= 50:#checking if string has 50 or more characters
        print "Long sentence."
    elif isinstance(value, str) and len(value) < 50:#checking if string has less than 50 characters
        print "Short sentence."
    elif isinstance(value, list) and len(value) >= 10:#checking if list length is greater or equal to 10
        print "Big list!"
    elif isinstance(value, list) and len(value) < 10:#checking if list length is less than 10
        print "Short list." 


#testing code
print typeFilter(sI)
print typeFilter(mI)
print typeFilter(bI)
print typeFilter(eI)
print typeFilter(spI)
print typeFilter(sS)
print typeFilter(mS)
print typeFilter(bS)
print typeFilter(eS)
print typeFilter(aL)
print typeFilter(mL)
print typeFilter(lL)
print typeFilter(eL)
print typeFilter(spL)
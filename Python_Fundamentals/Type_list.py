#Write program that takes a list & prints a message for each element in the list based on data type
#test data type for each item
#if str turn into a new string
#if num add to a running sum
#print str, num and analysis of what the list contains
#if only one type print the type
#if two types print mixed


#Examples to use:
l = ['magical unicorns', 19,'hello',98.98,'world']

x = [2,3,1,7,4,12]

y = ['magical','unicorns']

def typeList(value):
    intType = True
    string = ""
    num = 0
    for key in value:
        if isinstance(key, str):
            string += key + " "
            intType = False
        elif isinstance(key,int):
            num += key
        elif isinstance(key, float):
            num += key
    if num > 0 and intType == True:
        print "This list is only numbers."
        print "The sum is:", num
    elif num == 0 and intType == False:
        print "This list is strings."
        print "Their contents are:", string
    else:
        print "This list is mixed."
        print "The string is:", string
        print "The sum of the numbers is:", num

print typeList(l)
print typeList(x)
print typeList(y)
print typeList([11, 'Connor', 16, 'little', 16, 'man'])
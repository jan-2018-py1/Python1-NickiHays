#write program that takes a list of strings and a string with a single character, &
#print a new list of the strings that contain that character

#Example
word_list = ['hello', 'world', 'my', 'name', 'is', 'Anna']
char = 'o'

dif_list = ['this', 'is', 'to', 'find', 'characters']
char1 = 'i'
char2 = 't'

def charFind(stringList, val):
    newList = []
    for a in stringList:
        if val in a:
            newList.append(a)
    print newList


print charFind(word_list, char)
print charFind(dif_list, char1)
print charFind(dif_list, char2)
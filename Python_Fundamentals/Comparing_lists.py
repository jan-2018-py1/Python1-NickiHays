#compare two lists & print message based on if the lists are identical or not
#if identical print "The lists are the same."
#if different print "The lists are not the same."

#examples to test
list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

list_a = [1,2,5,6,5]
list_b = [1,2,5,6,5,3]

list_three = [1,2,5,6,5,16]
list_four = [1,2,5,6,5]

list_c = ['celery', 'carrots', 'bread', 'milk']
list_d = ['celery', 'carrots', 'bread', 'cream']



def compare(list1, list2):    
    if list1 == list2:
        print "The lists are the same"
    else:
        print "The lists are not the same"

print compare(list_one, list_two)
print compare(list_a, list_b)
print compare(list_three, list_four)
print compare(list_c, list_d)


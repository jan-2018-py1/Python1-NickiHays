#odd/even function
#create function that counts from 1 - 2000
#print the number & specify if it's odd or even

def even_odd():
    for x in range(1, 2001):
        if (x % 2 == 0):
            print "Number is", x, "This is an even number"
        elif (x % 2 == 1):
            print"Number is", x, "This is an odd number"
         
print even_odd()


#multiply function
#iterate through each number in a list
#print a list where each value has been multiplied by 5

a = [2,4,10,16]

def multiply(arr, num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr

print multiply(a,5)


#write function that takes multiply function as an argument
#print multiplied list as a 2-dim list
#each internal list should contain the 1's * the num in original list

#example
arr1 = [2,4,10,16]
def multiply(arr, num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr
arr2 = multiply(arr1,5)
print arr2

def layered_multiples(arr):
    newArr = []
    for x in range(len(arr)):
        a = []
        for y in range(0,arr[x]):
            a.append(1)
        newArr.append(a)
    return newArr
b = layered_multiples(multiply([2,4,5],3))
print b
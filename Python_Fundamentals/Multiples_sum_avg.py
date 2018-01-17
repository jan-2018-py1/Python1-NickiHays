#print all odd numberts from 1 to 1,000 using for loop
for sum in range(1, 1000):#sets the range from 1 to 1000
    if sum % 2 == 1:#states that if the number has a remainder of 1 when divided by 2 then to print that number, a number with a remainder of 1 would be an odd number
        print sum


#print all multiples of 5 from 5 to 1,000,000
for i in range(5, 1000001):#sets the range from 5 to 1,000,001 so that it will still print 1,000,000
    if (i % 5 == 0):#states that if the number in the range is completely divisible by 5 then print that number
        print i

#print sum of all the values in the list
a = [1, 2, 5, 10, 255, 3] 
sum = 0
for i in range(0, len(a)):#states the range is 0 to the length of a (6)
    sum += a[i] #adds the sum to each number in a (ex the first one is 0+1 making sum = 1 for the next one)
    print "accumulative sum is:", sum #prints each accumulative sum from one number to the next
print "total sum is:", sum #prints the sum of all the numbers together

#print average of the values in the list
x = [1, 2, 5, 10, 255, 3]
avg = sum(x)/len(x)#takes the sum of x divided by the length of x to get the average
print avg
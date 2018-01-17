#write a function to simulate tossing a coin 5000 times
#print how many times heads/tails appears cumulatively

def coinToss():
    import random
    heads = 0
    tails = 0
    for x in range(1,5001):
        flip = round(random.random())
        if (flip == 0):
            heads += 1
            tails += 0
            print "Attempt #", x, "Throwing a coin... It's a head!... Got", heads, "head(s) so far and", tails, "tail(s) so far"
        else:
            tails += 1
            heads += 0
            print "Attempt #", x, "Throwing a coin... It's a head!... Got", heads, "head(s) so far and", tails, "tail(s) so far"
            
print coinToss()


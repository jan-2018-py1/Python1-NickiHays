#write function to generate 10 scores between 60 & 100
#function should display score and associated grade



def score_grade():
    import random
    for x in range(0,10):
        y = random.randint(60,100)
        if y < 70:
            print "Score:", y, "Your grade is D"
        elif y >= 70 and y <= 79:
            print "Score:", y, "Your grade is C"
        elif y >= 80 and y <= 89:
            print "Score:", y, "Your grade is B"
        else:
            print "Score:", y, "Your grade is A"

print score_grade()
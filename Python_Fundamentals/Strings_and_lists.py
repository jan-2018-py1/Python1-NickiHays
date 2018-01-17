words = "It's thanksgiving day. It's my birthday, too!"
print words.find("day")
new_words = words.replace("day", "month")
print new_words


x = [2, 54, -2, 7, 12, 98]
print min(x)
print max(x)


p = ["hello", 2, 54, -2, 7, 12, 98, "world"]
print p[0] + p[7]

n= [19,2,54,-2,7,12,98,32,10,-3,6]
new_n = sorted(n)
print new_n
print len(new_n)
half_n = new_n[5:]
new_n = new_n[:5]

new_list = ([new_n] + half_n)
print new_list
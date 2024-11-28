i=0
star=""
for i in range(0,3):
    star = star + "*"
    print(star)
hashtag = "#"
space = ""
for j in range(0,5):
    print(space + hashtag)
    space = space + " "



def wordAdd(word, count):
    if count == 0:
        return ""
    else:
        print(word * count)
        return wordAdd(word, count - 1)

wordAdd("*", 3)

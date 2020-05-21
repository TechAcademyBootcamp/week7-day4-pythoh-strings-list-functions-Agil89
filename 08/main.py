def longest(l):
    count = 0
    for x in l:
        if len(x)>count:
            count = len(x)
    return count



a = ['asds','asdasd','asdsad','das','asdasdsdasddas','asd','dasdasd']
print(longest(a))
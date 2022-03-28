def filter_long_words(words,n):
    l =list()
    for i in words:
        if len(i) >n:
            l.append(i)
    return l

words = ["hello",'World',"this","is","ineuron"]
n = 3
x = filter_long_words(words,n)
print("words with more than {} alphabets are {}".format(n,x))
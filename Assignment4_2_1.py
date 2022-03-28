def mapwords(words):
    l= list()
    for i in words:
        x = len(i)
        l.append(x)
    return l

words = ["hello",'World',"this","is","ineuron"]
x = mapwords(words)
print(x)
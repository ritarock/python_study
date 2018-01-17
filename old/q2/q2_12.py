import re

f = open("hightemp.txt")
text = f.read()
lines = f.readlines()
f.close

def fileadd(text,x):
    file = open('./col'+str(x)+'.txt','wt')
    file.write(column(text,x))
    file.close

def column(text,x):
    col = text.split()[x-1:len(text.split()):4]
    ans = ""
    for n in col:
        if len(lines) == len(text.split()):
            ans = ans + n
        else:
            ans = ans + n + "\n"
    return ans

fileadd(text,1)
fileadd(text,2)

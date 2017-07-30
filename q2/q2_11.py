import re

f = open("hightemp.txt")
text = f.read()
f.close

print (text.replace("\t"," "))
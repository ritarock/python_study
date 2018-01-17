import re
f1 = open("col1.txt")
text1 = f1.readlines()
f1.close

f2 = open("col2.txt")
text2 = f2.readlines()
f2.close

colmerge =""

for col1,col2 in zip (text1,text2):
    colmerge = colmerge + col1.replace("\n","") + "\t" + col2


file = open('mergefile.txt','wt')
file.write(colmerge)
file.close

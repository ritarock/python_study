import sys

f = open("hightemp.txt")
text = f.readlines()
f.close

input = sys.argv[1]
input = int(input)

if input > len(text):
    print("error")
else:
    for n in range(0,input):
        print(text[n].replace("\n",""))
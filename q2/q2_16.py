import sys
input = sys.argv[1]
input = int(input)

f = open("hightemp.txt")
text = f.readlines()
f.close

def maketext(input,text):
    if len(text) % input != 0:
        print("error")
    else:
        n = int(len(text) / input)
        for x in range(n):
            file = open('./text'+str(x+1)+'.txt','wt')
            file.write("".join(text[x*input:(x+1)*input]))
            file.close
            
maketext(input,text)
words = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

words = words.replace(",","").replace(".","")
words = words.split()
wlist = []

for word in words :
    wlist.append(len(word))

print(words)
print(wlist)
word = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
word = word.replace(".","").replace(",","")
word = word.split()
dict = {}
for w in range(0,len(word)):
    if w in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        dict[w] = (word[w])[0:1]
    else:
        dict[w] = (word[w])[0:2]
print(dict)

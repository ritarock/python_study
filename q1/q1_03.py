words = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = words.replace(".","").replace(",","")
words = words.split()
dict = {}
for word in range(0,len(words)):
    if word in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        dict[word] = (words[word])[0:1]
    else:
        dict[word] = (words[word])[0:2]
print(dict)

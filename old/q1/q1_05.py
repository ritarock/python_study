word = "I am an NLPer"

wordSplit = word.split(" ")
wordList = list(word)


def n_gram(wordSplit,x):
    last = len(wordSplit)
    ans = []
    for i in range(0,last-x + 1):
        ans.append(wordSplit[i:i+x])
    return ans


print(n_gram(wordSplit,2))
print(n_gram(word,2))

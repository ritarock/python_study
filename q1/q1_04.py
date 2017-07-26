# word = "I am an NLPer"

# word_split = word.split(" ")
# word_list = list(word)

# def n_gram(word_split,x):
#     last = len(word_split)
#     print(last)
#     ans = []
#     for i in range(0,last-1):
#         ans.append(word_split[i:i+1])
#     return ans

# print(n_gram(word_split,2))

word = "I am an NLPer"

wordSplit = word.split(" ")
wordList = list(word)


def n_gram(wordSplit,x):
    last = len(wordSplit)
    ans = []
    for i in range(0,last-1):
        ans.append(wordSplit[i:i+2:1])
    return ans


print(n_gram(wordSplit,2))

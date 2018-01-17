import random

word = "I couldn't believe that I could actually "\
        "understand what I was reading : the phenomenal power of the human mind ."

ans = []

def wordsplit(word):
    word_split = word.split()
    for w in word_split:
        ans.append(ran(w))
    return " ".join(ans)


def ran(word):
    if len(word) < 5:
        return word
    else:
        f_word = word[0]
        e_word = word[-1]
        r_word = word[1:-1]
        print(r_word)
        r_word = "".join(random.sample(list(r_word),len(list(r_word))))
        word = f_word +r_word + e_word
        return word

print (wordsplit(word))


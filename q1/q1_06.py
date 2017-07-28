import q1_05

word1 = "paraparaparadise"
word2 = "paragraph"


print(q1_05.n_gram(word1,2))
print(q1_05.n_gram(word2,2))


X = set(q1_05.n_gram(word1,2))
Y = set(q1_05.n_gram(word2,2))

print(X)
print(Y)
print("和集合:",X|Y)
print("積集合:",X&Y)
print("差集合:",X-Y)

print('se' in X)
print('se' in Y)
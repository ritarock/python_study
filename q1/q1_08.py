# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

word = "We appreciate your agreement on the draft we sent on April 1st."

word_list = list(word)


def cipher(word):
    ans = []
    for w in word_list:
        if w.islower() == True:
            ans.append(chr(219-(ord(w))))
        else:
            ans.append(w)
    return ans

print("".join(cipher(word_list)))
# print("1".islower()) #=> False
# print("A".islower()) #=> False
# print("a".islower()) #=> True

str1 = "パトカー"
str2 = "タクシー"

str3 = [a + b for a,b in zip (str1,str2)]
print("".join(str3))
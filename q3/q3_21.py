from q3_20 import uktext
import re

f = './jawiki-country.json.gz'

# [[Category:ヘルプ|はやみひよう]]

text = uktext(f)

regex =r'^\[\[.*Category:>*\]\]$'
pattern = re.compile(regex)
matchObj = pattern.match(text)

print(matchObj)
print(pattern)

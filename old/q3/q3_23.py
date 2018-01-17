import gzip
import json
import re
import q3_20

f = './jawiki-country.json.gz'

# [[Category:ヘルプ|はやみひよう]]
# ===競馬===
text = (q3_20.uktext()).split('\n')
# print(text)

# for i in text:
#     category_line = re.search("^\[\[Category:(.*?)(|\|.*)\]\]$", i)
#     if category_line is not None:
#         print(category_line.group(0))

for i in text:
    level = re.search("^(={2,})(.+?).*$",i)
    if level is not None:
        print(level.group(0))
        print(int(level.group(0).count('=')/2-1))

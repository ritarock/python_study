import gzip
import json
import re
import q3_20

f = './jawiki-country.json.gz'

text = (q3_20.uktext()).split('\n')

print(text)

for i in text:
    category_line = re.search("^\[\[ファイル:(.*?)(|\|.*)\]\]$", i)
    if category_line is not None:
        print(category_line.group(1))
    jcategory_line = re.search("^\[\[file(.*?)(|\|.*)\]\]$", i)
    if jcategory_line is not None:
        print(jcategory_line.group(1))

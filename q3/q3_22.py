import gzip
import json
import re
import q3_20

f = './jawiki-country.json.gz'


text = (q3_20.uktext()).split('\n')

for i in text:
    category_line = re.search("^\[\[Category:(.*?)(|\|.*)\]\]$", i)
    if category_line is not None:
        print(category_line.group(1))


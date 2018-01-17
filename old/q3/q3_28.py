import gzip
import json
import re
import q3_20

f = './jawiki-country.json.gz'

text = (q3_20.uktext()).split('\n')


pt = r'<\/?[br|ref][^>]*?>'
# 置換後の文字列 = re.sub(正規表現, 置換する文字列, 置換される文字列 [, 置換回数])
def edit(word):
    ptword = re.sub(r'<\/?[br|ref][^>]*?>',"",word)
    return ptword



for i in text:
    category_line = re.search("^(.*?)\s=\s(.*)", i)
    if category_line is not None:
        # print(category_line.group(0).replace("'''","").replace("[[","").replace("]]",""))
        print(edit(category_line.group(0).replace("'''","").replace("[[","").replace("]]","")))
        if category_line.group(1) == "|公式国名":
            for j in text:
                test = re.search("^\*\{\{(.*?)<br/>$", j)
                if test is not None:
                    # print(test.group(0))
                    print(edit(test.group(0)))
            for k in text:
                test1 = re.search("^\*\*\{\{(.*?)</ref>$", k)
                if test1 is not None:
                    # print(test1.group(0).replace("'''","").replace("[[","").replace("]]",""))
                    print(edit(test1.group(0).replace("'''","").replace("[[","").replace("]]","")))


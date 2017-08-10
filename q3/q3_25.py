import gzip
import json
import re
import q3_20

f = './jawiki-country.json.gz'

text = (q3_20.uktext()).split('\n')

# print(text)

for i in text:
    category_line = re.search("^(.*?)\s=\s(.*)", i)
    if category_line is not None:
        print(category_line.group(0))
        if category_line.group(1) == "|公式国名":
            for j in text:
                test = re.search("^\*\{\{(.*?)<br/>$", j)
                if test is not None:
                    print(test.group(0))
            for k in text:
                test1 = re.search("^\*\*\{\{(.*?)</ref>$", k)
                if test1 is not None:
                    print(test1.group(0))




# "|公式国名":


# '|公式国名 = {{lang|en|United Kingdom of Great Britain and Northern Ireland}}<ref>英語以外での正式国名:<br/>', 
# '*{{lang|gd|An Rìoghachd Aonaichte na Breatainn Mhòr agus Eirinn mu Thuath}}（[[スコットランド・ゲール語]]）<br/>', 
# '*{{lang|cy|Teyrnas Gyfunol Prydain Fawr a Gogledd Iwerddon}}（[[ウェールズ語]]）<br/>', 
# '*{{lang|ga|Ríocht Aontaithe na Breataine Móire agus Tuaisceart na hÉireann}}（[[アイルランド語]]）<br/>',
# '*{{lang|kw|An Rywvaneth Unys a Vreten Veur hag Iwerdhon Glédh}}（[[コーンウォール語]]）<br/>', 
# '*{{lang|sco|Unitit Kinrick o Great Breetain an Northren Ireland}}（[[スコットランド語]]）<br/>', 
# '**{{lang|sco|Claught Kängrick o Docht Brätain an Norlin Airlann}}、{{lang|sco|Unitet Kängdom o Great Brittain an Norlin Airlann}}（アルスター・スコットランド語）</ref>'
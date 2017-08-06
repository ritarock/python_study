import gzip
import json
import re

f = './jawiki-country.json.gz'

# file = gzip.open(f)
# for line in file:
#   data_json = json.loads(line)
#   # print(data_json['title'])
#   if data_json['title'] == u'イギリス':
#     text = data_json['text']
#     break
def uktext():
  with gzip.open(f) as file:
    for line in file:
      data_json = json.loads(line)
      if data_json['title'] == u'イギリス':
        text = data_json['text']
        break
    return text

# print(uktext())
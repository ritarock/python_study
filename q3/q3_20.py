import gzip
import json

f = './jawiki-country.json.gz'

with gzip.open(f) as file:
  for line in file:
    data_json = json.loads(line)
    # print(data_json['title'])
    if data_json['title'] == 'イギリス':
      print(data_json['text'])
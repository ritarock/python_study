import gzip
import json

f = './jawiki-country.json.gz'

def uktext(f):
  with gzip.open(f) as file:
    for line in file:
      data_json = json.loads(line)
      if data_json['title'] == 'イギリス':
        return (data_json['text'])

print(uktext(f))
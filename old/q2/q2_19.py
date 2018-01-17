from collections import Counter
data = [line.split('\t')[0] for line in open('hightemp.txt')]
# print(",".join(data))
counter = Counter(data)

for data,cnt in counter.most_common():
    print(data,cnt)
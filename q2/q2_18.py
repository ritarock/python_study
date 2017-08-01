key = [line.split('\t')[2] for line in open('hightemp.txt')]
value = [line for line in open('hightemp.txt')]

ans = dict(zip(key,value))
print(ans)

for key,value in sorted(ans.items()):
    print(value)

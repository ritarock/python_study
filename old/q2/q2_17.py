import re

f = open("hightemp.txt")
l = f.readlines()
f.close

print('\n'.join(set((x.split('\t')[0] for x in l))))
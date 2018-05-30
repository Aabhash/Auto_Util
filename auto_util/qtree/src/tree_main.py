import re

print()
query = 'SELECT RLS.OK FROM TAB WHERE T = 2 ORDER BY OK'
keywordfile = 'keywords.txt'
keywords = []
with open(keywordfile, 'r') as f:
    keywords = f.read().split()

ac_list = []
query_words = re.split('(\W+)', query)
print(query_words)
print(keywords)

ac_list = [word for word in query_words if word in keywords]
print(ac_list)

triplets = []
for i in range(len(ac_list)-1):
    q_block = re.search(''+ac_list[i]+' *.* '+ac_list[i+1]+'', query)
    triplets.append([ac_list[i],ac_list[i+1],q_block.group(0)])

print(triplets)

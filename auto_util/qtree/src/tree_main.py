import re

query = 'SELECT RLS.OK FROM TAB WHERE T = 2 ORDER BY OK'
keywordfile = 'keywords.txt'
keywords = []
with open(keywordfile, 'r') as f:
    keywords = [word.strip() for word in f.read().split('\n')]

query_words = re.split('(\W+)', query)
print(query_words)
print(keywords)

ac_list = [word for word in keywords if word in query]
print(ac_list)

triplets = []
triplets 
for i in range(len(ac_list)-1):
    q_block = re.search(''+ac_list[i]+' *.* '+ac_list[i+1]+'', query)
    triplets.append([ac_list[i],ac_list[i+1],q_block.group(0)])
print(triplets)

import re
print()
query = 'SELECT * FROM TAB WHERE T = 2'
query_block1 = re.search('SELECT *.* FROM', query)
query_block2 = re.search('FROM *.* WHERE', query)
query_block3 = re.search('WHERE *.*', query)
print(query_block1.group(0))
print(query_block2.group(0))
print(query_block3.group(0))

#Shotest distance between any two keywords
#OR List of keywords
#Get the meat between keywords

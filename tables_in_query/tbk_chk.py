import re

table_dict = {}
table_file = "file.txt"
with open(table_file, 'r') as f:
    list_of_tables = f.read().split('\n')

for i in range(len(list_of_tables)):
    table_dict[list_of_tables[i]] = i
print(table_dict)
print("*********************TABLE LIST OBTAINED****************************\n\n")

query_file = 'query.txt'
query = ''
with open(query_file, 'r') as r:
    query = r.read()
" ".join(query.split())

query_word_list = re.split('(\W+)', query)
tables_in_query = set()
for word in query_word_list:
    if (word in table_dict):
        tables_in_query.add(word)

with open('output.txt', 'w') as f:
    for i in tables_in_query:
        f.write(str(i) + '\n')
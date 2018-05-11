import re

def read_tables(table_file):
    l = []
    with open(table_file, 'r') as f:
         l = (f.read().split('\n'))
    return l

def read_query(query_file):
    with open(query_file, 'r') as r:
        query = r.read()
    return query

def remove_whitespace(query):
    return " ".join(query.split())

def wordify_query(q):
    return re.split('(\W+)', query)

table_dict = {}
table_file = "file.txt"
table_list = read_tables(table_file)

for i in range(len(list_of_tables)):
    table_dict[list_of_tables[i]] = i
print(table_dict)
print("*********************TABLE LIST OBTAINED****************************\n\n")

query_file = 'query.txt'
query = read_query(query_file)
cleaned_query = remove_whitespace(query)
query_word_list = wordify_query(cleaned_query)

tables_in_query = set()
for word in query_word_list:
    if (word in table_dict):
        tables_in_query.add(word)

with open('output.txt', 'w') as f:
    for i in tables_in_query:
        f.write(str(i) + '\n')
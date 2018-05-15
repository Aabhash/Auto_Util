import re

def read_tables(table_file):
    with open(table_file, 'r') as f:
         l = (f.read().split('\n'))
    return l

def convert_to_dictionary(table_list):
    d = {}
    for i in range(len(table_list)):
        d[table_list[i]] = i
    return d

def read_query(query_file):
    with open(query_file, 'r') as r:
        query = r.read()
    return query

def remove_whitespace(query):
    return " ".join(query.split())

def wordify_query(q):
    return re.split('(\W+)', q)

def get_tables_in_query(table_dict, words_in_query):
    t_in_q = {word for word in words_in_query if word in table_dict}
    return t_in_q

def write_to_file(output_file, tables_in_query):
    with open(output_file, 'w') as f:
        for i in tables_in_query:
            f.write(str(i) + '\n')

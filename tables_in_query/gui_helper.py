import re

def read_tables(string_tables):
    string_tables = string_tables.upper()
    l = (string_tables.split('\n'))
    return l

def convert_to_dictionary(table_list):
    d = {}
    for i in range(len(table_list)):
        d[table_list[i]] = i
    return d

def clean(query):
    query_lines = query.splitlines()
    query = ''
    for line in query_lines:
        query = query + re.sub('--.*', '', line) +' '
    query = query.upper()
    return " ".join(query.split())

def wordify_query(q):
    return re.split('(\W+)', q)

def get_tables_in_query(table_dict, words_in_query):
    t_in_q = {word for word in words_in_query if word in table_dict}
    return t_in_q
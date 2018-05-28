import re        

def read_tables(string_tables):
    string_tables = string_tables.upper()
    l = (string_tables.split('\r\n'))
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
        query = query + re.sub('--.*', '', line)
        query = re.sub('//*.*/*/', '', query) +' ' 
    query = query.upper()
    return " ".join(query.split())

def wordify_query(q):
    return re.split('(\W+)', q)

def get_tables_in_query(table_dict, words_in_query):
    t_in_q = {word for word in words_in_query if word in table_dict}
    return t_in_q

def execute(txt_t, txt_q):
    table_list = read_tables(txt_t)
    table_dict = convert_to_dictionary(table_list)
    cleaned_query = clean(txt_q)
    words_in_query = wordify_query(cleaned_query)
    tables_found = get_tables_in_query(table_dict, words_in_query)
    return tables_found

from helper import *
from tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        self.init_window()

    def init_window(self):    
        self.master.title("Table_Q")
        self.pack(fill=BOTH)
        quitButton = Button(self, text="Find Tables",command=self.execute)
        quitButton.pack(side=BOTTOM)
        text_tables = Text(width=30)
        text_query = Text(width=30)
        text_output = Text(width=30)
        text_tables.pack(side=LEFT, expand=1)
        text_query.pack(side=LEFT, expand=1)
        text_output.pack(side=LEFT, expand=1)
        
    def execute(self):
        #print("Reading file paths")
        table_file = "tables.txt"
        query_file = 'query.txt'
        output_file = 'output.txt'
        #print("Reading list of tables from file {0}".format(table_file))
        table_list = read_tables(table_file)
        table_dict = convert_to_dictionary(table_list)
        #print("Table List Obtained")
        #print("Reading query from file {0}".format(query_file))
        query = read_query(query_file)
        cleaned_query = remove_whitespace(query)
        words_in_query = wordify_query(cleaned_query)
        #print("Getting tables from query")
        tables_in_query = get_tables_in_query(table_dict, words_in_query)
        #print("Writing to file")
        write_to_file(output_file, tables_in_query)
        exit()

def main(): 
    root = Tk()
    w, h = 800, 650
    ws, hs = root.winfo_screenwidth(), root.winfo_screenheight()
    x, y = (ws/2) - (w/2), (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    app = Window(root)
    root.mainloop()
        
if __name__ == "__main__":
    main()
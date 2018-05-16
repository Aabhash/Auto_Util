from gui_helper import *
from tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)   
        self.text_tables = ""
        self.text_query = ""
        self.text_output = ""            
        self.master = master
        self.init_window()

    def init_window(self):    
        self.master.title("Parse Tables")
        self.pack(fill=BOTH)
        self.text_tables = Text(width=30)
        self.text_query = Text(width=30)
        self.text_output = Text(width=30)
        self.text_tables.pack(side=LEFT, expand=1)
        self.text_query.pack(side=LEFT, expand=1)
        self.text_output.pack(side=LEFT, expand=1)
        quitButton = Button(self, text="FIND",command=self.execute)
        quitButton.pack(side=BOTTOM)
        
    def execute(self):
        self.text_output.delete('1.0',END)
        #print("Reading file paths")
        #table_file = "tables.txt"
        #query_file = 'query.txt'
        #output_file = 'output.txt'
        
        #print("Reading list of tables from file {0}".format(table_file))
        table_list = read_tables(self.text_tables.get("1.0", END))
        table_dict = convert_to_dictionary(table_list)
        #print("Table List Obtained")
        #print("Reading query from file {0}".format(query_file))
        cleaned_query = clean(self.text_query.get("1.0", END))
        words_in_query = wordify_query(cleaned_query)
        #print("Getting tables from query")
        tables_found = get_tables_in_query(table_dict, words_in_query)
        #print("Writing to file")
        for i in tables_found:
            self.text_output.insert(END, (str(i) + '\n'))
        #exit()

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
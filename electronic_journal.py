from datetime import date
import os
import json 
import tkinter as tk
from tkinter import ttk

#eJournal

journal = {}

today = date.today()

#Load the backing dictionary
if os.path.exists('myJournal.txt'):
    with open('myJournal.txt', 'r') as f:
        journal = json.load(f)
        print(journal)
else:
    print('File not found! Open the journal and add entries to save.')

def save(txt):
    journal[today.strftime("%m/%d/%Y")] = txt

#Write Window
def write():
    txt_window = tk.Toplevel()
    txt_window.attributes('-fullscreen', True)
    txt_window.title("Write")
    txt = tk.Text(txt_window, height = 5, width = 52, bg='light yellow')
    txt_window.configure(bg='light blue')

    def take_input():
        output.delete("1.0", "end-1c")
        entry = txt.get("1.0", "end-1c")
        print(entry)
        if entry is not None:
            
            journal[today.strftime("%m/%d/%Y")] = entry
            
            output.place(x=725, y=200)
            output.insert('end', 'Confirmed')
        
        
        
            
        else:
            output.insert('end', 'Error!')
        
        
        
    txt_label = tk.Label(txt_window, text="Tell me about your day  ")

    
    confirm_butt = tk.Button(txt_window, text="Enter", command=lambda:take_input())
    close_butt = tk.Button(txt_window, text="Close", command=txt_window.destroy)
    output = tk.Text (txt_window, height= 1, width=9, bg='light green' )
    
 


    close_butt.place(x= 750, y=150)
    confirm_butt.place(x=750, y=120)

    txt_label.pack()
    txt.pack()
    


    txt_window.mainloop()


#view window 
def view():
    peak = tk.Toplevel()
    peak.attributes('-fullscreen', True)
    peak.title("View Entires")
    peak.configure(bg='light blue')

    #value
    dates = list(journal.keys())
    entries = list(journal.values())



    #labels
    toptitle = ttk.Label(peak, text = 'Saved Entries', background='blue', foreground='white', font = ("Times New Roman", 15))
    itemsLabel = ttk.Label(peak, text= 'Select an Entry to View: ', font = ('Times New Roman', 10))
    output = tk.Text (peak, height= 1, width=9, bg='light green' )



    #Buttons
    dtype = tk.StringVar()
    options = ttk.Combobox(peak, width=27,textvariable=dtype)
    
    read_putt = tk.Button(peak, text='Read', command=lambda:read())
    return_butt = tk.Button(peak, text='Return', command=peak.destroy)
    read_txt = tk.Text(peak, height= 5, width= 50, bg= 'light yellow')
    clear_butt = tk.Button(peak, text='Clear',command=lambda:clear())

    #In case people want to make edits 
    edit_mess = tk.Message(peak, text='You can modify the text in the box, to change your entry if you like. Make your changes and hit "Save Changes" button when done! ', bg= 'light blue', width=1500,)
    edit_butt = tk.Button(peak, text='Save Changes', command=lambda:edit())

    def read():
        date_select = options.get()
        read_txt.place(x=600, y=300)
        read_txt.insert('end', journal.get(date_select))
        edit_mess.place(x=450, y=500)
        edit_butt.place(x=750, y=450)

    def clear():
        read_txt.delete("1.0", "end-1c")
        read_txt.place_forget()

    def edit():
        date_select = options.get()
        new_txt = read_txt.get("1.0", "end-1c")
        if new_txt != journal.get(date_select):
            journal[date_select] = new_txt
            output.place(x=725, y=700)
            output.insert('end', 'Confirmed')
            print("Changes Saved")
        else:
            print("no changes found, therefore no actions will be taken")
        
        

        


    options['values'] = (dates)

    toptitle.place(x=725, y = 10)
    options.place(x=685, y = 75)
    options.current()

    return_butt.place(x=755, y=175)
    read_putt.place(x=760, y=105)
    clear_butt.place(x=760, y= 140)


    peak.mainloop()

#initalize window 
window = tk.Tk()
window.attributes('-fullscreen', True)
window.title("EJournal")
window.configure(bg='light blue')
mainTxt = tk.Label(text="Welcome to your Electronic Journal")




close_butt = tk.Button(window, text="Save and Exit", command=window.destroy)
add_butt = tk.Button(window, text="Write in Journal", command=write)
peak_butt = tk.Button(window, text="View Entries", command=view)


mainTxt.place(x=675, y=10)
add_butt.place(x=250 , y=300)
close_butt.place(x=750, y= 300)
peak_butt.place(x=1250, y= 300)
#img1.place(x=0,y=0)

window.mainloop()
with open('myJournal.txt', 'w') as f:
    json.dump(journal, f)
print("journal successfully saved!")

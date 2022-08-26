from tkinter import *
from tkinter import filedialog
from webbrowser import BackgroundBrowser
from tkinter import messagebox

#asking if the user wants to close the program window

def on_closing():
    if messagebox.askokcancel('Exit', 'Do You want to exit the App?\n Data will not be saved'):
        root.destroy()

#head

root=Tk()
root.geometry('900x900')
root.title('Notepad')
root.config(bg='#99ff99')
root.iconbitmap('notep.ico')
root.resizable(False,False)
root.wm_attributes('-topmost', 1)
root.protocol('WM_DELETE_WINDOW', on_closing)




#command

def save_file():
    open_file=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    if open_file is None:
        return
    text=str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()

def open_file():
    file=filedialog.askopenfile(mode='r',filetype=[('text files','*.txt')])
    if file is not None:
        content=file.read()
    entry.insert(INSERT,content)   


#buttons

b1=Button(root,width='20',
          height='2',bg='#E0FFFF',
          text='save file',
          font=('Roboto',14,'bold'),
          command=save_file,
          bd=7,
          activebackground='#DCDCDC',
          relief=RIDGE

).place(x=100,y=20)


b2=Button(root,width='20',
          height='2',bg='#E0FFFF',
          text='open file',
          font=('Roboto',14,'bold'),
          command=open_file,
          bd=7,
          activebackground='#DCDCDC',
          relief=RIDGE,
          

                
).place(x=550,y=20)

#window for writing

entry=Text(height='33', 
           wrap=WORD, 
           bg='green', 
           font=50, 
           fg='white', 
           selectforeground='#33FF33', 
           selectbackground='black', 
           xscrollcommand=True 
) 
entry.place(x=11,y=100)


root.mainloop()

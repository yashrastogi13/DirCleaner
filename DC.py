import tkinter as tk
from tkinter import ttk
import os

def delete_empty_directory(d):
    try:
        for item in os.listdir(d):
            directory = os.path.join(d,item)
            if os.path.isdir(directory):
                if not os.listdir(directory):
                    #print(directory)
                    os.rmdir(directory)
                else:
                    delete_empty_directory(directory)
                    if not os.listdir(directory):
                        os.rmdir(directory)
        return True
    except Exception:
        return "Error : Invalid Path"

def print_error(e):
    global status_val
    status_val.set(e)
    status_description.configure(fg="red")
    status_description.place(x=110,y=200)

def finished():
    global status_val
    status_val.set("Defragmentation Complete")
    status_description.configure(fg="Green")
    status_description.place(x=85,y=200)

def submit_click():
    d = entry.get()
    status = delete_empty_directory(d)
    if status != True:
        print_error(status)
    else:
        finished()
    directory_val.set("")

def on_click(event):
    entry.configure(state=tk.NORMAL)
    entry.delete(0,tk.END)
    entry.unbind('<Button-1>',on_click_action)

window = tk.Tk()
window.geometry("330x270")
window.resizable(False,False)
window.title("Tkinter")

directory_val = tk.StringVar(master=window)                       #the entry value is stored in this var
directory_val.set("Enter the directory")
status_val = tk.StringVar(master=window)

frame = tk.Frame(master = window,relief = tk.GROOVE,bd=4,bg="white",width = 100,height = 100,visual=None,takefocus=True)

small_frame = tk.Frame(master=frame,relief=tk.FLAT,pady=25,bg="white")
photo = tk.PhotoImage(file = "icon.png",height = 35,width=35)
photo_label = tk.Label(master = small_frame,image=photo,padx=20,bg="white")
label = tk.Label(master = small_frame,text="Directory Defragmentor",font=("ariel",14,"bold"),anchor = "center",bg="white")
photo_label.pack(side=tk.LEFT)
label.pack()

entry = ttk.Entry(master = frame,width = 40,textvariable = directory_val,takefocus=True)
entry.configure(state=tk.DISABLED)
on_click_action = entry.bind('<Button-1>',on_click)

button = tk.Button(master = frame,text = "Start",command=submit_click,relief=tk.RAISED,height=1,width=10,bg="black",fg="white")
status_description = tk.Label(master=frame,textvariable=status_val,bg="white")
photo_label.pack(side="left")
small_frame.pack()
entry.pack()
button.pack(pady=40)
frame.pack(fill = tk.BOTH,expand = True)
window.mainloop()


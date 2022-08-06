import tkinter
import tkinter.messagebox
import pickle

# create a window
window = tkinter.Tk() 
window.title("To-Do List by Taybu")

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")

def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")

def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))

# Create GUI
frame_tasks = tkinter.Frame(window)
frame_tasks.pack()

# height is number of rows and width is column
listbox_tasks = tkinter.Listbox(frame_tasks, height=20, width=40, bg = "#C6B9C4")
listbox_tasks.pack(side=tkinter.LEFT)

# scoll the information
scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# single task at a time
entry_task = tkinter.Entry(window, width=55, bg = "#92c38F")
entry_task.insert(0, "Enter the task here")
entry_task.pack()

button_add_task = tkinter.Button(window, text="Add task", width=48, command=add_task, bg='blue')
button_add_task.pack()

button_delete_task = tkinter.Button(window, text="Delete task", width=48, command=delete_task, bg = 'red')
button_delete_task.pack()

button_load_tasks = tkinter.Button(window, text="Load tasks", width=48, command=load_tasks, bg = "#9F0C7B")
button_load_tasks.pack()

button_save_tasks = tkinter.Button(window, text="Save tasks", width=48, command=save_tasks, bg = "#A89CA5")
button_save_tasks.pack()

# run the code
window.mainloop()
# To-Do List
from tkinter import *
import random
from tkinter import messagebox
import time
from time import strftime
from tkinter.font import Font

def main():
    global home
    global to_do_list
    global t_entries
    global task_entry
    
    t_entries = ("What do you need to do?", "Add a new task...", "e.g. Buy groceries", "Type your task here",
                 "What's next on your list?", "e.g. Finish report by Friday", "Enter a task...",
                 "Got something to remember?", "e.g. Call the dentist", "Add to your to-do list", "What's on your mind?",
                 "Something to get done?", "Add it before you forget!", "What's the plan today?", "One more thing to do...",
                 "e.g. Walk the dog", "e.g. Reply to emails", "e.g. Pay electricity bill", "e.g. Clean the kitchen",
                 "e.g. Book dentist appointment", "Jot down a task...", "What's due today?", "Add something to tackle",
                 "e.g. Submit assignment", "Type here to add a task", "What needs doing?", "e.g. Pick up dry cleaning",
                 "Add your next task", "e.g. Renew car insurance", "Anything to add?")
    t_entry = random.choice(t_entries)

    home = Tk()
    home.title("Simple To-Do List")
    home.geometry("420x620")
    home.config(bg="#2e2c2c")
    #windowim = PhotoImage(file='logo.png')  # Un-Comment this and the line below this,
    #home.iconphoto(True, windowim)          # if the 'logo.png' file is in the same folder as the script

    digifont = Font(family="DS-Digital",size=26)  # Un-Comment this line if 'DS-Digital' font is not installed
                                                                          # AND 
    #digifont = Font(family="Consolas",size=18,weight='bold') # Comment this line if the above condition is met.

    header_text = Label(home, text="To-Do List", font=("Calibri",25,"bold"), fg="#e6e0e0", bg="#2e2c2c", pady=10)
    header_text.place(relx=0.5,rely=0.01,anchor="n")

    time_label = Label(home, font=digifont, padx=5, bg="#2e2c2c", fg="#d3cccc")
    time_label.place(relx=0.835,rely=0.025,anchor="n")

    def time():
        string = strftime('%H:%M:%S')
        time_label.config(text=string)
        time_label.after(1000,time)

    add_task_frame = Frame(home, bg="#2e2c2c")
    add_task_frame.place(relx=0.5,rely=0.1,anchor="n")

    tasks = []

    def add_task():
        task = task_entry.get()
        if to_do_list.size() <= 20 and task != "" and task not in t_entries:
            to_do_list.insert(to_do_list.size(), task)
            to_do_list.config(height=to_do_list.size())
            tasks.append(task)
            task_entry.delete(0,END)
            if len(task) > to_do_list.cget("width"):
                to_do_list.config(width=len(task)+5)
        elif to_do_list.size() > 20:
            messagebox.showwarning(title="Line expansion",message="List cannot exceed 20 lines")
        elif task == "":
            pass

    def add_event_t(event):
            task = task_entry.get()
            if to_do_list.size() <= 20 and task != "":
                to_do_list.insert(to_do_list.size(), task)
                to_do_list.config(height=to_do_list.size())
                tasks.append(task)
                task_entry.delete(0,END)
                if len(task) > to_do_list.cget("width"):
                    to_do_list.config(width=len(task)+2)
            elif to_do_list.size() > 20:
                messagebox.showwarning(title="Line expansion",message="List cannot exceed 20 lines")
            elif task == "":
                pass

    def clearentry(event):
        task_entry.delete(0,END)

    def replaceholder(event):
        global t_entries
        global task_entry
        t_entry = random.choice(t_entries)
        task_entry.delete(0,END)
        task_entry.insert(0,t_entry)
            
    task_entry = Entry(add_task_frame, width=30, font=('JetBrains Mono', 12, "italic"),
                        bg="#3a3736",   
                        fg="#dfd9d8",  
                        insertbackground="#dfd9d8",  
                        relief=FLAT,
                        highlightthickness=1,
                        highlightbackground="#5a5654", 
                        highlightcolor="#dfd9d8")
    task_entry.insert(0, t_entry)
    task_entry.pack(padx=3,side=LEFT)

    task_entry.bind("<FocusIn>",clearentry)
    task_entry.bind("<FocusOut>",replaceholder)
    task_entry.bind("<Return>",add_event_t)

    a_task_button = Button(add_task_frame, text="Add Task",
                        font=('JetBrains Mono', 11, 'bold'),
                        bg="#4a4644",
                        fg="#dfd9d8",
                        activebackground="#5a5654",
                        activeforeground="#ffffff",
                        relief=FLAT,
                        bd=0,
                        padx=12, pady=6,
                        cursor="hand2",
                        command=add_task).pack(padx=5,side=RIGHT)

    to_do_list = Listbox(home, font=('JetBrains Mono', 12, "bold"),
                        bg="#3a3736",
                        fg="#dfd9d8",
                        relief=FLAT,
                        highlightthickness=1,
                        highlightbackground="#5a5654",
                        selectbackground="#5a5654",
                        selectforeground="#ffffff",
                        bd=0)
    to_do_list.place(relx=0.5,y=130,anchor="n")
    to_do_list.config(height=8, width=40)

    bottom_but_frame = Frame(home)
    bottom_but_frame.place(relx=0.5,rely=0.9,anchor="n")

    def complete():
        for index in to_do_list.curselection():
            to_do_list.delete(index)
            to_do_list.config(height=to_do_list.size())

    def clear():

        def affirm():
            to_do_list.delete(0,END)
            confirm_win.destroy()

        def naffirm():
            confirm_win.destroy()


        confirm_win = Toplevel()
        confirm_win.geometry("360x150")
        confirm_win.config(bg="#2e2c2c")
        c_text = Label(confirm_win, text="Do you want to clear the list?", font=('JetBrains Mono', 14, 'bold'),bg="#2e2c2c",fg="#dfd9d8")
        c_text.place(relx=0.5,rely=0.2,anchor="n")
        countdown_label = Label(confirm_win, text="5", font=('JetBrains Mono', 14, 'bold'),bg="#2e2c2c",fg="#dfd9d8")
        countdown_label.place(relx=0.5,rely=0.35,anchor="n")
        def countdown(seconds_left):
            countdown_label.config(text=f"({str(seconds_left)})")
            if seconds_left > 0:
                confirm_win.after(1000, countdown, seconds_left - 1)

        countdown(5)

        buttonF = Frame(confirm_win)
        buttonF.place(relx=0.5,rely=0.6,anchor="n")
        cy_button = Button(buttonF, text="Yes", font=("Mono Sans",12,"bold"),bg="#4a4644",fg="#dfd9d8",activebackground="#5a5654",activeforeground="#ffffff",
                        relief=FLAT,bd=0,padx=12, pady=6,cursor="hand2",command=affirm).pack(side=LEFT)
        cn_button = Button(buttonF, text="No", font=("Mono Sans",12,"bold"),bg="#4a4644",fg="#dfd9d8",activebackground="#5a5654",activeforeground="#ffffff",
                        relief=FLAT,bd=0,padx=12, pady=6,cursor="hand2",command=naffirm).pack(side=RIGHT)
        confirm_win.after(5000, confirm_win.destroy)


    tsk_complete_b = Button(bottom_but_frame, text="Mark Completed", font=('JetBrains Mono', 11, 'bold'),
                        bg="#4a4644",
                        fg="#dfd9d8",
                        activebackground="#5a5654",
                        activeforeground="#ffffff",
                        relief=FLAT,
                        bd=0,
                        padx=12, pady=6,
                        cursor="hand2",command=complete).pack(side=LEFT)
    tsk_clear_b = Button(bottom_but_frame, text="Clear List", font=('JetBrains Mono', 11, 'bold'),
                        bg="#4a4644",
                        fg="#dfd9d8",
                        activebackground="#5a5654",
                        activeforeground="#ffffff",
                        relief=FLAT,
                        bd=0,
                        padx=12, pady=6,
                        cursor="hand2", command=clear).pack(side=RIGHT)

    time()

    home.mainloop()

if __name__ == "__main__":
    main()

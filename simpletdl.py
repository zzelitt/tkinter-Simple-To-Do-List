# To-Do List
from tkinter import *
import random
from tkinter import messagebox
import time
from time import strftime
import sys, os
from tkinter.font import Font

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def main():
    t_entries = ("ex: Call Mom tonight", "ex: Finish the homework", "ex: Eat healthy tonight", 
                "ex: Clean my room", "ex: Hit the gym", "ex: Do 10 push-ups",
                "ex: Yoga class at 6 tonight", "ex: Dentist appointment tomorrow", "ex: Cook food")
    t_entry = random.choice(t_entries)

    home = Tk()
    home.title("Simple To-Do List")
    home.geometry("420x620")
    home.config(bg="#2e2c2c")
    home.iconbitmap(resource_path("icons/listlogo1.ico"))

    header_text = Label(home, text="To-Do List", font=("Calibri",25,"bold"), fg="#e6e0e0", bg="#2e2c2c", pady=10)
    header_text.place(relx=0.5,rely=0.01,anchor="n")

    time_label = Label(home, font=("Arial Black",16), padx=5, bg="#2c2a2a", fg="#e6e0e0")
    time_label.place(relx=0.835,rely=0.035,anchor="n")

    def time():
        string = strftime('%H:%M')
        time_label.config(text=string)
        time_label.after(1000,time)

    add_task_frame = Frame(home, bg="#2e2c2c")
    add_task_frame.place(relx=0.5,rely=0.1,anchor="n")

    tasks = []

    def add_task():
        task = task_entry.get()
        if to_do_list.size() <= 20:
            to_do_list.insert(to_do_list.size(), task)
            to_do_list.config(height=to_do_list.size())
            tasks.append(task)
            if len(task) > to_do_list.cget("width"):
                to_do_list.config(width=len(task)+5)
        else:
            messagebox.showwarning(title="Line expansion",message="List cannot exceed 20 lines")
            
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

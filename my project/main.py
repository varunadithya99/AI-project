from rating_prediction import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def GoBack(gui):
    gui.destroy()
    main_page()


def close(root):
    root.destroy()


def main_page():
    global root
    root = Tk()
    global screen_height,screen_width
    screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (screen_width, screen_height))
    root.config(bg="yellow")
    head = Label(root, text="Online Course Recommendation System", font=("Helvetica", 50),bg='yellow')
    head.grid(row=0,column=0,padx=60,pady=40)
    new = Button(root, text="New User", font=("Times New Roman", 30), bd=3, command=new_user,height=1,width=12)
    old = Button(root, text="Old User", font=("Times New Roman", 30), bd=3, command=old_user,height=1,width=12)
    quit = Button(root, text="EXIT", font=("Times New Roman", 30), bd=3, command=lambda: close(root),height=1,width=12)
    old.grid(row=1,column=0,pady=40)
    new.grid(row=2,column=0,pady=40)
    quit.grid(row=3,column=0,pady=40)
    root.mainloop()

def table(prediction,root):
    frame = Frame(root,width=800,height=500,background="red")

    tree = ttk.Treeview(frame, columns=(1, 2, 3), height=10, show="headings")
    tree.pack(side = 'left')

    tree.heading(1, text="Sr.")
    tree.heading(2, text="Courses")
    tree.heading(3, text="Ratings")

    tree.column(1, width=200)
    tree.column(2, width=200)
    tree.column(3, width=200)

    scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    scroll.pack(side = 'right', fill = 'y')

    tree.configure(yscrollcommand=scroll.set)

    i = 1
    for val in prediction:
        tree.insert('', 'end', values=(i, courses[val], prediction[val]))
        i = i + 1
    frame.pack(pady=80)
def new_user():
    root.destroy()
    new_user_gui = Tk()
    #new_user_pred()
    head = Label(new_user_gui, text="Course recommendation for you", font=("Helvetica", 50), bg='yellow')
    head.pack()
    back = Button(new_user_gui, text="Back", font=('times', 20, 'bold'), command=lambda: GoBack(new_user_gui))
    new_user_gui.geometry("%dx%d" % (screen_width, screen_height))
    new_user_gui.config(bg="yellow")
    table(new_user_pred(), new_user_gui)
    back.pack()
    new_user_gui.mainloop()

def user_pred(user_id,password,old_user_gui):
    if user_id == password and 0 < user_id < 500:
        old_user_gui.destroy()
        old_user_gui = Tk()
        head = Label(old_user_gui, text="Course recommendation for you", font=("Helvetica", 50), bg='yellow')
        head.pack()
        back = Button(old_user_gui, text="Back", font=('times', 20, 'bold'), command=lambda: GoBack(old_user_gui))
        old_user_gui.geometry("%dx%d" % (screen_width, screen_height))
        old_user_gui.config(bg="yellow")
        table(old_user_pred(user_id),old_user_gui)
        back.pack()
        old_user_gui.mainloop()
    else:
        messagebox.showerror('Error', 'details are invalid!')



def old_user():
    root.destroy()
    old_user_gui = Tk()
    old_user_gui.geometry("%dx%d" % (screen_width, screen_height))
    old_user_gui.config(bg="yellow")
    head = Label(old_user_gui, text="Online Course Recommendation System", font=("Helvetica", 35), bg='yellow')
    head.grid(row=0, column=0, padx=60, pady=40)
    user = Label(old_user_gui,text="User ID",font=('times', 20, 'italic bold'),bg='yellow')
    passw = Label(old_user_gui,text="Password",font=('times', 20, 'italic bold'),bg='yellow')

    user_id = Entry(old_user_gui,bd=3,width=50)
    password = Entry(old_user_gui,bd=3,width=50)

    login = Button(old_user_gui,text="Login",font=('times',20,'bold'),command=lambda: user_pred(user_id.get(),password.get(),old_user_gui))
    back = Button(old_user_gui, text="Back", font=('times', 20, 'bold'), command=lambda: GoBack(old_user_gui))

    user.grid(row=1,column=0,pady=20)
    passw.grid(row=2,column=0,pady=20)
    user_id.grid(row=1,column=1,pady=20)
    password.grid(row=2,column=1,pady=20)
    login.grid(row=3,column=0,pady=20)
    back.grid(row=3,column=1,pady=20)
    old_user_gui.mainloop()

main_page()

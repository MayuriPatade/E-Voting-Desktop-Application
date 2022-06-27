from tkinter import *
import sqlite3
from tkinter import messagebox
from PIL import ImageTk, Image

#main Database
db=sqlite3.connect('login.db')
cur=db.cursor()

def login():
    db.execute("create table if not exists login(username text,password text)")
    # db.execute("insert into login(username,password) VALUES('admin','admin')")
    # db.execute("insert into login(username,password) VALUES('user','user')")
    cur.execute("select * from login where username=? AND password=?", (user_input.get(), pass_input.get()))
    row = cur.fetchone()
    if row:
        if row[0] == 'admin':
            admin_window()
            messagebox.showinfo('info', 'login successful')
        else:
            user_window()
    else:
        messagebox.showinfo('info', 'login failed')
    cur.connection.commit()
    db.close()



def clear():
    op = messagebox.showwarning("Clear", "Do you want to clear data? ")
    user_input.delete(0, END)
    pass_input.delete(0, END)


def admin_window():
    top = Toplevel()
    top.geometry("400x300")
    # creating frame
    f1 = Frame(top, width=400, height=300, bg="yellow")
    f1.place(x=0, y=0)
    # background image
    img_1 = Image.open("back.png")
    img1 = ImageTk.PhotoImage(img_1)
    # Create label to display Image
    L1 = Label(f1, image=img1)
    L1.place(x=0, y=0)
    Label(top, text="REGISTRATION SUCCESSFULL", font=("Arial", 10, "bold")).place(x=100, y=170)

    top.mainloop()


def user_window():
    top1 = Toplevel()
    top1.geometry("400x300")
    # creating frame
    f2 = Frame(top1, width=400, height=300, bg="yellow")
    f2.place(x=0, y=0)
    # background image
    img_1 = Image.open("back.png")
    img1 = ImageTk.PhotoImage(img_1)
    # Create label to display Image
    L1 = Label(f2, image=img1)
    L1.place(x=0, y=0)
    Label(top1, text="USER LOGGED IN", font=("Arial", 10, "bold")).place(x=150, y=170)

    top1.mainloop()


def reg():
    top2 = Toplevel(bg="#53868B")
    top2.geometry("500x300")
    top2.title("Registration Window")
    u_input = StringVar()
    p_input = StringVar()
    info_user = Label(top2, text="Username", font=10)
    info_user.place(x=50, y=50)

    us_input = Entry(top2, textvariable=u_input, font=10)
    us_input.place(x=170, y=50)

    info_pass = Label(top2, text="Password", font=10)
    info_pass.place(x=50, y=110)
    pa_input = Entry(top2, textvariable=p_input, show='*', font=10)
    pa_input.place(x=170, y=110)


    def user_reg():
        db.co
        r1 = u_input.get()
        r2 = p_input.get()
        db.execute("create table if not exists sreg(username text, password text)")
        command = 'insert into sreg (username,password) values (?,?);'
        a = cur.execute(command, (r1, r2,))
        print(a)
        messagebox.showinfo('info', 'Successfully registered')
        db.commit()
        db.close()

    r_btn = Button(top2, text="Register", bd=5, bg="red", relief="groove", font=10, command=user_reg)
    r_btn.place(x=170, y=180)



main_window = Tk()
main_window.configure(bg="#C1CDCD")
main_window.title("Login")
main_window.geometry("500x300+0+0")
padd = 20
main_window['padx'] = padd
# variables
u_input = StringVar()
p_input = StringVar()
user_input = StringVar()
pass_input = StringVar()
info_label = Label(main_window, text="Login Application", fg="white", bg="blue", bd=5, relief="groove", font=10)
info_label.pack(fill='x')

# f1=Frame(main_window,width=500,height=400)
# f1.place(x=0,y=0)

info_user = Label(main_window, text="Username", font=10)
info_user.place(x=50, y=50)

user_input = Entry(main_window, textvariable=user_input, font=10)
user_input.place(x=170, y=50)

info_pass = Label(main_window, text="Password", font=10)
info_pass.place(x=50, y=110)
pass_input = Entry(main_window, textvariable=pass_input, show='*', font=10)
pass_input.place(x=170, y=110)

login_btn = Button(text="Login", bd=5, bg="red", relief="groove", font=10, command=login)
login_btn.place(x=50, y=180)

reg_btn = Button(text="Register", bd=5, bg="red", relief="groove", font=10, command=reg)
reg_btn.place(x=170, y=180)

clr_btn = Button(text="Clear", bd=5, bg="red", relief="groove", font=10, command=clear)
clr_btn.place(x=320, y=180)

main_window.mainloop()
from tkinter import *
from PIL import ImageTk, Image
import sqlite3
from tkinter import messagebox
from matplotlib import pyplot as plt
from tkinter import ttk

# Create an instance of tkinter window
win = Tk()
win.title("E-VOTING SYSTEM")
bg_color = "#074463"

# variables
user_input = StringVar()
pass_input = StringVar()
sname_input = StringVar()
class_input = StringVar()
post_input = StringVar()
# voter variables
vname_input = StringVar()
vclass_input = StringVar()
vusername_input = StringVar()
vpass_input = StringVar()
vid_input = StringVar()

# student registration variables
stu_name_input = StringVar()
sclass_input = StringVar()
spost_input = StringVar()


# CLEAR
def clear_data():
    op = messagebox.askyesno("Clear", "Do you really want to clear data?")

    user_input.delete(0, END)
    pass_input.delete(0, END)


# Define the geometry of the window
win.geometry("1350x700+0+0")

# main databse
db = sqlite3.connect('vote.db')  # main database
cur = db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS poll
                    (name)""")


# database
def login():
    # db.execute("create table if not exists login(username text,password text,status text)")
    # db.execute("insert into login(username,password,status) VALUES('admin1','a123','admin')")
    # db.execute("insert into login(username,password,status) VALUES('user1','u123','user')")
    # cur.execute("select * from login where username=? AND password=?", (user_input.get(), pass_input.get()))
    cur.execute("select username,password,type from vlogin where username=? AND password=?",
                (user_input.get(), pass_input.get()))
    row = cur.fetchone()
    if row:
        if row[0] == 'admin1':
            admin_panel_window()
            messagebox.showinfo('info', 'login successful')

        else:
            userpanel_window()

    else:
        messagebox.showinfo('info', 'login failed')
    cur.connection.commit()
    # db.close()


# voter login database
def vote_login():
    vname = vname_input.get()
    vclass = vclass_input.get()
    global vuser
    vuser = vusername_input.get()
    vpass = vpass_input.get()
    # vid = vid_input.get()

    db.execute("create table if not exists vlogin(name text,class text, username text,password text)")
    command = 'insert into vlogin (name,class, username,password) values (?,?,?,?);'
    cur.execute(command, (vname, vclass, vuser, vpass))
    messagebox.showinfo("info", "Voter Successfully registered")
    db.commit()
    db.close()


# register window
def register():
    top3 = Toplevel(bg="#074463")
    top3.title("Registration")
    top3.geometry("1000x500+150+80")
    top3.configure(bg="#d7dae2")
    top3.resizable(False, False)
    fr = Frame(top3, width=1000, height=500)
    fr.place(x=0, y=0)
    # background image
    image_12 = Image.open("back1.JPG")
    img12 = ImageTk.PhotoImage(image_12)
    # Create a Label Widget to display the text or Image
    l12 = Label(fr, image=img12)
    l12.place(x=0, y=0)
    # buttons and labels
    title = Label(top3, text="Registration Form", bd=5, relief=GROOVE, bg=bg_color, fg="white",
                  font=("times new roman", 20, "bold",), padx=5, pady=5)
    title.pack(fill=X)

    Label(top3, text='Enter Student Name: ', font='Helvetica 14 bold').place(x=200, y=100)
    Entry(top3, width=30, textvariable=stu_name_input, font='Helvetica 14 bold').place(x=450, y=100)  # poll name

    Label(top3, text='Enter Your Class:  ', font='Helvetica 14 bold').place(x=200, y=150)
    Entry(top3, width=30, textvariable=sclass_input, font='Helvetica 14 bold').place(x=450, y=150)

    Label(top3, text='Enter Post: ', font='Helvetica 14 bold').place(x=200, y=200)
    Entry(top3, width=30, textvariable=spost_input, font='Helvetica 14 bold').place(x=450, y=200)
    sbmt_btn = Button(top3, text="Submit", command=sreg, width=43, bd=7, bg=bg_color, fg="red",
                      font="arial 13 bold")
    sbmt_btn.place(x=300, y=300)

    top3.mainloop()


# student registration form database
def sreg():
    global flag

    student_name = stu_name_input.get()
    sclass = sclass_input.get()
    spost = spost_input.get()
    db.execute("create table if not exists sreg(name text,class text, post text)")
    r_set = db.execute("select name from poll")
    row = cur.fetchone()

    i = 0  # row value inside the loop
    for poll in r_set:
        for j in range(len(poll)):
            if (poll[j] != spost):
                flag = 0
            else:
                flag = 1
        i = i + 1

    if (flag == 0):
        messagebox.showinfo('info', 'Poll does not exists')
    else:
        command = 'insert into sreg (name,class, post) values (?,?,?);'
        cur.execute(command, (student_name, sclass, spost,))
        messagebox.showinfo('info', 'Successfully registered')

    db.commit()
    db.close()


# voter register window
def vote_register():
    win.withdraw()
    v1 = Toplevel(bg="#074463")
    v1.title("Registration")
    v1.geometry("1000x500+150+80")
    v1.configure(bg="#d7dae2")
    v1.resizable(False, False)
    fr = Frame(v1, width=1000, height=500)
    fr.place(x=0, y=0)
    # background image
    image_vt = Image.open("back1.JPG")
    imgvt = ImageTk.PhotoImage(image_vt)
    # Create a Label Widget to display the text or Image
    lvt = Label(fr, image=imgvt)
    lvt.place(x=0, y=0)
    # buttons and labels
    title = Label(v1, text="Voter Registration", bd=5, relief=GROOVE, bg=bg_color, fg="white",
                  font=("times new roman", 20, "bold",), padx=5, pady=5)
    title.pack(fill=X)

    Label(v1, text='Enter Student Name: ', font='Helvetica 14 bold').place(x=200, y=100)
    Entry(v1, width=30, textvariable=vname_input, font='Helvetica 14 bold').place(x=450, y=100)  # poll name

    Label(v1, text='Enter Your Class: ', font='Helvetica 14 bold').place(x=200, y=150)
    Entry(v1, width=30, textvariable=vclass_input, font='Helvetica 14 bold').place(x=450, y=150)

    Label(v1, text='Set Username : ', font='Helvetica 14 bold').place(x=200, y=200)
    Entry(v1, width=30, textvariable=vusername_input, font='Helvetica 14 bold').place(x=450, y=200)

    Label(v1, text='Set Password : ', font='Helvetica 14 bold').place(x=200, y=250)
    Entry(v1, width=30, textvariable=vpass_input, font='Helvetica 14 bold').place(x=450, y=250)

    sbmt_btn = Button(v1, text="Submit", command=vote_login, width=43, bd=7, bg=bg_color, fg="red",
                      font="arial 13 bold")
    sbmt_btn.place(x=300, y=350)

    v1.mainloop()


def userpanel_window():
    win.withdraw()
    top1 = Toplevel(bg="#074463")
    top1.title("User Panel")
    top1.geometry("1250x700+150+80")
    top1.configure(bg="#d7dae2")
    top1.resizable(False, False)
    f2 = Frame(top1, width=1250, height=700)
    f2.place(x=0, y=0)

    # frame for mypolls
    f3 = Frame(top1, width=500, height=400)
    f3.place(x=150, y=150)
    image_7 = Image.open("p2.PNG")
    img7 = ImageTk.PhotoImage(image_7)
    f13 = Frame(top1, width=450, height=400)
    f13.place(x=700, y=150)
    image_13 = Image.open("register.png")
    img13 = ImageTk.PhotoImage(image_13)

    # Create an object of tkinter ImageTk
    image_6 = Image.open("back1.JPG")
    img6 = ImageTk.PhotoImage(image_6)

    # Create a Label Widget to display the text or Image
    l4 = Label(f2, image=img6)
    l4.place(x=0, y=0)
    l5 = Label(f3, image=img7)
    l5.place(x=0, y=0)
    l13 = Label(f13, image=img13)
    l13.place(x=0, y=0)

    # Creating Button
    poll_btn = Button(top1, text="My Polls", command=polls, width=48, bd=7, bg=bg_color, fg="red",
                      font="arial 13 bold")
    poll_btn.place(x=150, y=550)
    register_btn = Button(top1, text="Register", command=register, width=43, bd=7, bg=bg_color, fg="red",
                          font="arial 13 bold")
    register_btn.place(x=700, y=550)

    top1.mainloop()


def admin_panel_window():
    win.withdraw()
    top = Toplevel()
    top.title("Admin Panel")
    top.geometry("1280x720+150+80")
    top.configure(bg="#d7dae2")
    top.resizable(False, False)
    frame2 = Frame(top, width=1350, height=700)
    frame2.place(x=0, y=0)
    frame2.place(anchor="center", relx=0.5, rely=0.5)
    # Create an object of tkinter ImageTk
    image_1 = Image.open("back1.JPG ")
    img = ImageTk.PhotoImage(image_1)

    # Create poll image frame
    frame3 = Frame(top, width=500, height=400)
    frame3.place(x=100, y=100)
    frame4 = Frame(top, width=500, height=400)
    frame4.place(x=650, y=100)
    image_2 = Image.open("p1.PNG")
    img1 = ImageTk.PhotoImage(image_2)
    image_3 = Image.open("p4.PNG")
    img2 = ImageTk.PhotoImage(image_3)

    # Create a Label Widget to display the text or Image
    l1 = Label(frame2, image=img)
    l1.place(x=0, y=0)
    l2 = Label(frame3, image=img1)
    l2.place(x=0, y=0)
    l3 = Label(frame4, image=img2)
    l3.place(x=0, y=0)

    # Creating Button

    create_btn = Button(top, text="Create New Poll", command=create, width=40, bd=7, bg=bg_color, fg="red",
                        font="arial 14 bold")
    create_btn.place(x=100, y=500)
    results_btn = Button(top, text="Poll Results", command=selpl, width=40, bd=7, bg=bg_color, fg="red",
                         font="arial 14 bold")
    results_btn.place(x=650, y=500)
    cand_btn = Button(top, text="Candidate List", command=regcand, width=40, bd=7, bg=bg_color, fg="red",
                      font="arial 14 bold")
    cand_btn.place(x=400, y=600)

    top.mainloop()


# creating Polls
def create():
    def proceed():
        global pcursor

        global vuser
        pname = name.get()  # pollname
        can = cname.get()  # candidatename
        if pname == '':
            return messagebox.showerror('Error', 'Enter poll name')
        elif can == '':
            return messagebox.showerror('Error', 'Enter candidates')

        else:
            candidates = can.split(',')  # candidate list
            command = 'insert into poll (name) values (?);'
            cur.execute(command, (pname,))
            db.commit()
            pd = sqlite3.connect(pname + '.db')  # poll database
            pcursor = pd.cursor()  # poll cursor
            pcursor.execute("""CREATE TABLE IF NOT EXISTS polling
                        (name TEXT,votes INTEGER)""")
            pcursor.execute("""CREATE TABLE IF NOT EXISTS voterlist
                                           (username text)""")

            for i in range(len(candidates)):
                command = 'insert into polling (name,votes) values (?, ?)'
                data = (candidates[i], 0)
                pcursor.execute(command, data)
                pd.commit()
        pd.close()
        messagebox.showinfo('Success!', 'Poll Created')
        cr.destroy()

    name = StringVar()
    cname = StringVar()

    cr = Toplevel(bg="#8B8378")
    cr.geometry('900x400')
    cr.title('Create a new poll')
    frame5 = Frame(cr, width=900, height=700, bg="#8B8378")
    frame5.place(x=0, y=0)
    Label(frame5, text='Enter Details', font='Helvetica 14 bold').grid(row=3, column=2, padx=5, pady=5)
    Label(frame5, text='Enter Poll name: ', font='Helvetica 14 bold').grid(row=4, column=1, padx=5, pady=5)
    Entry(frame5, width=30, textvariable=name, font='Helvetica 14 bold').grid(row=4, column=2, padx=5,
                                                                              pady=5)  # poll name
    Label(frame5, text='(eg:captain elections)', font='Helvetica 9 bold').place(x=670, y=45)
    Label(frame5, text='Enter Candidates: ', font='Helvetica 14 bold').grid(row=5, column=1, padx=5, pady=5)
    Entry(frame5, width=30, textvariable=cname, font='Helvetica 14 bold').grid(row=5, column=2)  # candidate name
    Label(frame5, text='Note: Enter the candidate names one by one by putting commas', font='Helvetica 14 bold').grid(
        row=6, column=2, padx=5, pady=5)
    Label(frame5, text='eg: candidate1,candidate2,candidate3....', font='Helvetica 14 bold').grid(row=7, column=2,
                                                                                                  padx=5,
                                                                                                  pady=5)
    Button(frame5, text='Proceed', command=proceed, bd=7, bg=bg_color, fg="red", font="arial 14 bold").grid(row=10,
                                                                                                            column=2,
                                                                                                            padx=10,
                                                                                                            pady=10)


# Login window
frame = Frame(win, width=1350, height=700)
frame.place(x=0, y=0)
frame.place(anchor="center", relx=0.5, rely=0.5)

title = Label(win, text="E-Voting System", bd=5, relief=GROOVE, bg=bg_color, fg="white",
              font=("times new roman", 20, "bold",), padx=5, pady=5)
title.pack(fill=X)

username = Label(win, text="Username", bd=5, bg=bg_color, fg="white",
                 font=("times new roman", 20, "bold",), padx=5, pady=5)
username.place(x=500, y=300)
user_input = Entry(win, textvariable=user_input, bg=bg_color, fg="white",
                   font=("times new roman", 20, "bold",))
user_input.place(x=700, y=300)
info_pass = Label(win, text="Password", bd=5, bg=bg_color, fg="white",
                  font=("times new roman", 20, "bold",), padx=5, pady=5)
info_pass.place(x=500, y=400)
pass_input = Entry(win, textvariable=pass_input, show='*', relief=GROOVE, bg=bg_color, fg="white",
                   font=("times new roman", 20, "bold",))
pass_input.place(x=700, y=410)

login_btn = Button(win, text="Login", command=login, width=15, bd=7, fg="red", font="arial 12 bold")
login_btn.place(x=450, y=500)

reg_btn = Button(win, text="Register", command=vote_register, width=15, bd=7, fg="red", font="arial 12 bold")
reg_btn.place(x=640, y=500)

clr_btn = Button(win, text="Clear", command=clear_data, width=15, bd=7, fg="red", font="arial 12 bold")
clr_btn.place(x=850, y=500)

# f2=Frame(win,)

# Create an object of tkinter ImageTk
image_0 = Image.open("back1.JPG ")
img = ImageTk.PhotoImage(image_0)

# Create a Label Widget to display the text or Image
label = Label(frame, image=img)
label.place(x=0, y=0)


# Poll results
def selpl():  # pollresults
    def results():
        sel = sele.get()  # selected option
        if sel == '-select-':
            return messagebox.showerror('Error', 'Select Poll')
        else:
            pl.destroy()

            def project():
                names = []
                votes = []
                for i in range(len(r)):
                    data = r[i]
                    names.append(data[0])
                    votes.append(data[1])
                    plt.title('Poll Result')
                plt.pie(votes, labels=names, autopct='%1.1f%%', shadow=True, startangle=140)
                plt.axis('equal')
                plt.show()

            res = Toplevel(bg="#8B8378")  # result-page
            res.geometry('500x400')
            res.title('Results!')
            Label(res, text='Here is the Result!', font='Helvetica 14 bold').grid(row=1, column=2)
            con = sqlite3.connect(sel + '.db')
            pcursor = con.cursor()
            pcursor.execute('select * from polling')
            r = pcursor.fetchall()  # data-raw
            for i in range(len(r)):
                data = r[i]
                Label(res, text=data[0] + ': ' + str(data[1]) + ' votes', font='Helvetica 14 bold', padx=10,
                      pady=10).grid(row=2 + i, column=1)
            Button(res, text='Project Results', font='Helvetica 14 bold', bg=bg_color, fg="red", command=project,
                   padx=10, pady=10).place(x=200, y=200)

    cur.execute('select name from poll')
    data = cur.fetchall()
    pollnames = ['-select-']
    for i in range(len(data)):
        data1 = data[i]
        ndata = data1[0]
        pollnames.append(ndata)
    sele = StringVar()
    pl = Toplevel(bg="#8B8378")
    pl.geometry('500x400')
    pl.title('Voting System')
    Label(pl, text='Select Poll', font='Helvetica 12 bold', padx=10, pady=10).place(x=150, y=30)
    sel = ttk.Combobox(pl, values=pollnames, state='readonly', textvariable=sele, width=50, height=200)
    sel.place(x=10, y=100)
    sel.current(0)
    Button(pl, text='Get Results', command=results).place(x=350, y=100)


# registerd candidates
def regcand():
    r1 = Toplevel(bg="#074463")
    r1.title("Candidate Details")
    r1.geometry("1000x500+150+80")
    r1.configure(bg="#d7dae2")
    r1.resizable(False, False)
    # Create a Treeview Scrollbar
    tree_scroll = Scrollbar(r1)
    tree_scroll.pack(side=RIGHT, fill=Y)

    # Create The Treeview
    my_tree = ttk.Treeview(r1, yscrollcommand=tree_scroll.set, selectmode="extended")
    my_tree.pack()

    # formatting treeview
    style = ttk.Style()
    style.configure("Treeview.Heading", font=(None, 20), rowheight=25)
    style.configure("Treeview", rowheight=25)

    # Define Our Columns
    my_tree['columns'] = ("Name", "Class", "Post")

    # Format Our Columns
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("Name", anchor=W, width=400)
    my_tree.column("Class", anchor=W, width=400)
    my_tree.column("Post", anchor=W, width=400)

    # Create Headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("Name", text=" Name", anchor=W)
    my_tree.heading("Class", text="Class", anchor=W)
    my_tree.heading("Post", text="Post", anchor=W)

    # Configure the Scrollbar
    tree_scroll.config(command=my_tree.yview)

    # Create a database or connect to one that exists
    conn = sqlite3.connect('vote.db')

    # Create a cursor instance
    c = conn.cursor()

    c.execute("SELECT * FROM sreg")
    records = c.fetchall()

    # Add our data to the screen
    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', text='',
                           values=(record[0], record[1], record[2]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', text='',
                           values=(record[0], record[1], record[2]),
                           tags=('oddrow',))
        # increment counter
        count += 1
    # Create Striped Row Tags
    my_tree.tag_configure('oddrow', background="white", font=("Arial", 15))
    my_tree.tag_configure('evenrow', background="lightblue", font=("Arial", 15))

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()
    r1.mainloop()


# creating my polls
def pollpage():  # page for polling
    def proceed():
        global vuser
        # vuser=vusername_input
        chose = choose.get()
        print(chose)
        pd = sqlite3.connect(plname + '.db')  # poll database
        command = 'update polling set votes=votes+1 where name=?'
        pd.execute(command, (chose,))
        pd.commit()
        command = 'insert into voterlist (username)values(?)'
        pd.execute(command, (user_input.get(),))
        # print(command)
        # pd.execute(command1)
        pd.commit()

        pcursor.execute('select count(username) from voterlist where username=?', (user_input.get(),))
        row = pcursor.fetchone()
        print(row)
        if row[0] > 1:
            messagebox.showerror('error', 'You have already voted')
        else:
            messagebox.showinfo('Success!', 'You have voted')
        pd.close()

    # choose = StringVar()
    names = []
    pd = sqlite3.connect(plname + '.db')  # poll database
    pcursor = pd.cursor()  # poll cursor
    pcursor.execute('select name from polling')
    data = pcursor.fetchall()
    for i in range(len(data)):
        data1 = data[i]
        ndata = data1[0]
        names.append(ndata)
    print(names)
    ppage = Toplevel(bg="#FFE4C4")
    ppage.geometry('500x400')
    ppage.title('Poll')
    choose = StringVar(ppage, "1")
    title = Label(ppage, text="Vote for any one person!", bd=5, relief=GROOVE, bg=bg_color, fg="white",
                  font=("times new roman", 15), padx=5, pady=5, justify='center')
    title.grid(row=1, column=6, padx=26, ipady=25)
    # title.pack(fill=X)

    # Label(ppage, text='Vote for any one person!', font='Helvetica 12 bold',relief=GROOVE, padx=20, pady=20).grid(row=1, column=1)
    for i in range(len(names)):
        Radiobutton(ppage, text=names[i], value=names[i], variable=choose, font='Helvetica 12 ', padx=10,
                    pady=25, justify='center').grid(row=2 + i, column=3, padx=40, pady=22)
    Button(ppage, text='Vote', command=proceed, bd=5, bg=bg_color, fg="white", relief=GROOVE, font='Helvetica 20 bold',
           padx=10, pady=10).place(x=200, y=300)
    #


def polls():  # mypolls
    def proceed():
        global plname
        plname = psel.get()
        if plname == '-select-':
            return messagebox.showerror('Error', 'select poll')
        else:
            mpolls.destroy()
            pollpage()

    cur.execute('select name from poll')
    data = cur.fetchall()
    pollnames = ['-select-']
    for i in range(len(data)):
        data1 = data[i]
        ndata = data1[0]
        pollnames.append(ndata)
    psel = StringVar()
    mpolls = Toplevel(bg="#8B8378")
    mpolls.geometry('500x400')
    mpolls.title('Voting Program')
    Label(mpolls, text='Select Poll', font='Helvetica 14 bold', padx=10, pady=10).place(x=150, y=30)
    select = ttk.Combobox(mpolls, values=pollnames, state='readonly', textvariable=psel, width=50, height=200)
    select.place(x=10, y=100)
    select.current(0)
    Button(mpolls, text='Proceed', command=proceed).place(x=350, y=100)


win.mainloop()
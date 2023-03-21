from tkinter import *
import sys
import tkinter.ttk as ttk

import csv
import webbrowser 
def login():
    def command1(event):
        if entry1.get() =='admin' and entry2.get()=='password' or entry1.get()=='test' and entry2.get()== 'pass':
            root.deiconify()
            top.destroy()
            menupage()
            
    def command2():
        top.destroy()
        root.destroy()
        sys.exit()

    root=Tk()
    top=Toplevel()
    top.geometry('855x650')
    top.title('Soccathon Login screen')
    top.configure(background='white')
    photo2=PhotoImage(file='real.gif')
    photo=Label(top, image=photo2, bg='white')
    lbl1=Label(top, text='Username:', font='Helvetica 10')
    entry1= Entry(top)
    lbl2= Label(top, text='Password:', font='Helvetica 10')
    entry2= Entry(top, show='*')
    button1 = Button(top, text="Login", command=lambda:command1(event))
    button2 = Button(top, text="Cancel",command=lambda:command2()) 
    

    entry2.bind('<Return>', command1)
    lbl3=Label(top, text='@Copyright 2020',font =('Arial,8'))
    photo.pack()
    lbl1.pack()
    entry1.pack()
    lbl2.pack()
    entry2.pack()
    button2.pack()
    lbl3.pack()
    #label1.pack()
    button2.pack()
    button1.pack()

    root.withdraw()
    root.mainloop()

def menupage():
    root =Tk()
    root.title('Welcome to the largest soccer platform!')
    root.geometry('900x1200')

    root.iconbitmap('real.ico')
    root.configure(background='green')
    #splsh_img = tk.PhotoImage(file='real.gif',master=root)
    #root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='real.gif'))
    root.geometry("400x400")

    my_menu=Menu(root)
    root.config(menu=my_menu)
    def our_command():
        hide()
        our_command_frame.pack(fill='both', expand=1)
        TableMargin = Frame(our_command_frame, width=100)
        TableMargin.pack(side=TOP)
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
        tree = ttk.Treeview(TableMargin, columns=("Match", "Score", "Stadia"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('Match', text="Match", anchor=W)
        tree.heading('Score', text="Score", anchor=W)
        tree.heading('Stadia', text="Stadia", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=400)
        tree.column('#2', stretch=NO, minwidth=0, width=400)
        tree.column('#3', stretch=NO, minwidth=0, width=500)
        tree.pack()
        with open('test.csv','r') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                Match = row['Match']
                Score = row['Score']
                Stadia = row['Stadia']
                tree.insert("", 0, values=(Match, Score, Stadia))
    
    def our_command1():
        hide()
        our_command1_frame.pack(fill='both', expand=1)
        TableMargin = Frame(our_command1_frame, width=100)
        TableMargin.pack(side=TOP)
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
        tree = ttk.Treeview(TableMargin, columns=("Match", "Score", "Stadia"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('Match', text="Match", anchor=W)
        tree.heading('Score', text="Score", anchor=W)
        tree.heading('Stadia', text="Stadia", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=400)
        tree.column('#2', stretch=NO, minwidth=0, width=400)
        tree.column('#3', stretch=NO, minwidth=0, width=500)
        tree.pack()
        with open('city1.csv','r') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                Match = row['Match']
                Score = row['Score']
                Stadia = row['Stadia']
                tree.insert("", 0, values=(Match, Score, Stadia))
    def our_command2():
        hide()
        our_command2_frame.pack(fill='both', expand=1)
        TableMargin = Frame(our_command2_frame, width=100)
        TableMargin.pack(side=TOP)
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
        tree = ttk.Treeview(TableMargin, columns=("Match", "Score", "Stadia"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('Match', text="Match", anchor=W)
        tree.heading('Score', text="Score", anchor=W)
        tree.heading('Stadia', text="Stadia", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=400)
        tree.column('#2', stretch=NO, minwidth=0, width=400)
        tree.column('#3', stretch=NO, minwidth=0, width=500)
        tree.pack()
        with open('leicester1.csv','r') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                Match = row['Match']
                Score = row['Score']
                Stadia = row['Stadia']
                tree.insert("", 0, values=(Match, Score, Stadia))
    def our_command3():
        hide()
        our_command3_frame.pack(fill='both', expand=1)
        TableMargin = Frame(our_command3_frame, width=100)
        TableMargin.pack(side=TOP)
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
        tree = ttk.Treeview(TableMargin, columns=("Match", "Score", "Stadia"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('Match', text="Match", anchor=W)
        tree.heading('Score', text="Score", anchor=W)
        tree.heading('Stadia', text="Stadia", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=400)
        tree.column('#2', stretch=NO, minwidth=0, width=400)
        tree.column('#3', stretch=NO, minwidth=0, width=500)
        tree.pack()
        with open('chelsea1.csv','r') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                Match = row['Match']
                Score = row['Score']
                Stadia = row['Stadia']
                tree.insert("", 0, values=(Match, Score, Stadia))
    def our_command4():
        hide()
        our_command4_frame.pack(fill='both', expand=1)
        TableMargin = Frame(our_command4_frame, width=100)
        TableMargin.pack(side=TOP)
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
        tree = ttk.Treeview(TableMargin, columns=("Match", "Score", "Stadia"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('Match', text="Match", anchor=W)
        tree.heading('Score', text="Score", anchor=W)
        tree.heading('Stadia', text="Stadia", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=400)
        tree.column('#2', stretch=NO, minwidth=0, width=400)
        tree.column('#3', stretch=NO, minwidth=0, width=500)
        tree.pack()
        with open('tot.csv','r') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                Match = row['Match']
                Score = row['Score']
                Stadia = row['Stadia']
                tree.insert("", 0, values=(Match, Score, Stadia))
    def our_command5():
        hide()
        our_command5_frame.pack(fill='both', expand=1)
        TableMargin = Frame(our_command5_frame, width=100)
        TableMargin.pack(side=TOP)
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
        tree = ttk.Treeview(TableMargin, columns=("Top Scorers", "Goals", "League"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('Top Scorers', text="Top Scorers", anchor=W)
        tree.heading('Goals', text="Goals", anchor=W)
        tree.heading('League', text="League", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=400)
        tree.column('#2', stretch=NO, minwidth=0, width=400)
        tree.column('#3', stretch=NO, minwidth=0, width=500)
        tree.pack()
        with open('stat.csv','r') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                TopScorers = row['Top Scorers']
                Goals = row['Goals']
                League = row['League']
                tree.insert("", 0, values=(TopScorers, Goals, League))
    def our_command6():
        hide()
        our_command6_frame.pack(fill='both', expand=1)
        TableMargin = Frame(our_command6_frame, width=100)
        TableMargin.pack(side=TOP)
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
        tree = ttk.Treeview(TableMargin, columns=("Top Assists", "No.", "League"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('Top Assists', text="Top Assists", anchor=W)
        tree.heading('No.', text="No.", anchor=W)
        tree.heading('League', text="League", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=400)
        tree.column('#2', stretch=NO, minwidth=0, width=400)
        tree.column('#3', stretch=NO, minwidth=0, width=500)
        tree.pack()
        with open('assists.csv','r') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                Match = row['Top Assists']
                Score = row['No.']
                Stadia = row['League']
                tree.insert("", 0, values=(Match, Score, Stadia))

    def hide():
        our_command_frame.pack_forget()
        our_command1_frame.pack_forget()
        our_command2_frame.pack_forget()
        our_command3_frame.pack_forget()
        our_command4_frame.pack_forget()
        our_command5_frame.pack_forget()
        our_command6_frame.pack_forget()
    our_command_frame=Frame(root, width=900, height=1200,bg='red')
    our_command1_frame=Frame(root, width=900, height=1200,bg='red')
    our_command2_frame=Frame(root, width=900, height=1200,bg='red')
    our_command3_frame=Frame(root, width=900, height=1200,bg='red')
    our_command4_frame=Frame(root, width=900, height=1200,bg='red')
    our_command5_frame=Frame(root, width=900, height=1200,bg='red')
    our_command6_frame=Frame(root, width=900, height=1200,bg='red')
    def highlightslaliga():
        webbrowser.open('www.youtube.com/user/laliga')
    def HighlightsPremier():
        webbrowser.open('www.youtube.com/playlist?list=PLQ_voP4Q3cfdsmCD5bmf2nOMWARYqjP40')
    def highlightsSeriaA():
        webbrowser.open('www.youtube.com/user/legacalcioserieatim')
    def livestream():
        webbrowser.open('www.jokerlivestream.net/')
    file_menu=Menu(my_menu)
    my_menu.add_cascade(label="Clubs", menu=file_menu)
    file_menu.add_command(label="MUN FC", command=our_command)
    file_menu.add_separator()
    file_menu.add_command(label="MCFC", command=our_command1)
    file_menu.add_separator()
    file_menu.add_command(label="LFC", command=our_command2)
    file_menu.add_separator()
    file_menu.add_command(label="CFC", command=our_command3)
    file_menu.add_separator()
    file_menu.add_command(label="TOTFC", command=our_command4)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)


    
    second_menu=Menu(my_menu)
    my_menu.add_cascade(label="Statistics", menu=second_menu)
    second_menu.add_separator()
    second_menu.add_command(label="Goals", command=our_command5)
    second_menu.add_separator()
    second_menu.add_command(label="Assists", command=our_command6)
    second_menu.add_separator()
    second_menu.add_command(label="Passes", command=our_command5)
    second_menu.add_separator()
    second_menu.add_command(label="Clean sheets", command=our_command6)

    last_menu=Menu(my_menu)
    my_menu.add_cascade(label="More", menu=last_menu)
    last_menu.add_command(label="Highlights-Premier League", command=HighlightsPremier)
    last_menu.add_separator()
    last_menu.add_command(label="Highlights-La Liga", command=highlightslaliga)
    last_menu.add_separator()
    last_menu.add_command(label="Highlights- Seria A", command=highlightsSeriaA)
    last_menu.add_separator()
    last_menu.add_command(label="Livestream", command=livestream)
    root.mainloop()

login()
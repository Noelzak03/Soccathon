import csv
from tkinter import *
import tkinter.ttk as ttk
def csvstuff():
	root=Tk()
	display = Frame(root, width=500)
	display.pack(side=TOP)
	scrollbarx = Scrollbar(display, orient=HORIZONTAL)
	scrollbary = Scrollbar(display, orient=VERTICAL)
	tree = ttk.Treeview(display, columns=("matches", "scores"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
	scrollbary.config(command=tree.yview)
	scrollbary.pack(side=RIGHT, fill=Y)
	scrollbarx.config(command=tree.xview)
	scrollbarx.pack(side=BOTTOM, fill=X)
	tree.heading('matches', text="matches", anchor=W)
	tree.heading('scores', text="scores", anchor=W)
	tree.column('#0', stretch=NO, minwidth=0, width=0)
	tree.column('#1', stretch=NO, minwidth=0, width=200)
	tree.column('#2', stretch=NO, minwidth=0, width=200)
	tree.pack()
	with open('Manchester.csv','r') as f:
	    reader = csv.DictReader(f, delimiter=',')
	    print(reader)
	    for row in reader:
	        firstname = row['matches']
	        lastname = row['scores']
	        tree.insert("", 0, values=(firstname,lastname))
csvstuff()

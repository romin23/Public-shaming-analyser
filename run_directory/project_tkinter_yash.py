from tkinter import *
import tkinter
import tkinter.messagebox
from tkinter import ttk
import PublicShammingAnalyzer as psa

def task(top, stringVar_username, stringVar_password):
    top.quit()
    
    newTop = Tk()
    newTop.geometry("1800x900")
    username = stringVar_username.get()
    password = stringVar_password.get()
    blocked_users = psa.execute(username, password)
    newTop.mainloop()

    

    print(username)
    print(password)

    

def main():
    
    top = Tk()

    top.title('PUBLIC SHAMMING ANALYZER')
    top.geometry("800x400")
    
    top['bg'] = 'dark red'

    Label(top, text='PUBLIC SHAMMING ANALYZER\n', font=("arabic","20","bold"), bg = 'dark red').grid(row = 0)

    Label(top,text='Userame',font=("arabic","17","bold"),bg='dark red').grid(row = 3, column = 0)
    Label(top,text='Password',font=("arabic","17","bold"),bg='dark red').grid(row = 4, column = 0)

    stringVar_username = tkinter.StringVar()
    stringVar_password = tkinter.StringVar()

    entry_username = Entry(top, textvariable = stringVar_username, font = ("arabic", 17), width = 22).grid(row = 3, column = 1)
    entry_password = Entry(top, textvariable = stringVar_password, font=("arabic", 17),width = 22).grid(row = 4, column = 1)

    Label(top, text = "\n", bg='dark red').grid(row = 5, column = 0)

    btn_login = tkinter.Button(top, text='Login',
    font=("arabic","20","bold"),
    width = 5,
    bg='gold',
    activebackground="black",
    activeforeground="white",
    borderwidth = 10,
    command = lambda: task(top, stringVar_username, stringVar_password)).grid(row = 6, column = 0, columnspan = 2)
    
    top.mainloop()

main()

# #show donated list
# def showstats():
#     stat=Tk()
#     stat.title('show statistics')
#     stat.geometry("1500x1500")
#     stat['bg']='#49A'
#     #Label(stat,text='the blood goups donated till now are :\n',font=("arabic","22","bold"),bg='#49A').grid(row=0)
#     #Label(stat,bg='#49A',text="id firstname   lastname    age      phonenumber        blood group     gender                email id                          remarks     first time \n",font=("arabic","17","bold"),justify=LEFT).grid(row=1)
#     appLabel = Label(stat, text="SHOW DONATED LIST",fg="#06a099", width=40)
#     appLabel.config(font=("Sylfaen", 30))
#     appLabel.pack()

#     tree = ttk.Treeview(stat)
#     tree["columns"] = ("zero","one", "two", "three", "four","five","six","seven","eight","nine","ten")
#     tree.heading("zero",text="ID")
#     tree.heading("one", text="First Name")
#     tree.heading("two", text="Last Name")
#     tree.heading("three", text="Age")
#     tree.heading("four", text="phone no")
#     tree.heading("five", text="blood group")
#     tree.heading("six", text="gender")
#     tree.heading("seven", text="email id")
#     tree.heading("eight", text="renarks")
#     tree.heading("nine", text="first time")   
#     tree.column("zero",width=50,anchor='center')
#     tree.column("one",width=100,anchor="center")
#     tree.column("two",width=100,anchor="center")
#     tree.column("three",width=100,anchor="center")
#     tree.column("four",width=150,anchor="center")
#     tree.column("five",width=100,anchor="center")
#     tree.column("six",width=100,anchor="center")
#     tree.column("seven",width=200,anchor="center")
#     tree.column("eight",width=100,anchor="center")
#     tree.column("nine",width=100,anchor="center")
#   #create databse
#     conn = sqlite3.connect('blooddonaterequiredlist.db')

#     #create cursor
#     c=conn.cursor()
#     c.execute("SELECT *,oid FROM blooddonationlist ;")
#     i = 0

#     for row in c :
#         tree.insert('',"end",i,text="",values=(row[9],row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
#         i = i + 1

#     tree.pack()
#     conn.commit()
#     conn.close()
#     stat.mainloop()
    

# #delete from donated list
# def deleted():
# 	deler = Tk()
# 	deler.title('delete an entry ')
# 	deler.geometry('1500x1500')
# 	deler['bg']='orangered'
# 	delet=Label(deler,text="please enter the id of the entry to be deleted in the below box ",font=('arabic',"20","bold italic"))
# 	delet['bg']='orangered'
# 	delet.grid(row=5,column=5,padx=10,pady=10)
# 	deletr=Entry(deler,font=('arabic',"20","bold italic"),width=23)
# 	deletr.grid(row=15,column=5,padx=10,pady=10)
# 	def deleterow():
# 		#create databse
# 		conn = sqlite3.connect('blooddonaterequiredlist.db')
# 		#create cursor
# 		c=conn.cursor()
# 		#delete a record
# 		c.execute("DELETE from blooddonationlist WHERE oid = " + deletr.get())
# 		conn.commit()
# 		conn.close()
# 		deletr.delete(0,END)
# 		tkinter.messagebox.showinfo("successful","your data has been deleted from the databse ")
# 		deler.destroy()
# 	rowdel=tkinter.Button(deler, text='delete from list',font=('arabic',"20","bold italic"),width=20,bd=5,height=1,bg='red',activebackground="blue",command=deleterow).grid(row=16,column=5)

# #requirement form
# def reqbloodform():
# 	req = Tk()
# 	req.title('blood requirement form')
# 	req.geometry("1500x1500")
# 	req['bg']='dark red'
# 	Label(req,text='\t Please fill the below form :',font=("arabic","20","bold"),bg='dark red').grid(row=0)
# 	Label(req,text='First Name',font=("arabic","17","bold"),bg='dark red').grid(row=3)
# 	Label(req,text='Last Name',font=("arabic","17","bold"),bg='dark red').grid(row=4)
# 	Label(req,text='Age',font=("arabic","17","bold"),bg='dark red').grid(row=5)
# 	Label(req,text='phone number',font=("arabic","17","bold"),bg='dark red').grid(row=6)
# 	Label(req,text='required blood group',font=("arabic","17","bold"),bg='dark red').grid(row=7)
# 	Label(req,text='email id',font=("arabic","17","bold"),bg='dark red').grid(row=18)
# 	Label(req,text='gender',font=("arabic","17","bold"),bg='dark red').grid(row=16)
# 	Label(req,text='ever donated',font=("arabic","17","bold"),bg='dark red').grid(row=19)
# 	r1=Entry(req,font=("arabic",17),width=22)
# 	r2=Entry(req,font=("arabic",17),width=22)
# 	r3=Spinbox(req,from_=18,to=50,width=21,font=("arabic","17","bold"),justify='center')
# 	r4=Entry(req,font=("arabic",17),width=22)
# 	r6=Entry(req,font=("arabic",17),width=22)
# 	r7=Entry(req,font=("arabic",17),width=22)
# 	reqprev = IntVar()
# 	#chkbx=Checkbutton(top,text='previously donated',font=("arabic",17),variable=prev)
# 	#chkbx.grid(row=20,column=1)   
# 	r1.grid(row=3, column=1)
# 	r2.grid(row=4, column=1)
# 	r3.grid(row=5, column=1)
# 	r4.grid(row=6, column=1)
# 	reqgoption = StringVar(req,"1")
# 	valuers = {"Male":"Male","Female":"Female"}
# 	y=16
# 	for(text,value) in valuers.items():
# 		Radiobutton(req,text = text,variable =reqgoption,font=("arabic","17","bold"),selectcolor="green" ,value=value,indicator=0,activebackground="red",background="orange",width=20).grid(row=y,column=1)
# 		y=y+1
# 	reqoption = StringVar(req,"1")
# 	values = {"A+":"A+","A-":"A-","B+":"B+","B-":"B-","O+":"O+","O-":"O-","AB+":"AB+","AB-":"AB-",}
# 	x=7
# 	for(text,value) in values.items():
# 		Radiobutton(req,text = text,variable =reqoption,font=("arabic","17","bold"),selectcolor="green" ,value=value,indicator=0,activebackground="red",background="light blue",width=20).grid(row=x,column=1)
# 		x=x+1
# 	r6.grid(row=18,column=1)
# 	r7.grid(row=19,column=1)
# 	def reqsubmit():
#         #create databse
# 		conn = sqlite3.connect('blooddonaterequiredlist.db')
# 		#create cursor
# 		rc=conn.cursor()
# 		#insert into table
# 		rc.execute("INSERT INTO bloodrequiredlist VALUES (:f_name,:l_name,:age,:phoneno,:bloodgrp,:gender,:emailid,:everdonated)",
# 					{
# 						'f_name':r1.get(),
# 						'l_name':r2.get(),
# 						'age':r3.get(),
# 						'phoneno':r4.get(),
# 						'bloodgrp':reqoption.get(),
# 						'gender':reqgoption.get(),
# 						'emailid':r6.get(),
# 						'everdonated':r7.get()
# 					}
# 				)
# 		conn.commit()
# 		conn.close()
# 		#clear text boxes
# 		r1.delete(0,END)
# 		r2.delete(0,END)
# 		r3.delete(0,END)
# 		r4.delete(0,END)
# 		reqoption.set(None)
# 		reqgoption.set(None)
# 		r6.delete(0,END)
# 		r7.delete(0,END)
# 		#chkbx.deselect()
# 		tkinter.messagebox.showinfo("successful","thank you! your data has been added to the required blood list ")
# 		req.destroy()
# 	sub=tkinter.Button(req,text="submit",activebackground="blue",width=18,height=1,bg='green',font=("arabic","20","bold"),command=reqsubmit).grid(row=23,column=1)
# 	deletetop=tkinter.Button(req,text="close window",activebackground="blue",fg="white",width=18,height=1,bg='black',font=("arabic","20","bold"),command=req.destroy).grid(row=23,column=0)
# #buttons

# #donate form
# b1=tkinter.Button(i, text='Donate Form',font=("arabic","20","bold"),width=20,bd=5,activebackground="black",activeforeground="white",height=2,bg='light blue',command=donateblood,borderwidth=10).grid(row=7,column=1)
# #show donated list
# b2=tkinter.Button(i,text='Show Donated List',font=("arabic","20","bold"),width=20,bd=5,activebackground="black",activeforeground="white",height=2,bg='aqua',command=showstats,borderwidth=10).grid(row=15,column=1)
# #delete from donated list button
# b3=tkinter.Button(i, text='Delete From Donated List',font=("arabic","20","bold"),width=20,bd=5,height=2,bg='blue',activebackground="black",activeforeground="white",command=deleted,justify='center',borderwidth=10).grid(row=30,column=1)
# #request submitted
# b4=tkinter.Button(i,text="Request Submitted",font=("arabic","20","bold"),width=20,bd=5,height=2,bg="light green",activebackground="black",activeforeground="white",command=requestcallback,borderwidth=10,justify='center').grid(row=7,column=2,columnspan=2)
# #already donated
# b5=tkinter.Button(i,text="Already Donated",font=("arabic","20","bold"),width=20,bd=5,height=2,bg="green",activebackground="black",activeforeground="white",command=donatedcallback,borderwidth=10,justify='center').grid(row=15,column=2,columnspan=2)
# #close button
# b6=tkinter.Button(i, text='Close This Window',font=("arabic","20","bold"),width=20,bd=5,height=2,bg='black',fg='white',activebackground="black",activeforeground="white",command=i.destroy,justify='center',borderwidth=10).grid(row=30,column=2,columnspan=2)
# #requirement form
# b7=tkinter.Button(i, text='Required Blood Form ',font=("arabic","20","bold"),width=17,bd=5,height=2,bg='gold',activebackground="black",activeforeground="white",borderwidth=10,command=reqbloodform).grid(row=7,column=4)
# #show req list
# b8=tkinter.Button(i, text='Show Required List ',font=("arabic","20","bold"),width=17,bd=5,height=2,bg='dark orange',activebackground="black",activeforeground="white",borderwidth=10,command=showreq).grid(row=15,column=4)
# #delete from requirement list
# b9=tkinter.Button(i, text='Delete From Req List',font=("arabic","20","bold"),width=17,bd=5,height=2,bg='red',activebackground="black",activeforeground="white",command=deletedreq,justify='center',borderwidth=10).grid(row=30,column=4)
# #create database
# b10=tkinter.Button(i, text='Click Here To Create Database If You Are Using For The First Time',font=("arabic","20","bold"),width=55,bd=5,height=2,bg='pink',activebackground="black",activeforeground="red",command=createdatabase,justify='center',borderwidth=10).grid(row=35,column=1,columnspan=4)

# Label(i,text="\n SPARE ONLY 15 MINUTES AND SAFE A LIFE \nSTARVE A VAMPIRE , DONATE BLOOD" ,font=("arabic","20","italic bold"),bg='maroon',justify='center').grid(row=40,column=1,columnspan=4)
# Label(i,text="YOU DON'T NEED SUPERPOWERS TO BE A HERO ,YOU CAN BECOME ONE BY DONATING BLOOD",font=("arabic","20","bold"),bg='maroon',justify='center').grid(row=41,column=1,columnspan=4)
# i['bg']='maroon'
# i.mainloop()
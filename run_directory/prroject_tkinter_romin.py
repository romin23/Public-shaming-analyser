import tkinter as tk
import PublicShammingAnalyzer as psa

root=tk.Tk()

# setting the windows size
# root.geometry("1500x720")

# declaring string variable
# for storing name and password
name_var=tk.StringVar()
passw_var=tk.StringVar()


# defining a function that will
# get the name and password and
# print them on the screen
def submit():
	usr_name = name_var.get()
	password = passw_var.get()
	# print(usr_name, password)
	blocked_users = psa.execute(usr_name, password)

	for i in range(1000):
		print("Test 1")

	if len(blocked_users) != 0:
		for key, value in blocked_users.items():
			print("Test 2")
			# output_display.insert(0, "Test")
			# output_display.insert((f"User {key} has been unfollowed/Blocked due to following comments flagged as offensive \n {value}"))
    	            
	# name_var.set("")
	# passw_var.set("")

name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))

passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))
passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')

sub_btn=tk.Button(root,text = 'Submit', command = submit)

output_display = tk.Text(root, height=5, width=25, bg='light cyan')

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)
output_display.grid(row=0, column=2)

root.mainloop()

# psa.test()


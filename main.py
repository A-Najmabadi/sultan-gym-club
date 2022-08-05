#Created By Ali Najmabadi and Ghafur Beheshti
# import important Libraries and DB file
import tkinter as TK
from tkinter import DISABLED, LEFT, constants as TK_CONST
from tkinter.tix import COLUMN
import datetime as dt
import database


# body builder Logging in 
def login():
	global id_, password, error, main_frame

	code = id_.get()
	pass_ = password.get()

	try:
		code = int(code)
	except:
		error.config(text="Please Insert Integer :-)", fg='orange')
		return

	body_builder = database.auth(code, pass_)
	if body_builder:
		profile_view(body_builder, code, pass_)
	else:
		error.config(text="Error, Need To Sign Up?", fg='orange')

def sign_up():
	global error

	name_ = name.get()
	family_ = family.get()
	age_ = age.get()
	weight_ = weight.get()
	height_ = height.get()
	password_ = password.get()

	message = ''
	if name_ and age_ and family_ and weight_ and height_ and password_:
		try:
			age_ = int(age_)
			weight_ = float(weight_)
			height_ = float(height_)
		except:
			message += 'Enter Correct Data\n'

		if not 8 <= len(password_) <= 32:
			message += 'Password Must Be Between 8 And 32 Characters\n'
	else:
		message += 'Fill Out All Fields\n'
	
	if message:
		error.config(text=message, fg='orange')
		message = ''
	else:
		new_Id = database.add_bodybuilder(name_, family_, age_, weight_, height_, password_)
		login_view_after(new_Id)
	

def sign_up_view():
	global main_frame, name, family, age, weight, height, password, error  
	for i in main_frame.winfo_children():
		i.destroy()

	error = TK.Label(main_frame, text='', bg='#1F76CC')
	error.place(relx=0.5, rely=0.8, anchor=TK_CONST.CENTER)

	signing = TK.Label(main_frame, text="Signing Up...", bg='#1F76CC', fg='White', font= ('Arial', 15))
	signing.place(relx=0.5, rely=0.1, anchor=TK_CONST.CENTER)	

	sign_up_frame = TK.Frame(main_frame, border=5, bg='#1F76CC')
	sign_up_frame.place(relx=0.5, rely=0.5, anchor=TK_CONST.CENTER)

	name_label = TK.Label(sign_up_frame, text="FisrtName ", bg='#1F76CC', fg='White')
	name_label.grid(row=1, column=0)
	name = TK.Entry(sign_up_frame, width=15)
	name.grid(row=1, column=2)

	family_label = TK.Label(sign_up_frame, text="LastName ", bg='#1F76CC', fg='White')
	family_label.grid(row=2, column=0)
	family = TK.Entry(sign_up_frame, width=15)
	family.grid(row=2, column=2)

	age_label = TK.Label(sign_up_frame, text="Age ", bg='#1F76CC', fg='White')
	age_label.grid(row=3, column=0)
	age = TK.Entry(sign_up_frame, width=15)
	age.grid(row=3, column=2)

	weight_label = TK.Label(sign_up_frame, text="Weight (KG) ", bg='#1F76CC', fg='White')
	weight_label.grid(row=4, column=0)
	weight = TK.Entry(sign_up_frame, width=15)
	weight.grid(row=4, column=2)

	height_label = TK.Label(sign_up_frame, text="Height  (CM) ", bg='#1F76CC', fg='White')
	height_label.grid(row=5, column=0)
	height = TK.Entry(sign_up_frame, width=15)
	height.grid(row=5, column=2)

	password_label = TK.Label(sign_up_frame, text="Password ", bg='#1F76CC', fg='White')
	password_label.grid(row=6, column=0)
	password = TK.Entry(sign_up_frame, width=15)
	password.grid(row=6, column=2)

	submit_button = TK.Button(main_frame,text="Submit",command=sign_up, width=10, bg='#004A95', fg='White')
	submit_button.place(relx=0.5, rely=0.65, anchor=TK_CONST.CENTER)

	back_button = TK.Button(main_frame,text="Back",command=login_view, width=10, bg='#004A95', fg='White')
	back_button.place(relx= 0.5, rely=0.70, anchor=TK_CONST.CENTER)

def edit_profile(id_):
	global main_frame, error_e

	name_ = name_e.get()
	family_ = family_e.get()
	age_ = age_e.get()
	weight_ = weight_e.get()
	height_ = height_e.get()
	pass_ = password_e.get()
	cpass_ = confrimPass_e.get()

	message_ = ''
	if name_ and age_ and family_ and weight_ and height_ and pass_ and cpass_:
		try:
			age_ = int(age_)
			weight_ = float(weight_)
			height_ = float(height_)
		except:
			message_ += 'Enter Correct Data\n'

		if not 8 <= len(pass_) <= 32:
			message_ += 'Password Must Be Between 8 And 32 Characters\n'

		if pass_ != cpass_:
			message_ += 'Passwords Are Not Equal\n'	
	else:
		message_ += 'Fill Out All Fields\n'

	if message_:
		error_e.config(text=message_, fg='orange')
		message_ = ''
		
	else:
		edited_user = database.update_body_builder(id_, name_, family_, age_, weight_, height_, pass_)
		if edited_user:
			profile_view(edited_user, id_, pass_)


def edit_profile_view(user, code, pass_):
	global main_frame, name_e, family_e, age_e, height_e, weight_e, password_e, confrimPass_e, error_e

	for i in main_frame.winfo_children():
		i.destroy()	

	error_e = TK.Label(main_frame, text='', bg='#1F76CC', fg='White')
	error_e.place(relx=0.5, rely=0.8, anchor=TK_CONST.CENTER)

	edit_label = TK.Label(main_frame,text= 'Editing Profile', bg='#1F76CC', fg='White', font= ('Arial', 15))
	edit_label.place(relx= 0.5, rely= 0.2, anchor=TK_CONST.CENTER)

	edit_frame = TK.Frame(main_frame, border=5, bg='#1F76CC')
	edit_frame.place(relx=0.5, rely=0.5, anchor=TK_CONST.CENTER)

	id_label = TK.Label(edit_frame, text="ID", bg='#1F76CC', fg='White')
	id_label.grid(row=0, column=0)
	id_entry = TK.Entry(edit_frame, width=15)
	id_entry.grid(row=0, column=2)
	id_entry.insert(0, code)
	id_entry.config(state='readonly')


	name_label = TK.Label(edit_frame, text="FisrtName ", bg='#1F76CC', fg='White')
	name_label.grid(row=1, column=0)
	name_e = TK.Entry(edit_frame, width=15)
	name_e.grid(row=1, column=2)
	name_e.insert(0, user.name)

	family_label = TK.Label(edit_frame, text="LastName ", bg='#1F76CC', fg='White')
	family_label.grid(row=2, column=0)
	family_e = TK.Entry(edit_frame, width=15)
	family_e.grid(row=2, column=2)
	family_e.insert(0, user.family)

	age_label = TK.Label(edit_frame, text="Age ", bg='#1F76CC', fg='White')
	age_label.grid(row=3, column=0)
	age_e = TK.Entry(edit_frame, width=15)
	age_e.grid(row=3, column=2)
	age_e.insert(0, user.age)

	weight_label = TK.Label(edit_frame, text="Weight (KG) ", bg='#1F76CC', fg='White')
	weight_label.grid(row=4, column=0)
	weight_e = TK.Entry(edit_frame, width=15)
	weight_e.grid(row=4, column=2)
	weight_e.insert(0, user.weight)

	height_label = TK.Label(edit_frame, text="Height  (CM) ", bg='#1F76CC', fg='White')
	height_label.grid(row=5, column=0)
	height_e = TK.Entry(edit_frame, width=15)
	height_e.grid(row=5, column=2)
	height_e.insert(0, user.height)

	password_label = TK.Label(edit_frame, text="Password ", bg='#1F76CC', fg='White')
	password_label.grid(row=6, column=0)
	password_e = TK.Entry(edit_frame, width=15)
	password_e.grid(row=6, column=2)
	password_e.insert(0, pass_)

	confrimPass_label = TK.Label(edit_frame, text="Confrim Password ", bg='#1F76CC', fg='White')
	confrimPass_label.grid(row=7, column=0)
	confrimPass_e = TK.Entry(edit_frame, width=15)
	confrimPass_e.grid(row=7, column=2)

	label = TK.Label(edit_frame, text= '', bg='#1F76CC', fg='White')
	label.grid(row=8, column=2)

	back_button = TK.Button(edit_frame,text="Back To Profile",command=  lambda: profile_view(user, code, pass_), bg='#004A95', fg='White')
	back_button.grid(row= 9, column=2)

	save_button = TK.Button(edit_frame,text="Save Changes",command= lambda: edit_profile(code), bg='#004A95', fg='White')
	save_button.grid(row= 9, column=0)

def delete_account(code):
	database.delete_account(code)
	login_view()

def delete_account_view(user, code, pass_):
	for i in main_frame.winfo_children():
		i.destroy()

	alert_label = TK.Label(main_frame,text= 'Do You Really Want To Delete Your Account?\n ((This Can Not Be Undone!))', fg='orange' , bg='#1F76CC', font= ('Arial', 15))
	alert_label.place(relx= 0.5, rely= 0.35, anchor=TK_CONST.CENTER)	

	delete_frame = TK.Frame(main_frame, border=5, bg='#1F76CC')
	delete_frame.place(relx=0.5, rely=0.5, anchor=TK_CONST.CENTER)

	delete_account_button = TK.Button(delete_frame, text= 'Yes! Delete My Account', command=lambda: delete_account(code), width=25, bg='#004A95', fg='White')
	back_button = TK.Button(delete_frame, text= 'No! Back To Profile', command= lambda: profile_view(user, code, pass_), width=25, bg='#004A95', fg='White')

	delete_account_button.pack()
	back_button.pack()

def profile_view(user, code, pass_):
	global main_frame

	for i in main_frame.winfo_children():
		i.destroy()
	
	# TK.Label(main_frame, text='this is a test').pack()
	welcome_label = TK.Label(main_frame,text= 'Happy To See You %s %s' % (user.name, user.family), bg='#1F76CC', fg='White', font= ('Arial', 15))
	welcome_label.place(relx= 0.5, rely= 0.1, anchor=TK_CONST.CENTER)

	date = dt.datetime.now()
	date_label = TK.Label(main_frame, text=f"{date:%A, %B %d, %Y}", bg='#1F76CC', fg='White')
	date_label.place(relx=0.5, rely= 0.9, anchor=TK_CONST.CENTER)

	options_frame = TK.Frame(main_frame, border=5, bg='#1F76CC')
	options_frame.place(relx=0.25, rely=0.5, anchor=TK_CONST.CENTER)

	data_frame = TK.Frame(main_frame, border=5, bg='#1F76CC')
	data_frame.place(relx=0.75, rely=0.5, anchor=TK_CONST.CENTER)

	edit_profile_button = TK.Button(options_frame, text='Edit Profile', command= lambda: edit_profile_view(user, code, pass_), width=15, bg='#004A95', fg='White') # SHOULD NOT BE None
	edit_profile_button.pack()

	choose_coach_button = TK.Button(options_frame, text='Choose Coach', command= lambda: get_coach_view(user, code, pass_), width=15, bg='#004A95', fg='White') # SHOULD NOT BE None
	choose_coach_button.pack()

	choose_program_button = TK.Button(options_frame, text='Choose Program', command= lambda: get_program_view(user, code, pass_), width=15, bg='#004A95', fg='White') # SHOULD NOT BE None
	choose_program_button.pack()

	delete_account_button = TK.Button(options_frame, text='Delete Account', command=lambda: delete_account_view(user, code, pass_), width=15, bg='#004A95', fg='White') # SHOULD NOT BE None
	delete_account_button.pack()

	log_out_button = TK.Button(options_frame, text='Log Out', command=login_view, width=15, bg='#004A95', fg='White')
	log_out_button.pack()


	TK.Label(data_frame, text=('FisrtName: %s' % user.name), bg='#1F76CC', fg='White').pack()
	TK.Label(data_frame, text=('LastName: %s' % user.family), bg='#1F76CC', fg='White').pack()
	TK.Label(data_frame, text=('Age: %s' % user.age), bg='#1F76CC', fg='White').pack()
	TK.Label(data_frame, text=('Weight: %s' % user.weight ), bg='#1F76CC', fg='White').pack()
	TK.Label(data_frame, text=('Height: %s' % user.height), bg='#1F76CC', fg='White').pack()
	TK.Label(data_frame, text= 'Coach ID: %s' % user.coach, bg='#1F76CC', fg='White').pack()
	TK.Label(data_frame, text= 'Program ID: %s' % user.program, bg='#1F76CC', fg='White').pack()

	# print('inside proflie')

def get_coach(code, c_id, pass_):
	_message = ''
	# answer = database.choose_coach(code, c_id)
	if c_id:
		try:
			c_id = int(c_id)
			l_coaches = database.get_coach_ids()

			coaches = []
			for coach in l_coaches:
				coaches.append(coach[0])

			if c_id in coaches:
				answer = database.choose_coach(code, c_id)
				if answer:
					profile_view(answer, code, pass_)
			else:
				_message += 'The Entered Number Is Not In Given Data\n'
			
				
		except:
			_message += 'Enter Integer\n'
	else:
		_message += 'Fill Out Field\n'	
	
	if _message:
		_error.config(text=_message, fg='orange')
		


def get_coach_view(user, code, pass_):
	global main_frame, name__, family__, id_c, age__, _error

	for i in main_frame.winfo_children():
		i.destroy()

	get_coach_label = TK.Label(main_frame,text= 'Enter The ID Of Your Selected Coach', bg='#1F76CC', fg='White', font= ('Arial', 15))
	get_coach_label.place(relx= 0.5, rely= 0.2, anchor=TK_CONST.CENTER)

	coach_frame = TK.Frame(main_frame, border=5, bg='#1F76CC')
	coach_frame.place(relx=0.5, rely=0.5, anchor=TK_CONST.CENTER)

	list_of_coaches = database.get_coach()


	columner = 1
	if list_of_coaches:
		cID_label = TK.Label(coach_frame, text="Coach ID", bg='#1F76CC', fg='White')
		cID_label.grid(row=0, column=0)

		cname_label = TK.Label(coach_frame, text="Name", bg='#1F76CC', fg='White')
		cname_label.grid(row=1, column=0)

		cfamily_label = TK.Label(coach_frame, text="Family", bg='#1F76CC', fg='White')
		cfamily_label.grid(row=2, column=0)

		cage_label = TK.Label(coach_frame, text="Age", bg='#1F76CC', fg='White')
		cage_label.grid(row=3, column=0)
		for IDS in list_of_coaches:
			button = TK.Button(coach_frame, text=IDS[2], command=None, state=DISABLED, height=1, width=15, bg='#FFFFFF')
			button.grid(row= 0, column=columner)

			name_button = TK.Button(coach_frame, text=IDS[0], command=None, state=DISABLED, height=1, width=15, bg='#FFFFFF')
			name_button.grid(row= 1, column=columner)

			family_button = TK.Button(coach_frame, text=IDS[1], command=None, state=DISABLED, height=1, width=15, bg='#FFFFFF')
			family_button.grid(row= 2, column=columner)

			age_button = TK.Button(coach_frame, text=IDS[3], command=None, state=DISABLED, height=1, width=15, bg='#FFFFFF')
			age_button.grid(row= 3, column=columner)

			columner += columner

		null_label = TK.Label(coach_frame, text= '', bg='#1F76CC', fg='White')
		null_label.grid(row=5, column=4)

		# alert_label = TK.Label(coach_frame, bg='#1F76CC', fg='White')
		# alert_label.grid(row=6, column=4)

		# select_label = TK.Label(coach_frame, text= 'Enter Your Coach ID: ')
		# select_label.grid(row=7, column=2)

		_error = TK.Label(coach_frame, text="", bg='#1F76CC', fg='White')
		_error.place(relx=0.54, rely=0.6, anchor=TK_CONST.CENTER)

		s_coach = TK.Entry(coach_frame, width=15)
		s_coach.grid(row=7, column=4)

		null_label = TK.Label(coach_frame, text= '', bg='#1F76CC', fg='White')
		null_label.grid(row=8, column=4)

		submit_button = TK.Button(coach_frame, text= 'Submit', width=15, command=lambda: get_coach(code, s_coach.get(), pass_), bg='#004A95', fg='White')
		submit_button.grid(row=9, column=4)

		back_button_ = TK.Button(coach_frame, text="Back To Profile", width=15, command=lambda: profile_view(user, code, pass_), bg='#004A95', fg='White')
		back_button_.grid(row=10, column=4)

	else:
		error_d = TK.Label(main_frame, text="There Is No Coach To See! Check This Later...", bg='#1F76CC', fg='White')
		error_d.place(relx=0.5, rely=0.8, anchor=TK_CONST.CENTER)

		back_button_1 = TK.Button(coach_frame, text="Back", command=  lambda: profile_view(user, code, pass_), width=10, bg='#004A95', fg='White')
		back_button_1.grid(row= 3, column=4)
	


def choose_program(id, code, pass_):
	answer = database.choose_program(id, code)

	if answer:
		profile_view(answer, code, pass_)

def show_program(program, user, code, pass_):
	# for i in program_frame.winfo_children():
	# 	i.destroy()
	
	null_label2 = TK.Label(program_frame, text= '', bg='#1F76CC', fg='White')
	null_label2.grid(row=3, column=p_columner//2)
	null_label2.grid(row=3, column=p_columner//2-1)

	back_button_0.destroy()

	ID_label = TK.Button(program_frame,width=10, state=DISABLED, text= 'Program ID:')
	ID_label.grid(row=4, column=p_columner//2-1)

	sat_label = TK.Button(program_frame,width=10, state=DISABLED, text= 'Saturday:')
	sat_label.grid(row=5, column=p_columner//2-1)

	sun_label = TK.Button(program_frame,width=10, state=DISABLED, text= 'Sunday:')
	sun_label.grid(row=6, column=p_columner//2-1)

	mon_label = TK.Button(program_frame,width=10, state=DISABLED, text= 'Monday:')
	mon_label.grid(row=7, column=p_columner//2-1)

	tue_label = TK.Button(program_frame,width=10, state=DISABLED, text= 'Tuesday:')
	tue_label.grid(row=8, column=p_columner//2-1)

	wed_label = TK.Button(program_frame,width=10, state=DISABLED, text= 'Wednesday:')
	wed_label.grid(row=9, column=p_columner//2-1)

	thu_label = TK.Button(program_frame,width=10, state=DISABLED, text= 'Thursday:')
	thu_label.grid(row=10, column=p_columner//2-1)

	fri_label = TK.Button(program_frame,width=10, state=DISABLED, text= 'Friday:')
	fri_label.grid(row=11, column=p_columner//2-1)

	_id_button = TK.Button(program_frame, text=program.id, command= None, width=10, state=DISABLED)
	_id_button.grid(row= 4, column=p_columner//2)

	sat_button.config(text=program.sat, command= None, width=10, height=1, state=DISABLED)
	sat_button.grid(row=5, column=p_columner//2)

	sun_button.config(text=program.sun, command= None, width=10, height=1, state=DISABLED)
	sun_button.grid(row=6, column=p_columner//2)

	mon_button.config(text=program.mon, command= None, width=10, height=1, state=DISABLED)
	mon_button.grid(row=7, column=p_columner//2)

	tue_button.config(text=program.tue, command= None, width=10, height=1, state=DISABLED)
	tue_button.grid(row=8, column=p_columner//2)

	wed_button.config(text=program.wed, command= None, width=10, height=1, state=DISABLED)
	wed_button.grid(row=9, column=p_columner//2)

	thu_button.config(text=program.thu, command= None, width=10, height=1, state=DISABLED)
	thu_button.grid(row=10, column=p_columner//2)

	fri_button.config(text=program.fri, command= None, width=10, height=1, state=DISABLED)
	fri_button.grid(row=11, column=p_columner//2)

	_submit_button.config(text='Submit', command= lambda: choose_program(program.id, code, pass_), width=10, height=1, bg='#004A95', fg='White')
	_submit_button.grid(row=12, column=p_columner//2)

	back_button = TK.Button(program_frame, text="Back", command=  lambda: profile_view(user, code, pass_), width=10, bg='#004A95', fg='White')
	back_button.grid(row= 12, column=p_columner//2-1)


def get_program(id, user, code, pass_):
	_message_ = ''
	# answer = database.choose_coach(code, c_id)
	if id:
		try:
			id_ = int(id)

			l_programs = database.get_program()

			programs = []
			for program in l_programs:
				programs.append(program[0])

			if id_ in programs:
				Program = database.show_program(id_)
				if Program:
					show_program(Program, user, code, pass_)
			# 	program = database.show_program(id_)	
			# 	if program:
			# 		show_program(program, user, code, pass_)
			else:
				_message_ += 'The Entered Number Is More Or Less Than Given Data\n'	
		except:
			_message_ += 'Enter Integer\n'
	else:
		_message_ += 'Fill Out Field\n'	
	
	if _message_:
		_error_.config(text=_message_, fg='orange')
		

def get_program_view(user, code, pass_):
	global back_button_0,_error_, p_columner,  main_frame, program_frame, sat_button, sun_button, mon_button, tue_button, wed_button, thu_button, fri_button, _submit_button

	
	for i in main_frame.winfo_children():
		i.destroy()

	program_label = TK.Label(main_frame,text= 'Enter ID Of A Prgram To See Details', bg='#1F76CC', fg='White', font= ('Arial', 15))
	program_label.place(relx= 0.5, rely= 0.1, anchor=TK_CONST.CENTER)

	program_frame = TK.Frame(main_frame, border=5, bg='#1F76CC')
	program_frame.place(relx=0.5, rely=0.6, anchor=TK_CONST.CENTER)

	_error_ = TK.Label(main_frame, text='', bg='#1F76CC', fg='White')
	_error_.place(relx=0.5, rely=0.99, anchor=TK_CONST.CENTER)

	# id_label = TK.Label(program_frame, text="ID")
	# id_label.grid(row=0, column=0)
	# id_entry = TK.Entry(program_frame, width=15)
	# id_entry.grid(row=0, column=2)
	search_entry = TK.Entry(program_frame, width=10)
	search_button = TK.Button(program_frame,text='Search',command= None, width=10, height=1, bg='#004A95', fg='White')
	null_label = TK.Label(program_frame, text= '', bg='#1F76CC', fg='White')
	

	#days
	sat_button = TK.Button(program_frame,text='',command= None, width=10, height=1)
	sun_button = TK.Button(program_frame,text='',command= None, width=10, height=1)
	mon_button = TK.Button(program_frame,text='',command= None, width=10, height=1)
	tue_button = TK.Button(program_frame,text='',command= None, width=10, height=1)
	wed_button = TK.Button(program_frame,text='',command= None, width=10, height=1)
	thu_button = TK.Button(program_frame,text='',command= None, width=10, height=1)
	fri_button = TK.Button(program_frame,text='',command= None, width=10, height=1)
	_submit_button = TK.Button(program_frame,text='',command= None, width=10, height=1)

	list_of_programs = database.get_program()
	p_columner = 0
	if list_of_programs:
		for id in list_of_programs:
			ID_button = TK.Button(program_frame, text=id[0], command=None, state=DISABLED, height=1, width=10)
			ID_button.grid(row= 0, column=p_columner)
			p_columner += 1

		if p_columner == 0 or p_columner == 1:
			p_columner = 2	

		null_label.grid(row=1, column=2)
		search_button.grid(row=2, column=p_columner//2)		
		search_entry.grid(row=2, column=p_columner//2-1)
		search_button.config(command=lambda: get_program(search_entry.get(), user, code, pass_), bg='#004A95', fg='White')
	
	else:
		error_d = TK.Label(main_frame, text="There Is No Program To See! Check This Later...", bg='#1F76CC', fg='White')
		error_d.place(relx=0.5, rely=0.8, anchor=TK_CONST.CENTER)

	back_button_0 = TK.Button(program_frame, text="Back", command=  lambda: profile_view(user, code, pass_), width=10, bg='#004A95', fg='White')
	back_button_0.grid(row= 3, column=p_columner//2)


	# program_label = TK.Label(program_frame, text="Program: ")
	# program_label.grid(row=1, column=0)

	# null_label = TK.Label(program_frame, text= '')
	# null_label.grid(row=8, column=2)

	# back_button = TK.Button(program_frame,text="Back To Profile",command=  lambda: profile_view(user, code, pass_))
	# back_button.grid(row= 9, column=2)

	# search_button = TK.Button(program_frame,text="Search program",command= get_program)
	# search_button.grid(row= 9, column=0)

	# search_button = TK.Button(program_frame,text="Submit program",command= get_program)
	# search_button.grid(row= 9, column=1)

def login_view_after(new_Id):
	global main_frame, id_, password, error
	for i in main_frame.winfo_children():
		i.destroy()

	welcome = TK.Label(main_frame, text="Welcome Champion!", bg='#1F76CC', fg='White', font= ('Arial', 20))
	welcome.place(relx=0.5, rely=0.3, anchor=TK_CONST.CENTER)

	new_ID_Label = TK.Label(main_frame, text="Your New ID Is %s" %new_Id, bg='#1F76CC', fg='White')
	new_ID_Label.place(relx=0.5, rely=0.35, anchor=TK_CONST.CENTER)

	inputs_frame = TK.Frame(main_frame, border=5, bg='#1F76CC')
	inputs_frame.place(relx=0.5, rely=0.5, anchor=TK_CONST.CENTER)

	id_label = TK.Label(inputs_frame, text="ID ", bg='#1F76CC', fg='White')
	id_label.grid(row=1, column=0)
	id_ = TK.Entry(inputs_frame, width=10)
	id_.grid(row=1, column=2)

	password_label = TK.Label(inputs_frame, text="Password ", bg='#1F76CC', fg='White')
	password_label.grid(row=2, column=0)
	password = TK.Entry(inputs_frame, width=10, show= '*')
	password.grid(row=2, column=2)

	login_button = TK.Button(main_frame,text="Enter",command=login, bg='#004A95', fg='White')
	login_button.place(relx=0.48, rely=0.6, anchor=TK_CONST.CENTER)

	sign_up_button = TK.Button(main_frame,text="Sign Up",command=sign_up_view, bg='#004A95', fg='White')
	sign_up_button.place(relx=0.55, rely=0.6, anchor=TK_CONST.CENTER)

	error = TK.Label(main_frame, text="", bg='#1F76CC', fg='White')
	error.place(relx=0.5, rely=0.8, anchor=TK_CONST.CENTER)

	direction_label = TK.Label(main_frame, text='Created By Ali Najmabadi and Ghafur Beheshti', bg='#1F76CC', fg='White')
	direction_label.place(relx=0.5, rely=0.95, anchor=TK_CONST.CENTER)


def login_view():
	global main_frame, id_, password, error
	for i in main_frame.winfo_children():
		i.destroy()

	welcome = TK.Label(main_frame, text="Welcome Champion!", bg='#1F76CC', fg='White', font= ('Arial', 20))
	welcome.place(relx=0.5, rely=0.3, anchor=TK_CONST.CENTER)

	inputs_frame = TK.Frame(main_frame, border=5, bg='#1F76CC')
	inputs_frame.place(relx=0.5, rely=0.5, anchor=TK_CONST.CENTER)

	id_label = TK.Label(inputs_frame, text="ID ", bg='#1F76CC', fg='White')
	id_label.grid(row=1, column=0)
	id_ = TK.Entry(inputs_frame, width=10)
	id_.grid(row=1, column=2)

	password_label = TK.Label(inputs_frame, text="Password ", bg='#1F76CC', fg='White')
	password_label.grid(row=2, column=0)
	password = TK.Entry(inputs_frame, width=10, show= '*')
	password.grid(row=2, column=2)

	login_button = TK.Button(main_frame,text="Enter",command=login, bg='#004A95', fg='White')
	login_button.place(relx=0.48, rely=0.6, anchor=TK_CONST.CENTER)

	sign_up_button = TK.Button(main_frame,text="Sign Up",command=sign_up_view, bg='#004A95', fg='White')
	sign_up_button.place(relx=0.55, rely=0.6, anchor=TK_CONST.CENTER)

	error = TK.Label(main_frame, text="", bg='#1F76CC')
	error.place(relx=0.5, rely=0.8, anchor=TK_CONST.CENTER)

	direction_label = TK.Label(main_frame, text='Created By Ali Najmabadi and Ghafur Beheshti', bg='#1F76CC', fg='White')
	direction_label.place(relx=0.5, rely=0.95, anchor=TK_CONST.CENTER)



main_window = TK.Tk()
main_window.geometry("800x600")
main_window.resizable(False, False)
main_window.title('Sultan Club House')
main_window.iconbitmap('gym_icon.ico')

main_frame = TK.Frame(main_window, borderwidth=10, bg='#1F76CC')
main_frame.pack(fill=TK_CONST.BOTH, expand=1)


# start of the progarm:
login_view()
	
main_window.mainloop()

#Created By Ali Najmabadi and Ghafur Beheshti
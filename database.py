import sqlite3 as SQL
#Created By Ali Najmabadi and Ghafur Beheshti

COACH_TABLE = """
	CREATE TABLE IF NOT EXISTS Coach(
		name nvarchar(150) not null,
		family nvarchar(150) not null,
		id INTEGER primary key not null,
		age INTEGER not null,
		date_of_start text not null
	)
"""

PROGRAM_TABLE = """
	CREATE TABLE IF NOT EXISTS Program(
		id INTEGER primary key not null,
		sat text,
		sun text,
		mon text,
		tue text,
		wed text,
		thu text,
		fri text
	)
"""

BODY_BUILDER_TABLE = """
	CREATE TABLE IF NOT EXISTS BodyBuilder(
		name nvarchar(150) not null,
		family nvarchar(150) not null,
		id INTEGER primary key not null,
		age INTEGER not null,
		weight REAL not null,
		height REAL not null,
		password nvarchar(32) not null,
		coach INTEGER,
		program INTEGER,

		foreign key(coach)
			references Coach(id)
			on delete SET NULL
			on update CASCADE
		
		foreign key(program)
			references Program(id)
			on delete SET NULL
			on update CASCADE
	)
"""


class BodyBuilder:
	def __init__(self, name, family, id, age, weight, height, password, coach, program=None):
		self.name = name
		self.family = family
		self.id = id
		self.age = age
		self.weight = weight
		self.height = height
		self.password = password
		self.coach = coach
		self.program = program

	# class new_BodyBuilder(id):
	# 	id = id	

class Coach:
	def __init__(self, name, family, id, age, date_of_start):
		self.name = name
		self.family = family
		self.id = id
		self.age = age
		self.date_of_start = date_of_start

class Program:
	def __init__(self, id,  sat, sun, mon, tue, wed, thu, fri):
		self.id  = id
		self.sat = sat
		self.sun = sun
		self.mon = mon
		self.tue = tue
		self.wed = wed
		self.thu = thu
		self.fri = fri		

def auth(id, password):
	conn = SQL.connect('db.sqlite3')
	cursor = conn.cursor()
	cursor.execute('PRAGMA foreign_keys=ON')
	cursor.execute("select * from BodyBuilder where id = ? AND password = ?", (id, password))
	data = cursor.fetchone()
	conn.close()

	if data:
		body_builder = BodyBuilder(*data)
		return body_builder
	else:
		return False

def delete_account(code):
	conn = SQL.connect('db.sqlite3')
	cursor = conn.cursor()
	cursor.execute('PRAGMA foreign_keys=ON')
	cursor.execute('delete from BodyBuilder where id = ?', (code, ))
	conn.commit()
	conn.close()


def add_bodybuilder(name, family, age, weight, height, password):
	conn = SQL.connect('db.sqlite3')
	cursor = conn.cursor()
	cursor.execute('PRAGMA foreign_keys=ON')
	cursor.execute('insert into BodyBuilder(name, family, age, weight, height, password) VALUES(?, ?, ?, ?, ?, ?)', (name, family, age, weight, height, password))
	conn.commit()

	cursor.execute('select id from BodyBuilder where name = ? AND family = ? AND age = ? AND weight = ? AND height = ? AND password = ?', (name, family, age, weight, height, password))
	data = cursor.fetchone()
	conn.close()

	if data:
		return str(*data)

def choose_program(id, code):
	conn = SQL.connect('db.sqlite3')
	cursor = conn.cursor()
	cursor.execute('PRAGMA foreign_keys=ON')
	cursor.execute('update BodyBuilder set program = ? where id = ?' , (id, code))
	conn.commit()

	cursor.execute('select * from BodyBuilder where id = ?', (code,))
	data = cursor.fetchone()
	conn.close()

	if data:
		body_builder = BodyBuilder(*data)
		
		return body_builder
	else:
		return False	



def get_program():
	conn = SQL.connect('db.sqlite3')
	cursor = conn.cursor()
	cursor.execute('PRAGMA foreign_keys=ON')
	cursor.execute('select id from Program')
	data = cursor.fetchall()
	conn.close()
	if data:
		return data

def show_program(id):
	conn = SQL.connect('db.sqlite3')
	cursor = conn.cursor()
	cursor.execute('PRAGMA foreign_keys=ON')
	cursor.execute('select * from Program where id = ?', (id, ))
	data = cursor.fetchone()
	
	if data:
		program = Program(*data)
		return program
	else:
		return False	

def get_coach():
	conn = SQL.connect('db.sqlite3')
	cursor = conn.cursor()
	cursor.execute('PRAGMA foreign_keys=ON')
	cursor.execute('select * from coach ')
	data = cursor.fetchall()
	conn.close()

	if data:
		return data

def get_coach_ids():
	conn = SQL.connect('db.sqlite3')
	cursor = conn.cursor()
	cursor.execute('PRAGMA foreign_keys=ON')
	cursor.execute('select id from coach ')
	data = cursor.fetchall()
	conn.close()

	if data:
		return data		

def choose_coach(_id, cId):
	conn = SQL.connect('db.sqlite3')
	cursor = conn.cursor()
	cursor.execute('PRAGMA foreign_keys=ON')
	# cursor.execute('PRAGMA foreign_keys=OFF')
	cursor.execute('update BodyBuilder set coach = ? where id = ?' , (cId, _id))
	# cursor.execute('PRAGMA foreign_keys=ON')
	conn.commit()

	cursor.execute('select * from BodyBuilder where id = ?', (_id,))
	data = cursor.fetchone()
	conn.close()

	if data:
		body_builder = BodyBuilder(*data)
		
		return body_builder
	else:
		return False	




def update_body_builder(id_, name, family, age, weight, height, password):
	conn = SQL.connect('db.sqlite3')
	cursor = conn.cursor()
	cursor.execute('PRAGMA foreign_keys=ON')
	cursor.execute('update BodyBuilder set name = ?, family = ?, age = ?, weight = ?, height = ?, password = ? where id = ?', (name, family, age, weight, height, password, id_))
	conn.commit()

	cursor.execute('select * from BodyBuilder where id = ?', (id_,))
	data = cursor.fetchone()
	conn.close()

	if data:
		body_builder = BodyBuilder(*data)
		
		return body_builder
	else:
		
		return False



if __name__ == "__main__":

	conn = SQL.connect('db.sqlite3')
	cursor = conn.cursor()
	cursor.execute('PRAGMA foreign_keys=ON')
	cursor.execute(COACH_TABLE)
	cursor.execute(PROGRAM_TABLE)
	cursor.execute(BODY_BUILDER_TABLE)

	
	conn.close()
	#Created By Ali Najmabadi and Ghafur Beheshti





import sqlite3
conn = sqlite3.connect('questions database.db')
curosr = conn.cursor()
curosr.execute("create table if not exists time_q (id INTEGER PRIMARY KEY,  question text, opt1, opt2, opt3, opt4, answer)")
ques= input("enter question: ")
opt1= input("opt1: ")
opt2= input("opt2: ")
opt3= input("opt3: ")
opt4= input("opt4: ")
answer= input("answer: ")

curosr.execute("insert into time_q (question, opt1, opt2, opt3, opt4, answer) values (?, ?, ?, ?, ?, ?)",
        (ques, opt1, opt2, opt3, opt4, answer))


curosr.execute("SELECT * FROM time_q ")
x=curosr.fetchall()
print(x)
curosr.execute("SELECT opt1, opt2 FROM time_q WHERE opt4= '{}'".format(opt4))
x=curosr.fetchone()
print(x[1])
conn.commit()
conn.close()
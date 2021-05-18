import sqlite3
from datetime import date

#current_date = date.today()

# class Database:
db = "alltasks.db"
dbase = sqlite3.connect(db)
dbase.execute(""" CREATE TABLE IF NOT EXISTS task_tables(id INTEGER PRIMARY KEY AUTOINCREMENT, task_name VARCHAR(25),message TEXT) """)
dbase.commit()

def fetch_data( task_id):
      try:
            if task_id == 'a' or task_id == 'A':
                  data = dbase.execute(""" SELECT * FROM task_tables""")
                  results = data.fetchall()
                  return results
            else:
                  data = dbase.execute(""" SELECT * FROM task_tables WHERE id = {} """.format(task_id))
                  results = data.fetchall()
                  return results
      except :
            return None


def add_data(task_name, messag):
      dbase.execute(""" INSERT INTO task_tables(task_name, message) VALUES(?, ?) """, (task_name, messag))
      dbase.commit()
      
def update_data(task_id, task_name):
      dbase.execute(""" UPDATE task_tables SET task_name = {} WHERE id = {} """.format(task_name, task_id))
      dbase.commit()

def delete_data(task_id):
      dbase.execute( """ DELETE FROM  task_tables WHERE id = {} """.format(task_id))# (task_id))
      dbase.commit()

def close_database():
      dbase.close()
      


# x = Database()
# x.add_data("finish ", "must watch all about love nga 10:11")
# x.add_data("start ", "must watch all about love nga 10:11")
# x.add_data("begin ", "must watch all about love nga 10:11")
# x.add_data("run ", "must watch all about love nga 10:11")
# x.add_data("finish ", "must watch all about love nga 10:11")
# x.add_data("kill ", "must watch all about love nga 10:11")
# x.add_data("cross ", "must watch all about love nga 10:11")
# x.add_data("run ", "must watch all about love nga 10:11")
#x.update_data(2, "aftere")
# a = x.fetch_data(50)

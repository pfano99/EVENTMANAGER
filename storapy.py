import sqlite3


dbase = sqlite3.connect("Database.db")
dbase.execute(""" CREATE TABLE IF NOT EXISTS eventTable(
      eventName TEXT NOT NULL,
      eventStatus TEXT NOT NULL,
      dateCreated TEXT NOT NULL,
      finishDate TEXT NOT NULL,
      eventDetails TEXT) """)

def Insert_Data(eventName, eventStatus, dateCreated, finishDate, eventDetails):
      dbase.execute(""" INSERT INTO eventTable(eventName,eventStatus, dateCreated, finishDate, eventDetails) VALUES(?, ?, ?, ?, ?)""",
       (eventName,eventStatus, dateCreated, finishDate, eventDetails)
       
      )
      dbase.commit()
      dbase.close()

def Delete_Data(name):
      dbase.execute(""" DELETE FROM eventTable WHERE eventName=(?,) """, (name))
      dbase.commit()
def Update_Data():
      dbase.close()
      pass

def Veiw_Data():
      data = dbase.execute(""" SELECT * FROM eventTable  """)
      #dbase.close()
      return data
def search_Event(eventName):
      isFound = False
      eveName = dbase.execute(""" SELECT eventName FROM eventTable  """)
      for name in eveName:
            if name == eventName:
                  isFound = True
                  break

      return isFound

def Close_DataBase():
      dbase.close()
#Insert_Data("skill", "Important", "12-15-1999", "02-01-2020","job")

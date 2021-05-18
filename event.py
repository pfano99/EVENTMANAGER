
from tkinter import *
from tkinter import messagebox
import storapy
import sys
import time
import sqlite3

today_date = time.gmtime()
current_time = "{}-{}-{}".format(today_date[2],today_date[1],today_date[0] )
print(current_time)


root = Tk()
root.geometry("800x400")
root.title("Event Manager")
root.configure(bg="#233012")

########################## FUNCTIONS ###############################

def quit_App():
      sys.exit()
      #sys.quit()

def clear_Inputs():
      name_Entry.delete(0, END)
      status_Entry.delete(0, END)
      created_date_Entry.delete(0, END)
      finish_Date_Entry.delete(0, END)
      details_Entry.delete(0, END)

def display_Current_Data():
      info_Box.delete(0, END)
      data = storapy.Veiw_Data()
      for event in data:
            info_Box.insert(END, event)

def get_Search(name):
      isFound = storapy.search_Event(name)
      if isFound == True:
            message = "Event Is Available"
            #messagebox.showerror("Event Not Found", "Event Not Found")
      else:
            #message = "Event Is Not Available"
            messagebox.showerror("Event Not Found", "Event Not Found")
      #return message

      

def add_Menu():
      global name_Entry
      global status_Entry
      global created_date_Entry
      global finish_Date_Entry
      global details_Entry
      #global menu_Frame
      menu_Frame = Toplevel(bg="#233012")
      menu_Frame.title("Add Event")
      menu_Frame.geometry("350x500")

      info_Box = Frame(menu_Frame)
      info_Box.place(
            relwidth=0.9,
            relheight=0.9,
            relx=0.05,
            rely=0.05
      )

      name_Label = Label(info_Box, text="Event Name", font=("bold", 18), anchor=W)
      name_Label.place(
            relwidth = 0.75,
            relheight= 0.05,
            relx = 0.05,
            rely=0.05
      )
      name_Entry = Entry(info_Box, font=("bold", 18))
      name_Entry.place(
            relwidth = 0.9,
            relheight= 0.07,
            relx = 0.05,
            rely=0.12
      )
      status_Label = Label(info_Box, text="Event Status", font=("bold", 18), anchor=W)
      status_Label.place(
            relwidth = 0.75,
            relheight= 0.05,
            relx = 0.05,
            rely=0.21
      )
      status_Entry = Entry(info_Box, font=("bold", 18))
      status_Entry.place(
            relwidth = 0.9,
            relheight= 0.07,
            relx = 0.05,
            rely=0.28
      )

      create_date_Label = Label(info_Box, text="Date Created", font=("bold", 18), anchor=W)
      create_date_Label.place(
            relwidth = 0.75,
            relheight= 0.05,
            relx = 0.05,
            rely=0.37
      )
      created_date_Entry = Entry(info_Box, font=("bold", 18), state = DISABLED)
      created_date_Entry.place(
            relwidth = 0.9,
            relheight= 0.07,
            relx = 0.05,
            rely=0.44
      )

      created_date_Entry.setvar(current_time)

      finish_Date_Label = Label(info_Box, text="Finish By", font=("bold", 18), anchor=W)
      finish_Date_Label.place(
            relwidth = 0.75,
            relheight= 0.05,
            relx = 0.05,
            rely=0.53
      )
      finish_Date_Entry = Entry(info_Box, font=("bold", 18))
      finish_Date_Entry.place(
            relwidth = 0.9,
            relheight= 0.07,
            relx = 0.05,
            rely=0.6
      )

      details_Label = Label(info_Box, text="Event Details", font=("bold", 18), anchor=W)
      details_Label.place(
            relwidth = 0.75,
            relheight= 0.05,
            relx = 0.05,
            rely=0.69
      )
      details_Entry = Entry(info_Box, font=("bold", 18))
      details_Entry.place(
            relwidth = 0.9,
            relheight= 0.07,
            relx = 0.05,
            rely=0.76
      )

      save_Button = Button(info_Box, text="Add",bg="green", font=("bold", 18), command = lambda: storapy.Insert_Data(
          name_Entry.get(), status_Entry.get(), created_date_Entry.get(), finish_Date_Entry.get(), details_Entry.get()  
      ))
      save_Button.place(
            relwidth=0.45,
            relheight=0.1,
            relx=0.05,
            rely=0.85
      )

      clear_Button = Button(info_Box, text="Clear Inputs",bg="red", font=("bold", 18), command=clear_Inputs)
      clear_Button.place(
            relwidth=0.4,
            relheight=0.1,
            relx=0.55,
            rely=0.85
      )
      

def delete_Menu():
      menu_Frame = Toplevel(bg="#233012")
      menu_Frame.title("Delete Event")
      menu_Frame.geometry("450x200")

      info_Box = Frame(menu_Frame)
      info_Box.place(
            relwidth=0.96,
            relheight=0.9,
            relx=0.02,
            rely=0.05
      )

      event_name_Label = Label(menu_Frame, text="Event Name", font=("bold", 15), anchor=W)
      event_name_Label.place(
            relwidth = 0.5,
            relheight =0.15,
            relx = 0.05,
            rely = 0.08
      )

      event_name_Entry = Entry(menu_Frame,font=("bold", 15))
      event_name_Entry.place(
            relwidth = 0.9,
            relheight =0.15,
            relx = 0.05,
            rely = 0.25
      )

      event_Found_Label = Label(menu_Frame, text="Event Not Found", bg="gray", font=("italic", 15))
      event_Found_Label.place(
            relwidth = 0.57,
            relheight =0.15,
            relx = 0.38,
            rely = 0.44
      )

      search_Event_Button = Button(menu_Frame, text="Search Event",bg="green", font=("bold", 15), command=lambda :get_Search(
            event_name_Entry.get())
      )
      search_Event_Button.place(
            relwidth = 0.3,
            relheight =0.15,
            relx = 0.05,
            rely = 0.44
      )
      

      
def update_Menu():
      menu_Frame = Toplevel(bg="#233012")
      menu_Frame.title("Update Event")
      menu_Frame.geometry("450x200")

      info_Box = Frame(menu_Frame)
      info_Box.place(
            relwidth=0.96,
            relheight=0.9,
            relx=0.02,
            rely=0.05
      )

      event_name_Label = Label(menu_Frame, text="Event Name", font=("bold", 15), anchor=W)
      event_name_Label.place(
            relwidth = 0.5,
            relheight =0.15,
            relx = 0.05,
            rely = 0.08
      )

      event_name_Entry = Entry(menu_Frame,font=("bold", 15))
      event_name_Entry.place(
            relwidth = 0.9,
            relheight =0.15,
            relx = 0.05,
            rely = 0.25
      )

      event_Found_Label = Label(menu_Frame, text="Event Not Found", bg="gray", font=("italic", 15))
      event_Found_Label.place(
            relwidth = 0.57,
            relheight =0.15,
            relx = 0.38,
            rely = 0.44
      )

      search_Event_Button = Button(menu_Frame, text="Search Event",bg="green", font=("bold", 15))
      search_Event_Button.place(
            relwidth = 0.3,
            relheight =0.15,
            relx = 0.05,
            rely = 0.44
      )


################# TITLE FRAME ######################

title_Frame = Frame(root, )
title_Frame.place(relwidth=0.35, relheight=0.2, relx=0.01, rely=0.05)
Label(title_Frame, text="LIST TO CHECK",font=("bold", 10)).place(
      relwidth=0.5, relheight=0.5, relx=0.25, rely=0.25
)

################ BUTTON FRAME ###############3

button_Frame = Frame(root, )
button_Frame.place(relwidth=0.35, relheight=0.65, relx=0.01, rely=0.3)

add_Button = Button(button_Frame, text="Add Event", font=("bold", 15), fg="blue", command=add_Menu)
add_Button.place(relwidth=0.5, relheight=0.17, relx=0.25, rely=0.05)

update_Button = Button(button_Frame, text="Update Event", font=("bold", 15), fg="blue", command=update_Menu)
update_Button.place(relwidth=0.5, relheight=0.17, relx=0.25, rely=0.25)

delete_Button = Button(button_Frame, text="Delete Event", font=("bold", 15), fg="blue", command=delete_Menu)
delete_Button.place(relwidth=0.5, relheight=0.17, relx=0.25, rely=0.46)

#veiw_Button = Button(button_Frame, text="Veiw Event", font=("bold", 15))
#veiw_Button.place(relwidth=0.5, relheight=0.17, relx=0.25, rely=0.67)

reFrash_Button = Button(button_Frame, text="Refresh", font=("bold", 15), fg="green", command=display_Current_Data)
reFrash_Button.place(relwidth=0.45, relheight=0.17, relx=0.02, rely=0.8)

exit_Button = Button(button_Frame, text="Exit", font=("bold", 15), bd=3,fg="red", command=quit_App)
exit_Button.place(relwidth=0.45, relheight=0.17, relx=0.52, rely=0.8)

###### LIST_BOX AND SCROLL BAR #############
info_Box = Listbox(root, font = ("italic", 14))
info_Box.place(relwidth=0.58, relheight=0.9, relx=0.4, rely=0.05)
display_Current_Data()

scrowller = Scrollbar(root, bg="blue")
scrowller.place(relwidth=0.02, relheight=0.9, relx=0.38, rely=0.05)

info_Box.configure(yscrollcommand=scrowller.set)
scrowller.configure(command=info_Box.yview)



root.mainloop()
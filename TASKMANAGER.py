from tkinter import *
from tkinter import messagebox
import storage as thedata

colors = ["white", "gray", "#687b87", "#3279a8", "red"]
app = Tk()

class database_communication:
      def adding_to_database(self, task_name, task_message):
            try:
                  if task_name != " " and task_message != " ":
                        thedata.add_data(thedata,task_message)
                  else:
                        print("Make sure all fields are filled")
            except:
                        print("Something went wrong!!!!")
      def updating_a_record(self):
            pass
      def deleting_a_record(self, x):
            
            if str(x).isnumeric():
                  thedata.delete_data(x)

            else:
                  return "Must be an integer"

      
      
local_access = database_communication()
class homePage:
      def __init__(self, root, bg_color):
            self.app = root
            self.app.geometry("800x400") 
            self.app.title("Get Easy")
            self.app.config(bg = bg_color[0])
            self.colors = bg_color

      def header_menu(self, ):
            self.header_frame = Frame(self.app, bg = self.colors[2])
            self.header_frame.place(relwidth =1, relheight = 0.15, rely = 0)
            Label(self.header_frame, text = "Gat Easy", font = ("bold", 20),fg = self.colors[0], bg = self.colors[2]).place(
                  relwidth =0.5, relheight =0.5, relx =0.02, rely =0.25
            )
      def side_menu(self, ):
            self.side_frame = Frame(self.app, bg = self.colors[2])
            self.side_frame.place(relwidth =0.2, relheight = 1, relx = 0)
            ######### 
            ###################
            self.home_Button = Button(self.side_frame, text = "Home", font = ("bold", 15), fg = self.colors[2], anchor = W, command = lambda: self.homeMenu(self.main_section()))
            self.add_event_Button = Button(self.side_frame, text = "Add Task", font = ("bold", 15), fg = self.colors[2], anchor = W, command = lambda: self.add_item_menu(self.main_section()))
            self.update_event_Button = Button(self.side_frame, text = "Update Task", font = ("bold", 15), fg = self.colors[2], anchor = W, command = lambda: self.update_item_menu(self.main_section())) 
            self.delete_event_Button = Button(self.side_frame, text = "Delete Task", font = ("bold", 15), fg = self.colors[2], anchor = W, command = lambda: self.remove_item_menu(self.main_section())) 
            self.close_app_Button = Button(self.side_frame, text = "Exit", font = ("bold", 15), fg = self.colors[2], anchor = W, command = self.close_application)
            
            self.home_Button.place(relwidth =0.98, relheight = 0.1, relx = 0.01, rely = 0.25)
            self.add_event_Button.place(relwidth =0.98, relheight = 0.1, relx = 0.01, rely = 0.37)
            self.update_event_Button.place(relwidth =0.98, relheight = 0.1, relx = 0.01, rely = 0.49)
            self.delete_event_Button.place(relwidth =0.98, relheight = 0.1, relx = 0.01, rely = 0.61)
            self.close_app_Button.place(relwidth =0.98, relheight = 0.1, relx = 0.01, rely = 0.73)

      def main_section(self):
            self.main_box = Frame(self.app, relief = RAISED)
            self.main_box.place(relwidth = 0.79, relheight = 0.825, relx =0.205, rely = 0.16)
            return self.main_box
      
      def homeMenu(self, mainbox):
            Label(mainbox, text = "hello there", font = ("bold", 15)).place(relwidth = 0.5, relheight = 0.25, relx =0.25, rely = 0.25)

      def add_item_menu(self, mainbox):
            add_box = LabelFrame(mainbox, text = "Add Task", font = ("bold", 15))
            add_box.place(relwidth = 0.95, relheight =0.95, relx = 0.02, rely = 0.02)
            
            Label(add_box, text = "Event Name", font = ("bold", 15),anchor = W ).place(
                 relwidth = 0.5, relheight =0.1, relx = 0.02, rely = 0.05
            )
            ##############
            event_name = Entry(add_box, font = ("bold", 15))
            event_name.place(relwidth = 0.65, relheight =0.12, relx = 0.02, rely = 0.18)
            Label(add_box, text = "Message", font = ("bold", 15), anchor = W).place(
                  relwidth = 0.5, relheight =0.1, relx = 0.02, rely = 0.32
            )
            message = Entry(add_box, font = ("bold", 15))
            message.place(relwidth = 0.65, relheight = 0.45, relx = 0.02, rely = 0.42)

            add_btn = Button(add_box, text = "Add", font = ("bold", 15), command = lambda: local_access.adding_to_database(event_name.get(), message.get()))
            add_btn.place(relwidth = 0.2, relheight =0.1, relx = 0.73, rely = 0.77)

      #FUNCTION TO DISPLAY THE SEARCH ENTRY AND SEARCH BUTTON

      def search_menu(self, the_box, btn_text ):
            Label(the_box, text = "Event Number", font = ("bold", 15), anchor = W).place(
                  relwidth = 0.5, relheight =0.1, relx = 0.02, rely = 0.02
            )
            event_no = Entry(the_box, font = ("bold", 15))
            event_no.place(relwidth = 0.65, relheight =0.12, relx = 0.02, rely = 0.18)
            """
                  search button will call function(1st func) to call a function(2nd func) in storage file to check if the event is available or not then 
                  the function(1st func) will call the search result function(3rd) to display the appropriate information based on the results.
            """
            search_btn = Button(the_box, text = "Search", font = ("bold", 15))
            search_btn.place(relwidth = 0.2, relheight =0.12, relx = 0.7, rely = 0.18)

      ## Function to display final output based on the result of the search.
      def search_result(self, the_box, results):
            # Label(the_box, text = "Event Number", font = ("bold", 15), anchor = W).place(
            #       relwidth = 0.5, relheight =0.1, relx = 0.02, rely = 0.02
            # )
            # event_no = Entry(the_box, font = ("bold", 15))
            # event_no.place(relwidth = 0.65, relheight =0.12, relx = 0.02, rely = 0.18)
            # search_btn = Button(the_box, text = "Search", font = ("bold", 15))
            # search_btn.place(relwidth = 0.2, relheight =0.12, relx = 0.7, rely = 0.18)

            # is_found = True
            # if is_found:
            #       event_name = Entry(the_box, font = ("bold", 15))
            #       event_name.place(relwidth = 0.65, relheight =0.12, relx = 0.02, rely = 0.18)
            #       Label(the_box, text = "Message", font = ("bold", 15), anchor = W).place(
            #             relwidth = 0.5, relheight =0.1, relx = 0.02, rely = 0.32
            #       )
            #       message = Entry(the_box, font = ("bold", 15))
            #       message.place(relwidth = 0.65, relheight = 0.45, relx = 0.02, rely = 0.42)
            #       action_btn = Button(the_box, text = btn_text, font = ("bold", 15))
            #       action_btn.place(relwidth = 0.2, relheight =0.12, relx = 0.7, rely = 0.18)
            # else:
            #       Label(the_box, text = "Event Not Found!!", font = ("bold", 15)).place(
            #             relwidth = 0.5, relheight =0.45, relx = 0.25, rely = 0.42
            #       )
            pass

      def remove_item_menu(self, main_box):
            remove_box = LabelFrame(main_box, text = "Remove Task", font = ("bold", 15))
            remove_box.place(relwidth = 0.95, relheight =0.95, relx = 0.02, rely = 0.02)
            #self.search_result(remove_box, "Remove")

      def update_item_menu(self, main_box):
            update_box = LabelFrame(main_box, text = "Update Task", font = ("bold", 15))
            update_box.place(relwidth = 0.95, relheight =0.95, relx = 0.02, rely = 0.02)
            #self.search_result(update_box, "Update")


      def close_application(self):
            response = messagebox.askokcancel("Close Application", "Do you want to exit!")
            if response == True:
                  self.app.quit()

x = homePage(app, colors)
x.header_menu()
x.side_menu()
x.main_section()

app.mainloop()

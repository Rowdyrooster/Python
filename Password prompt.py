import tkinter
from tkinter import *

class Application(Frame):
    ### AGUI Application with 3 buttons

        def __init__(self, master):
            ### initializes Frame
            Frame.__init__(self,master)
            self.grid()
            self.create_widgets()

        def create_widgets(self):
            ## Create button, text, and entry widgets
            self.instruction = Label(self, text = "Enter the password:")
            self.instruction.grid(row = 0, columnspan = 2, sticky = W)
            self.password = Entry(self)
            self.password.grid(row = 1 , sticky = W)

            self.submit_button = Button(self, text = "Submit", command = self.reveal)
            self.submit_button.grid(row = 6, column = 0, sticky = W)

            self.text = Text(self, width = 35, height = 5, wrap = WORD)
            self.text.grid( row = 3, column = 0, columnspan = 2, sticky = W)

            self.cancel_button = Button(self, text = "cancel", command = self.reveal)
            self.cancel_button.grid(row = 7, column = 0, sticky = W)

            self.forgot_button = Button(self, text = "Forgot Password", command = self.reveal)
            self.forgot_button.grid(row = 8, column = 0, sticky = W)

        def reveal(self):
            content = self.password.get()
            if content == "Pass":
                message = "Verifying.......Access Granted"
                self.text.delete(0.0, END)
                self.text.insert(0.0, message)
                
            else:
                message = "Access Denied"
                self.text.delete(0.0, END)
                self.text.insert(0.0, message)


root = Tk()
root.title("Authentication")
root.geometry("350x250")
app = Application(root)

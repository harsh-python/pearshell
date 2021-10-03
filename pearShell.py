import os
import time
import pyttsx3 
import json
from getpass import getpass
from tkinter import messagebox
from tkinter import *


class Pearshell:
    def __init__(self):
        self.about = """@CopyRight
Version: 1.0
By: Harhbir Singh
"""
        # run var
        self.run = True
        #speech
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voices', self.voices[0].id)
        # reading the json file for password and username
        self.file = open("set.json", 'r')
        self.data = self.file.read()
        self.file.close()
        self.file_data = json.loads(self.data)
        self.name = self.file_data["username"]
        self.passd = self.file_data["password"]
##        print(self.name)
##        print(self.passd)

    def speak(self,audio):
        self.engine.say(audio)
        print(audio)
        self.engine.runAndWait()

    # setup
    ##############################################################
    def setup(self,e):
        self.root.destroy()
        os.system('attrib -s -h -r set.json')
        self.speak("Welcome To Pear Shell Setup")
        self.username = input("Enter Your Username For Pear Shell: ")
        self.password = getpass("Enter Your User Account Password: ")
        self.file3 = open("set.json",'r')
        self.data3 = self.file3.read()
        self.file3.close()

        self.file_data3 = json.loads(self.data3)
        self.name = self.file_data3["username"]
        self.passd = self.file_data3["password"]
        self.v2 = {
            "username":self.username,
            "password":self.password
        }
        self.file_data3 = json.dumps(self.v2)
        self.file4 = open("set.json",'w')
        self.data4 =self.file4.write(self.file_data3)
        self.file4.close()
        time.sleep(2)
        self.speak("Your Account Is Setup!")
        self.speak("You Can Now Use Pear Shell")
        os.startfile('pearShell.py')
        os.system('attrib +s +h +r set.json')
        exit() 
    ##############################################################
    # main terminal
    ##############################################################
    def terminal(self,e):
        self.root.destroy() # destroy root
        self.speak("Welcome To Pear Shell..")
        self.speak('Enter your username and password!')
        for i in range(4):
            self.usern = input("USERNAME: ")
            self.passn = getpass("PASSWORD: ")
            if self.usern == self.name and self.passn == self.passd:
                self.speak("Login Successful!!!!!")
                break
            else:
                self.speak("Username and Password not found!")
        time.sleep(1)
        self.speak('Now You Can Use The Pear Shell, Happy Coding!')
        while self.run:
            self.x = input('>>> ')
            if self.x == 'exit':
                self.speak("Wrong")
                self.speak("Type 'exit()' TO Exit")
            elif self.x == "exit()":
                self.speak("Thanks For Using Pear Shell")
            elif self.x == "help":
                self.speak("To Exit Type: exit()")
                self.speak("For About: about_ter")
                self.speak("To open Setup: set_ter")
                # speak("To Uninstall The Python Shell: uninstall_ter")
            elif self.x == 'about_ter':
                messagebox.showinfo("About", self.about)
            elif self.x == 'set_ter':
                os.system('attrib -s -h -r set.json')
                self.speak("Welcome To Pear Shell Setup")
                self.username = input("Enter Your Username For Pear Shell: ")
                self.password = getpass("Enter Your User Account Password: ")
                self.file3 = open("set.json",'r')
                self.data3 = self.file3.read()
                self.file3.close()

                self.file_data3 = json.loads(self.data3)
                self.name = self.file_data3["username"]
                self.passd = self.file_data3["password"]
                self.v2 = {
                    "username":self.username,
                    "password":self.password
                }
                self.file_data3 = json.dumps(self.v2)
                self.file4 = open("set.json",'w')
                self.data4 =self.file4.write(self.file_data3)
                self.file4.close()
                time.sleep(2)
                self.speak("Your Account Is Setup!")
                self.speak("You Can Now Use Pear Shell")
                os.startfile('pearShell.py')
                os.system('attrib +s +h +r set.json')
                exit()
            # elif x == "uninstall_ter":
            #     os.remove('python_shell.py')
            #     exit()

            try:
                self.y = eval(self.x)
                if self.y: print(self.x)
            except:
                try:
                    exec(self.x)
                except Exception as e:
                    if self.x == 'exit' or self.x == 'help' or self.x == 'about_ter' or self.x == "uninstall_ter":
                        pass
                    else:
                        print(f"error: {e}")
    ##############################################################
    # load
    ##############################################################
    def load(self):
        # Create object
        global root
        self.root = Tk()

        # Adjust size
        self.w = 500
        self.h = 300

        self.ws = self.root.winfo_screenwidth()
        self.hs = self.root.winfo_screenheight()
        self.x = (self.ws/2) - (self.w/2)
        self.y = (self.hs/2) - (self.h/2)
        self.root.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
        self.root.overrideredirect(True)

        # Add image file
        self.bg = PhotoImage(file = "logo.png")

        # Create Canvas
        canvas1 = Canvas( self.root, width = 400,
                                        height = 400)

        canvas1.pack(fill = "both", expand = True)

        # Display image
        canvas1.create_image( 0, 0, image = self.bg,
                                        anchor = "nw")

        # Add Text
        canvas1.create_text( 250, 250, text = "TO LOAD PRESS [CTRL+L] OR FOR SETUP PRESS [CTRL+S] ",font=("bold",10))

        # binding keys to functions
        self.root.bind('<Control-Key-l>', self.terminal)
        self.root.bind('<Control-Key-s>', self.setup)

        # Execute tkinter
        self.root.mainloop()

if __name__ == "__main__":
    os.system('attrib +s +h +r set.json')
    var = Pearshell()
    var.load()
          

# importing modules
import os
import time
import pyttsx3 
import json
from getpass import getpass
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser


class Pearshell: # main class
    def __init__(self):     # init function
        # 'about' var
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
    def setup(self,e): # stup function
        self.root.destroy() # destroing the load window
        os.system('attrib -s -h -r set.json')
        # welcome
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
                self.speak("To open the python editor: editin")
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
            elif self.x == 'editin':
                self.editor()
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
        
    #######################################################
    # gui editor
    #######################################################
    def editor(self)       :
        self.root2 = Tk()
        self.root2.title("PearShell~Editor")
        self.root2.geometry("1000x498")

        
        global open_status_name
        self.open_status_name = False

        global selected
        self.selected = False

        def new_file():
            self.my_text.delete("1.0", END)
            self.root2.title("PearShell~Editor//New file")
            self.status_bar.config(text="New file           ")

            global open_status_name
            self.open_status_name = False

        def open_file():
            self.my_text.delete("1.0",END)

            self.text_file = filedialog.askopenfilename(title="Open file", filetypes=(("Python files", "*.py"), ("All files", "*.*"), ("Text files", "*.txt")))
            if self.text_file:
                global open_status_name
                self.open_status_name = self.text_file
            self.name = self.text_file           
            self.status_bar.config(text="File Opened           ")
            self.root2.title(f"PearShell~Editor//{self.name}")

            self.text_file = open(self.text_file, 'r')
            self.stuff = self.text_file.read()
            self.my_text.insert(END, self.stuff)
            self.text_file.close()
        
        def save_as_file():
            text_file = filedialog.asksaveasfilename(defaultextension=".*", title="Save as", filetypes=(("Python files", "*.py"), ("All files", "*.*"), ("Text files", "*.txt")))
            if text_file:
                name = text_file
                self.status_bar.config(text="File saved!          ")
                self.root2.title(f"PearShell~Editor//{name}")

                text_file = open(text_file, 'w')
                text_file.write(self.my_text.get(1.0, END))
                text_file.close()
        
        def save_file():
            global open_status_name
            if self.open_status_name:
                text_file = open(self.open_status_name, 'w')
                text_file.write(self.my_text.get(1.0, END))
                text_file.close()

                self.status_bar.config(text="File saved!          ")
            else:
                save_as_file()

        def cut_text(e):
            global selected
            if e:
                selected = self.root2.clipboard_get()
            else:    
                if self.my_text.selection_get():
                    selected = self.my_text.selection_get()
                    self.my_text.delete("sel.first", "sel.last")
                    self.root2.clipboard_clear()
                    self.root2.clipboard_append(selected)
        
        def copy_text(e):
            global selected
            if e:
                selected = self.root2.clipboard_get()
                
            if self.my_text.selection_get():
                selected = self.my_text.selection_get()
                self.root2.clipboard_clear()
                self.root2.clipboard_append(selected)
        
        def paste_text(e):
            global selected
            if e:
                selected = self.root2.clipboard_get()
            else:    
                if selected:
                    position = self.my_text.index(INSERT)
                    self.my_text.insert(position, selected)

        def bold_it():
            bold_font = font.Font(self.my_text, self.my_text.cget("font"))
            bold_font.configure(weight="bold")

            self.my_text.tag_configure("bold", font=bold_font)

            current_tags = self.my_text.tag_names("sel.first")
            
            if "bold" in current_tags:
                self.my_text.tag_remove("bold", "sel.first", "sel.last")
            else:
                self.my_text.tag_add("bold", "sel.first", "sel.last")
        
        def it_it():
            it_font = font.Font(self.my_text, self.my_text.cget("font"))
            it_font.configure(slant="italic")

            self.my_text.tag_configure("it", font=it_font)

            current_tags = self.my_text.tag_names("sel.first")
            
            if "it" in current_tags:
                self.my_text.tag_remove("it", "sel.first", "sel.last")
            else:
                self.my_text.tag_add("it", "sel.first", "sel.last")
        
        def text_color():
            my_color = colorchooser.askcolor()[1]
            if my_color:
                co1_font = font.Font(self.my_text, self.my_text.cget("font"))
                

                self.my_text.tag_configure("co", font=co1_font, foreground=my_color)

                curret_tags = self.my_text.tag_names("sel.first")
                
                if "co" in curret_tags:
                    self.my_text.tag_remove("co", "sel.first", "sel.last")
                else:
                    self.my_text.tag_add("co", "sel.first", "sel.last")
        
        def bg_color():
            my_color = colorchooser.askcolor()[1]
            if my_color:
                self.my_text.config(bg=my_color)
        def all_color():
            my_color = colorchooser.askcolor()[1]
            if my_color:
                self.my_text.config(fg=my_color)

        def select_text(e):
            if e:
                self.my_text.tag_add('sel', '1.0', 'end')
            else:
                self.my_text.tag_add('sel', '1.0', 'end')
        
        def clear_text(e):
            if e:
                self.my_text.delete(1.0, END)
            else:
                self.my_text.delete(1.0, END)
        
        def night_mode():
            self.main_color = "#000000"
            self.second_color = "#303030"
            self.text_color = "#1aff00"

            self.root2.config(bg=self.main_color)
            self.my_text.config(bg=self.second_color, fg=self.text_color)
            self.status_bar.config(bg=self.main_color, fg=self.text_color)
            self.toolbar_frame.config(bg=self.main_color)
            self.it_button.config(bg=self.main_color, fg=self.text_color)
            self.bold_button.config(bg=self.main_color, fg=self.text_color)
            self.file_menu.config(bg=self.main_color, fg=self.text_color)
            self.edit_menu.config(bg=self.main_color, fg=self.text_color)
            self.color_menu.config(bg=self.main_color, fg=self.text_color)
            self.mode_menu.config(bg=self.main_color, fg=self.text_color)
        
        def light_mode():
            self.main_color = "SystemButtonFace"
            self.second_color = "SystemButtonFace"
            self.text_color = "black"

            self.root2.config(bg=self.main_color)
            self.my_text.config(bg=self.second_color, fg=self.text_color)
            self.status_bar.config(bg=self.main_color, fg=self.text_color)
            self.toolbar_frame.config(bg=self.main_color)
            self.it_button.config(bg=self.main_color, fg=self.text_color)
            self.bold_button.config(bg=self.main_color, fg=self.text_color)
            self.file_menu.config(bg=self.main_color, fg=self.text_color)
            self.edit_menu.config(bg=self.main_color, fg=self.text_color)
            self.color_menu.config(bg=self.main_color, fg=self.text_color)
            self.mode_menu.config(bg=self.main_color, fg=self.text_color)

        # tootlbar
        self.toolbar_frame = Frame(self.root2)
        self.toolbar_frame.pack(fill=X)

        # Create Main Frame
        self.my_frame = Frame(self.root2)
        self.my_frame.pack(pady=5)

        # create scrollbar for text box
        self.text_scroll = Scrollbar(self.my_frame)
        self.text_scroll.pack(side=RIGHT, fill=Y)

        self.text_scroll2 = Scrollbar(self.my_frame, orient='horizontal')
        self.text_scroll2.pack(side=BOTTOM, fill=X)

        # create text box
        self.my_text = Text(self.my_frame, width=122, height=29, font=("Courier New", 14,"bold"), foreground="black", selectbackground="gray", selectforeground="blue", undo=True, yscrollcommand=self.text_scroll.set, xscrollcommand=self.text_scroll2.set, wrap="none")
        self.my_text.pack()

        # Configuring scrollbar
        self.text_scroll.config(command=self.my_text.yview)

        self.text_scroll2.config(command=self.my_text.xview)
        # Creating menu
        self.my_menu = Menu(self.root2)
        self.root2.config(menu=self.my_menu)

        # file menu
        self.file_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=new_file, accelerator="  ")
        self.file_menu.add_command(label="Open", command=open_file, accelerator="  ")
        self.file_menu.add_command(label="Save", command=save_file, accelerator="  ")
        self.file_menu.add_command(label="Save as", command=save_as_file, accelerator="  ")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root2.quit, accelerator="  ")

        # edit menuself.
        self.edit_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut", command=lambda: cut_text(False), accelerator="(Ctrl+X)")
        self.edit_menu.add_command(label="Copy", command=lambda: copy_text(False), accelerator="(Ctrl+C)")
        self.edit_menu.add_command(label="Paste       ", command=lambda: paste_text(False), accelerator="(Ctrl+V)")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Undo", command=self.my_text.edit_undo, accelerator="(Ctrl+Z)")
        self.edit_menu.add_command(label="Redo", command=self.my_text.edit_redo, accelerator="(Ctrl+Y)")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Select All", command=lambda: select_text(False), accelerator="(Ctrl+A)")
        self.edit_menu.add_command(label="Clear", command=lambda: clear_text(False), accelerator="(Ctrl+D)")

        
        # color menu
        self.color_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="Color", menu=self.color_menu)
        self.color_menu.add_command(label="Background", command=bg_color, accelerator=" ")
        self.color_menu.add_command(label="Text", command=text_color, accelerator=" ")
        self.color_menu.add_command(label="All Text", command=all_color, accelerator=" ")

        # mode menu
        self.mode_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="Modes", menu=self.mode_menu)
        self.mode_menu.add_command(label="Night Mode", command=night_mode, accelerator=" ")
        self.mode_menu.add_command(label="Light Mode", command=light_mode, accelerator=" ")

        # adding a status bar
        self.status_bar = Label(self.root2, text='Ready           ', anchor=E)
        self.status_bar.pack(fill=X, side=BOTTOM, ipady=5)

        # edit bindings
        self.root2.bind('<Control-Key-x>', cut_text)
        self.root2.bind('<Control-Key-c>', copy_text)
        self.root2.bind('<Control-Key-v>', paste_text)
        self.root2.bind('<Control-Key-a>', select_text)
        self.root2.bind('<Control-Key-d>', clear_text)

        # toolbar button
        self.bold_button = Button(self.toolbar_frame, text="Bold", command=bold_it)
        self.bold_button.grid(row=0, column=0, sticky=W, padx=5)

        self.it_button = Button(self.toolbar_frame, text="Italic", command=it_it)
        self.it_button.grid(row=0, column=1, padx=5)

        # mainloop
        self.root2.mainloop()

            
if __name__ == "__main__":
    os.system('attrib +s +h +r set.json')
    var = Pearshell()
    var.load()
          

          

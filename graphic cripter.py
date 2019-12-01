import tkinter as tk
import os
import encript as e
#starting variables
green = '#D4FF5F'
blue = '#66A1FF'
red = '#FF4848'
font = ('Calibri', 16)
homeb_font = ('Helvetica', 14)
big_font = ('Calibri', 18)
passwords_list = []
#functions for updating the widget_list and passwords_list
def passwords_list_update():
    global passwords_list
    passwords_list = []
    for root, dirs, files in os.walk('encrypted passwords'):
        for x in files:
            passwords_list.append(x.replace('.txt', ''))
passwords_list_update()

def widget_list_update():
    widget_list.delete(first=0, last=widget_list.size())
    for x in passwords_list:
        widget_list.insert(tk.END, x)
#classes for creating all the ...
def create():
    frame = Create()
class Create():
    def __init__(self):
        button_c.config(state='disabled')
        button_r.config(state='disabled')
        button_d.config(state='disabled')
        #frame which contains all the create stuff
        self.create_window = tk.Frame(bg=green)
        self.create_window.place(relx=0.06, rely=0.1, relwidt=0.88, relheight=0.8)
        #all thinghs to get all the data (password ecc...)
        name_label = tk.Label(self.create_window, text='Inserisci il nome della password:',
            font=font, anchor='nw', bg=green)
        name_label.place(relx=0, rely=0, relwidt=0.9, relheight=0.1)
        self.name_entry = tk.Entry(self.create_window, font=font, bd=0)
        self.name_entry.place(relx=0.05, rely=0.1, relwidt=0.9, relheight=0.1)

        key_label = tk.Label(self.create_window, text='Inserisci la chiave per criptare la password:',
             font=font, anchor='nw', bg=green)
        key_label.place(relx=0, rely=0.2, relwidt=1, relheight=0.1)
        self.key_entry = tk.Entry(self.create_window, font=font, bd=0)
        self.key_entry.place(relx=0.05, rely=0.3, relwidt=0.9, relheight=0.1)
        self.privacy_button = tk.Button(self.create_window, text='•', font=font, bg='white',
            relief='flat', command=lambda: self.privacy_buttons_f(self.key_entry))
        self.privacy_button.place(relx=0.85, rely=0.3, relwidt=0.1, relheight=0.1)

        password_label = tk.Label(self.create_window,text='Inserisci la password:', font=font,
            anchor='nw', bg=green)
        password_label.place(relx=0, rely=0.4, relwidt=1, relheight=0.1)
        self.password_entry = tk.Entry(self.create_window, font=font, bd=0)
        self.password_entry.place(relx=0.05, rely=0.5, relwidt=0.9, relheight=0.1)
        self.privacy_button2 = tk.Button(self.create_window, text='•', font=font, bg='white',
            relief='flat', command=lambda: self.privacy_buttons_f(self.password_entry))
        self.privacy_button2.place(relx=0.85, rely=0.5, relwidt=0.1, relheight=0.1)
        #button that starts the mainprocess
        self.mainprocess_button = tk.Button(self.create_window, text='Cripta', font=font, bg=green,
            activebackground=green, command=self.mainprocess_button_f)
        self.mainprocess_button.place(relx = 0.25, rely=0.7, relwidt=0.5, relheight=0.2)
        #home button
        self.home_button = tk.Button(self.create_window, text='X', font=homeb_font, bg=green, fg='red',
            bd=0, activebackground=green, command=self.home_button_f)
        self.home_button.place(relx=0.9, rely=0, relwidt=0.1, relheight=0.1)

    def mainprocess_button_f(self):
        name_password = self.name_entry.get()
        key_password = self.key_entry.get()
        password = self.password_entry.get()
        passwords_list_update()
        #this will be used to avoid the user enter nothing or things he cant
        controll_name_password = (name_password != '')
        controll_name_password2 = (name_password not in passwords_list)
        controll_key_password = (key_password != '')
        un_k = [x for x in key_password if(x not in e.a)]#unsupported charachters in the key
        controll_key_password2 = (len(un_k)==0)
        controll_password = (password != '')
        un_p = [x for x in password if(x not in e.a)]#unsupported charachters in the password
        controll_password2 = (len(un_p)==0)
        ok = (controll_name_password and controll_name_password2 and controll_key_password and controll_key_password2 and controll_password and controll_password2)

        if ok:#main process
            x = open(file=('encrypted passwords\\' + name_password + '.txt'), mode='w')
            x.write(e.cripter(password, key_password, 1))#1 means: cript!
            x.close()
            passwords_list_update()
            widget_list_update()
            button_c.config(state='normal')
            button_r.config(state='normal')
            button_d.config(state='normal')
            self.create_window.destroy()
        else:
            if (not controll_name_password):
                warning_lab = tk.Label(self.create_window, font=font, anchor='nw', fg='red', bg=green,
                    text='Inserisci il nome della password che vuoi salvare!')
                warning_lab.place(relx=0, rely=0, relwidt=0.9, relheight=0.1)
            if (not controll_name_password2):
                warning_lab = tk.Label(self.create_window, font=font, anchor='nw', fg='red', bg=green,
                    text="Attenzione, c'è già una password chiamata così, cambia nome!")
                warning_lab.place(relx=0, rely=0, relwidt=0.9, relheight=0.1)
            if (not controll_key_password):
                warning_lab = tk.Label(self.create_window, font=font, anchor='nw', fg='red', bg=green,
                    text='Inserisci il la chiave della password che vuoi salvare!')
                warning_lab.place(relx=0, rely=0.2, relwidt=1, relheight=0.1)
            if (not controll_key_password2):
                warning_lab = tk.Label(self.create_window, font=font, anchor='nw', fg='red', bg=green,
                    text=f'Sono spiacente, non riesco a criptare il carattere {un_k[0]}')
                warning_lab.place(relx=0, rely=0.2, relwidt=1, relheight=0.1)
            if (not controll_password):
                warning_lab = tk.Label(self.create_window, font=font, anchor='nw', fg='red', bg=green,
                    text='Inserisci il la password che vuoi salvare!')
                warning_lab.place(relx=0, rely=0.4, relwidt=1, relheight=0.1)
            if (not controll_password2):
                warning_lab = tk.Label(self.create_window, font=font, anchor='nw', fg='red', bg=green,
                    text=f'Sono spiacente, non riesco a criptare il carattere {un_p[0]}')
                warning_lab.place(relx=0, rely=0.4, relwidt=1, relheight=0.1)

    def home_button_f(self):
        self.create_window.destroy()
        button_c.config(state='normal')
        button_r.config(state='normal')
        button_d.config(state='normal')
        passwords_list_update()
        widget_list_update()

    def privacy_buttons_f(self, entry):
        if entry.cget('show') == '':
            entry.config(show='•')
        else:
            entry.config(show='')


def read():
    frame = Read()
class Read():
    def __init__(self):
        button_c.config(state='disabled')
        button_r.config(state='disabled')
        button_d.config(state='disabled')
        #first step of the read option:
        self.read_label = tk.Label(buttons_place,text='Seleziona la password\n che vuoi decriptare',
             font=big_font, bg=blue)
        self.read_label.place(relx=0, rely=0, relwidt=(2/3), relheight=1)
        #button that starts the second step
        self.read_button = tk.Button(buttons_place, text='Decripta', font=big_font, activeforeground='white',
            bg=blue, relief='groove', activebackground=blue, command=self.read_button_f)
        self.read_button.place(relx=(2/3), rely=0, relwidt=(1/3), relheight=1)
        #home button
        self.home_button = tk.Button(buttons_place, text='X', font=homeb_font, foreground='red', bg=blue,
            relief='flat', activebackground=blue, command=self.home_button_f)
        self.home_button.place(x=405, y=0, widt=60, height=50)

    def read_button_f(self):
        try:#this try block is used to the eventuality of pressing the decript_button selecting nothing in the widget_list(listbox), see the first line
            def decript_button_f():#button of the second step that starts the main process
                #ok button of the end of the second step to close evrything
                def password_label_ok_f():
                    self.read_label.destroy()
                    self.read_button.destroy()
                    self.read_window.destroy()
                    self.home_button.destroy()
                    button_c.config(state='normal')
                    button_r.config(state='normal')
                    button_d.config(state='normal')
                    widget_list.config(state='normal')

                key = key_entry.get()

                if key != '':
                    name_password = widget_list.get(first=widget_list.curselection())#
                    password = open(file=('encrypted passwords\\' + name_password + '.txt'), mode='r').read()#
                    decripted_password = e.cripter(password, key, -1)#-1 means: decript
                    #data output
                    first_step_button.destroy()
                    self.key_label.destroy()
                    key_entry.destroy()
                    decript_button.destroy()
                    #data output
                    password_label = tk.Label(self.read_window)
                    password_label.place(relx=0, rely=0, relwidt=1, relheight=1)
                    password_label.config(text=('La tua password è\n' + decripted_password),bg=blue,
                                          font=font, anchor='n', pady='70')

                    password_label_ok = tk.Button(self.read_window)
                    password_label_ok.place(relx=0.4, rely=0.7, relheight=0.2, relwidt=0.2)
                    password_label_ok.config(text='Ok', font=font, bg=blue, activebackground=blue,
                                             command=password_label_ok_f)
                else:
                    self.key_label.config(fg='red', text='Inserisci la chiave per decriptare la password!')
            #function to show dots instead of letters
            def privacy_buttons_f(entry):
                if entry.cget('show') == '':
                    entry.config(show='•')
                else:
                    entry.config(show='')
            #'home' button that goes to the first step function
            def first_step_button_f():
                self.read_window.destroy()
                self.read_button.config(state='normal')
                self.home_button.config(state='normal')
                widget_list.config(state='normal')
            #if the user selected no line in the listbox the line under gives an error and python goes to the exception code line
            widget_list.get(first=widget_list.curselection())
            self.read_button.config(state='disabled')
            self.home_button.config(state='disabled')
            widget_list.config(state='disabled')
            #frame which contains all the read second step's stuff
            self.read_window = tk.Frame(bg=blue)
            self.read_window.place(relx=0.15, rely=0.2, relwidt=0.7, relheight=0.6)
            #all thinghs to get the key
            self.key_label = tk.Label(self.read_window, text='Inserisci la chiave per decriptare la password',
                font=font, anchor='w', bg=blue)
            self.key_label.place(relx=0, rely=0, relwidt=0.9, relheight=0.15)
            key_entry = tk.Entry(self.read_window, font=font)
            key_entry.place(relx=0.05, rely=0.15, relwidt=0.9, relheight=0.15)
            privacy_button = tk.Button(self.read_window, text='•', font=font, bg='white', relief='flat',
                command=lambda: privacy_buttons_f(key_entry))
            privacy_button.place(relx=0.8, rely=0.16, relwidt=0.15, relheight=0.14)
            #button that starts the mainprocess
            decript_button = tk.Button(self.read_window, text='Decripta', font=font, bg=blue,
                activebackground=blue, command=decript_button_f)
            decript_button.place(relx= 0.25, rely=0.5, relwidt=0.5, relheight=0.3)
            #home button that returns to the first step
            first_step_button = tk.Button(self.read_window, text='X', font=homeb_font, bg=blue, bd=0,
                fg='red', activebackground=blue, activeforeground='red', command=first_step_button_f)
            first_step_button.place(relx=0.9, rely=0, relwidt=0.1, relheight=0.1)

            self.read_label.config(text='Seleziona la password\n che vuoi decriptare', fg='black')
        except tk.TclError:
            self.read_label.config(text='Seleziona la password\n che vuoi decriptare!', fg='red')

    def home_button_f(self):
        self.read_label.destroy()
        self.read_button.destroy()
        self.home_button.destroy()
        button_c.config(state='normal')
        button_r.config(state='normal')
        button_d.config(state='normal')


def delete():
    frame = Delete()
class Delete():
    def __init__(self):
        button_c.config(state='disabled')
        button_r.config(state='disabled')
        button_d.config(state='disabled')
        widget_list.config(selectmode='multiple')
        #first step of the delete option
        self.delete_label = tk.Label(buttons_place, text='Seleziona la password\n che vuoi eliminare', font=big_font, bg=red)
        self.delete_label.place(relx=0, rely=0, relwidt=(2/3), relheight=1)
        #button that start the second step
        self.delete_button = tk.Button(buttons_place, text='Elimina', font=big_font, activeforeground='white',
            bg=red, relief='groove', activebackground=red, command=self.delete_button_f)
        self.delete_button.place(relx=(2/3), rely=0, relwidt=(1/3), relheight=1)
        #home button
        self.home_button = tk.Button(text='X', font=homeb_font, foreground='white', bg=red,
            relief='flat', activebackground=red, command=self.home_button_f)
        self.home_button.place(x=405, y=0, widt=60, height=50)

    def delete_button_f(self):
        #second step
        if widget_list.curselection() != ():#this will used if the user select no line of the widget_list(listbox)
            #to disable the first step's widget
            self.home_button.config(state='disabled')
            self.delete_button.config(state='disabled')
            #button's function that start the mainprocess
            def mainprocess_button_f():
                curselection = widget_list.curselection()
                for x in curselection:
                    os.unlink(f'encrypted passwords\\{passwords_list[x]}.txt')
                passwords_list_update()#update passwords_list because it must be reused
                widget_list_update()#update widget_list because it must be reused
                #returns to home
                button_c.config(state='normal')
                button_r.config(state='normal')
                button_d.config(state='normal')
                widget_list.config(selectmode='single')
                delete_window.destroy()
                self.delete_label.destroy()
                self.delete_button.destroy()
                self.home_button.destroy()

            def first_step_button_f():
                delete_window.destroy()
                self.delete_button.config(state='normal')
                self.home_button.config(state='normal')
            #second step widgets
            delete_window = tk.Frame(bg=red)
            delete_window.place(relx=0.15, rely=0.2, relwidt=0.7, relheight=0.6)

            delete_label_sure = tk.Label(text='Sei sicuro di voler\neliminare questi elementi?',
                bg=red, font=big_font, fg='black', anchor='n', pady=70, master=delete_window)
            delete_label_sure.place(relx=0, rely=0, relheight=1, relwidt=1)
            #button that starts the main process
            mainprocess_button = tk.Button(delete_window, text='Ok', font=font, bg=red,
                activebackground=red, command=mainprocess_button_f)
            mainprocess_button.place(relx= 0.25, rely=0.5, relwidt=0.5, relheight=0.3)
            #button that returns to the first step
            first_step_button = tk.Button(delete_window, text='X', font=homeb_font, bg=red,
                bd=0, fg='white', activebackground=red, activeforeground='white', command=first_step_button_f)
            first_step_button.place(relx=0.9, rely=0, relwidt=0.1, relheight=0.1)

            self.delete_label.config(text='Seleziona gli elementi\n che vuoi eliminare', fg='black')
        else:
            self.delete_label.config(text='Seleziona gli elementi\n che vuoi eliminare!', fg='white')


    def home_button_f(self):
        self.delete_label.destroy()
        self.delete_button.destroy()
        self.home_button.destroy()
        widget_list.config(selectmode='single')
        button_c.config(state='normal')
        button_r.config(state='normal')
        button_d.config(state='normal')


w = tk.Tk()
w.geometry('700x500')
w.title('Cripter')
w.resizable(False, False)
#designing the home:
buttons_place = tk.Frame(w)
buttons_place.place(relx=0, rely=0, relwidt=1, relheight=0.25)

button_c = tk.Button(buttons_place)
button_c.pack(side='left', fill='both', expand=True)
button_c.config(text='Aggiungi\nuna password', font=big_font, activeforeground='white',
                bg=green, activebackground=green, relief='groove', command=create)

button_r = tk.Button(buttons_place)
button_r.pack(side='left', fill='both', expand=True)
button_r.config(text='Recupera\nuna password', font=big_font, activeforeground='white',
                bg=blue, relief='groove', activebackground=blue, command=read)

button_d = tk.Button(buttons_place)
button_d.pack(side='left', fill='both', expand=True)
button_d.config(text='Elimina\nuna password', font=big_font, activeforeground='white',
                bg=red, relief='groove', activebackground=red, command=delete)
#the list and scrollbar frame
list_palce = tk.Frame()
list_palce.place(relx=0, rely=0.25, relwidt=1, relheight=0.75)

scrollbar = tk.Scrollbar(list_palce)
scrollbar.pack(side='right', fill='y')

widget_list = tk.Listbox(list_palce)
widget_list.pack(side='left', fill='both', expand=True)
widget_list.config(font=big_font, yscrollcommand=scrollbar.set, selectmode='single',
                   bd=0, selectbackground=blue)
scrollbar.config(command=widget_list.yview)

widget_list_update()

w.mainloop()

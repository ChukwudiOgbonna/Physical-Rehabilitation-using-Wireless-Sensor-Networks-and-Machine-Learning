import sqlite3
from tkinter import *
from tkinter import messagebox as ms

# make database and users (if not exists already) table at programme start up
import bluetooth

with sqlite3.connect('User_Data.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL PRIMARY KEY,password TEXT NOT NULL);')
c.execute(
    'CREATE TABLE IF NOT EXISTS lefthandvalues(id INTEGER NOT NULL PRIMARY KEY,force REAL NOT NULL,flex REAL NOT NULL,acceleration REAL NOT NULL);')
c.execute(
    'CREATE TABLE IF NOT EXISTS righthandvalues(id INTEGER NOT NULL PRIMARY KEY,force REAL NOT NULL,flex REAL NOT NULL,acceleration REAL NOT NULL);')
c.execute(
    'CREATE TABLE IF NOT EXISTS leftlegvalues(id INTEGER NOT NULL PRIMARY KEY,force REAL NOT NULL,flex REAL NOT NULL,acceleration REAL NOT NULL);')
c.execute(
    'CREATE TABLE IF NOT EXISTS rightlegvalues(id INTEGER NOT NULL PRIMARY KEY,force REAL NOT NULL,flex REAL NOT NULL,acceleration REAL NOT NULL);')
db.commit()
db.close()


# main Class
class main:
    def __init__(self, master):
        # Window
        self.master = master
        # Stores values from calibration
        self.lefthandvalues = []
        self.righthandvalues = []
        self.leftlegvalues = []
        self.rightlegvalues = []

        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        # Create Widgets
        self.widgets()

    def popup(self, message):
        root = Tk()
        root.title('Popup window')
        w = 400  # popup window width
        h = 200  # popup window height
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))

        w = Label(root, text=message, width=120, height=10)
        w.pack()

        mainloop()

    # Login Function
    def login(self):
        # Establish Connection
        with sqlite3.connect('User_Data.db') as db:
            c = db.cursor()

        # Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user, [(self.username.get()), (self.password.get())])
        result = c.fetchall()
        if result:
            self.logf.pack_forget()
            self.head.pack_forget()
            self.head = Label(self.master, text='CALLIBRATION', font=('', 35), pady=10)
            self.head.pack()
            self.calibratef.pack()

        else:
            ms.showerror('Oops!', 'Username Not Found.')

    def new_user(self):
        # Establish Connection
        with sqlite3.connect('User_Data.db') as db:
            c = db.cursor()

        # Find Existing username if any take proper action
        find_user = ('SELECT username FROM user WHERE username = ?')
        c.execute(find_user, [(self.n_username.get())])
        if c.fetchall():
            ms.showerror('Error!', 'Username Taken Try a Different One.')
        else:
            ms.showinfo('Success!', 'Account Created!')
            self.log()
        # Create New Account
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert, [(self.n_username.get()), (self.n_password.get())])
        db.commit()

        # Frame Packing Methords

    def log(self):  # login page

        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()

    def cr(self):  # register page

        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()

    def callibrateLeftHand(self):

        # Check if values already exist
        if not self.lefthandvalues:
            self.calibratef.pack_forget()
            self.callibratelefthandf.pack()
            self.lefthandvalues = bluetooth.callibrateLeftHand()
            self.callibratelefthandf.pack_forget()
            self.calibratef.pack()

        else:
            self.popup('LeftHand Already Calibrated')

    def callibrateRightHand(self):
        self.calibratef.pack_forget()
        self.callibratelefthandf.pack()
        self.righthandvalues = bluetooth.callibrateRightHand()
        self.callibratelefthandf.pack_forget()
        self.calibratef.pack()

    def callibrateLeftLeg(self):
        # remove previous frame and put current frame
        self.calibratef.pack_forget()
        self.callibratelefthandf.pack()
        # get values from bluetooth
        self.leftlegvalues = bluetooth.callibrateLeftLeg()
        # remove currebt framne and put previous frame
        self.callibratelefthandf.pack_forget()
        self.calibratef.pack()

    def callibrateRightLeg(self):
        self.calibratef.pack_forget()
        self.callibratelefthandf.pack()
        self.rightlegvalues = bluetooth.callibrateRightLeg()
        self.callibratelefthandf.pack_forget()
        self.calibratef.pack()

    def getMachineLearningPrediction(self):
        averagehandforce = (self.lefthandvalues[0] + self.righthandvalues[0]) / 2  # Average left and right hand forces
        averagehandflex = (self.lefthandvalues[1] + self.righthandvalues[1]) / 2  # Average left and right hand flex
        averagehandacceleration = (self.lefthandvalues[2] + self.righthandvalues[
            2]) / 2  # Average left and right hand acceleraction values
        averagelegforce = (self.rightlegvalues[0] + self.leftlegvalues[0] / 2)  # Average left and right leg forces
        averagelegacceleration = (
                    self.rightlegvalues[1] + self.leftlegvalues[1])  # Average left and right leg acceleration

        # Encode the data to categorial

    # Draw Widgets
    def widgets(self):
        self.head = Label(self.master, text='LOGIN', font=('', 35), pady=10)
        self.head.pack()
        self.logf = Frame(self.master, padx=10, pady=10)
        Label(self.logf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.logf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.logf, text=' Login ', bd=3, font=('', 15), padx=5, pady=5, command=self.login).grid()
        Button(self.logf, text=' Create Account ', bd=3, font=('', 15), padx=5, pady=5, command=self.cr).grid(row=2,
                                                                                                              column=1)
        self.logf.pack()

        self.crf = Frame(self.master, padx=10, pady=10)
        Label(self.crf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.crf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.crf, text='Create Account', bd=3, font=('', 15), padx=5, pady=5, command=self.new_user).grid()
        Button(self.crf, text='Go to Login', bd=3, font=('', 15), padx=5, pady=5, command=self.log).grid(row=2,
                                                                                                         column=1)
        self.calibratef = Frame(self.master, padx=10, pady=10)
        Button(self.calibratef, text='Calibrate Left Hand', bd=3, font=('', 15), padx=5, pady=5,
               command=self.callibrateLeftHand).grid()

        self.callibratelefthandf = Frame(self.master, padx=10, pady=10)
        Label(self.callibratelefthandf, text='Rotate Left Hand, Flex Fingers and Apply Force Simultaenously ',
              font=('', 20), pady=5, padx=5).grid(sticky=W)

    # self.calibratef= Frame(self.master,padx=10,pady=10)
    #  Button(self.crf, text='Callibrate Left Hand', bd=3, font=('', 15), padx=5, pady=5, command=self.new_user).grid()


if __name__ == '__main__':
    # Create Object
    # and setup window
    root = Tk()
    root.title('Login Form')
    # root.geometry('400x350+300+300')
    main(root)
    root.mainloop()

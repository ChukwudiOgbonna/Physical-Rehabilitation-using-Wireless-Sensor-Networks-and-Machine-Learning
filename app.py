# import all the relevant classes
import concurrent.futures
import datetime
import sqlite3
import time

import numpy as np
from kivy.app import App
from kivy.core.image import Image
from kivy.core.text import Label
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from matplotlib import pyplot as plt

import MachineLearning
import bluetooth
import pandas as pd

count=0
username = str
impairment = str
left_hand_values = list()
right_hand_values = list()
left_leg_values = list()
right_leg_values = list()
test_tuple = list()
exercise_tuple = list()
left_hand_dict=dict()
right_hand_dict=dict()
right_leg_dict=dict()
left_leg_dict=dict()




# print(df.head())
from pandas import array
def insertIntoDb(parameter):
    with sqlite3.connect('User_Data.db') as db:
        c = db.cursor()
        insert = "Update user set impairment = ? where username = ?"
        c.execute(insert,parameter)
        print(parameter)
        db.commit()



class calibrateLeftHandAccelerationWindow(Screen):
    def calibrate(self):
        global left_hand_values
        # Do collection in another thread
        try:
            return_value=bluetoothHandler.calibrateLeftHandAcceleration()
            left_hand_values.append(return_value)
            print("Left Hand Acceleration is "+ str(return_value))
            show_popup3()
        except:
            show_popup4()





    def back(self):
        sm.current = 'calibratelefthandwindow'


class calibrateLeftHandFlexWindow(Screen):
    def calibrate(self):
        global left_hand_values
        try:
            return_value = bluetoothHandler.calibrateLeftHandFlex()
            left_hand_values.append(return_value)
            print("Left Hand Flex is " + str(return_value))
            show_popup3()
        except:
            show_popup4()


    def back(self):
        sm.current = 'calibratelefthandwindow'


class calibrateLeftHandForceWindow(Screen):
    def calibrate(self):
        global left_hand_values
        try:
            return_value = bluetoothHandler.calibrateLeftHandForce()
            left_hand_values.append(return_value)
            print("Left hand force is " +str(return_value))
            show_popup3()
        except:
            show_popup4()

    def back(self):
        sm.current = 'calibratelefthandwindow'


class calibrateRightHandAccelerationWindow(Screen):
    def calibrate(self):
        global right_hand_values
        try:
            return_value = bluetoothHandler.calibrateRightHandAcceleration()
            right_hand_values.append(return_value)
            print("Right Hand Acceleration is "+ str(return_value))
            show_popup3()
        except:
            show_popup4()


    def back(self):
        sm.current = 'calibraterighthandwindow'


class calibrateRightHandFlexWindow(Screen):
    def calibrate(self):
        global right_hand_values
        try:
            return_value = bluetoothHandler.calibrateRightHandFlex()
            right_hand_values.append(return_value)
            print("Right Hand Flex is "+str(return_value))
            show_popup3()
        except:
            show_popup4()



    def back(self):
        sm.current = 'calibraterighthandwindow'


class calibrateRightHandForceWindow(Screen):
    def calibrate(self):
        global right_hand_values
        try:
            return_value = bluetoothHandler.calibrateRightHandForce()
            right_hand_values.append(return_value)
            print("Right Hand Force is "+ str(return_value))
            show_popup3()

        except:
            show_popup4()


    def back(self):
        sm.current = 'calibraterighthandwindow'


class calibrateRightLegAccelerationWindow(Screen):
    def calibrate(self):
        global right_leg_values
        try:
            return_value=bluetoothHandler.calibrateRightLegAcceleration()
            right_leg_values.append(return_value)
            print("Right Leg Acceleration is "+ str(return_value))
            show_popup3()
        except:
            show_popup4()



    def back(self):
        sm.current = 'calibraterightlegwindow'


class calibrateRightLegForceWindow(Screen):
    def calibrate(self):
        global right_leg_values
        try:
            return_value = bluetoothHandler.calibrateRightLegForce()
            right_leg_values.append(return_value)
            print("Right Leg Force is "+str(return_value))
            show_popup3()
        except:
            show_popup4()






    def back(self):
        sm.current = 'calibraterightlegwindow'


class calibrateLeftLegAccelerationWindow(Screen):
    def calibrate(self):
        global left_leg_values
        try:
            return_value = bluetoothHandler.calibrateLeftLegAcceleration()
            left_leg_values.append(return_value)
            print("Left Leg Acceleration is "+ str(return_value))
            show_popup3()
        except:
            show_popup4()


    def back(self):
        sm.current = 'calibrateleftlegwindow'


class calibrateLeftLegForceWindow(Screen):
    def calibrate(self):
        global left_leg_values
        try:
           return_value = bluetoothHandler.calibrateLeftLegForce()
           left_leg_values.append(return_value)
           print("Left Leg Force is "+ str(return_value))
           show_popup3()

        except:
            show_popup4()



    def back(self):
        sm.current = 'calibrateleftlegwindow'


class calibrateLeftHandWindow(Screen):
    pass


class calibrateRightHandWindow(Screen):
    pass


class calibrateLeftLegWindow(Screen):
    pass


class calibrateRightLegWindow(Screen):
    pass


class arthritisWindow(Screen):
    pass

class parkinsonDiseaseWindowExercise(Screen):
    def insertIntoDatabase(self):
        global left_hand_dict
        global right_hand_dict
        global left_leg_dict
        global right_leg_dict
        global username
        if left_hand_dict.get('force') != None:
            left_hand_force = left_hand_dict.get('force')
        else:
            left_hand_force = 0
        if left_hand_dict.get('flex') != None:
            left_hand_flex = left_hand_dict.get('flex')
        else:
            left_hand_flex = 0
        if left_hand_dict.get('acceleration') != None:
            left_hand_acceleration = left_hand_dict.get('acceleration')
        else:
            left_hand_acceleration = 0
        if right_hand_dict.get('force') != None:
            right_hand_force = left_hand_dict.get('force')
        else:
            right_hand_force = 0
        if right_hand_dict.get('flex') != None:
            right_hand_flex = left_hand_dict.get('flex')
        else:
            right_hand_flex = 0
        if right_hand_dict.get('acceleration') != None:
            right_hand_acceleration = left_hand_dict.get('acceleration')
        else:
            right_hand_acceleration = 0
        if left_leg_dict.get('force') != None:
            left_leg_force = left_hand_dict.get('force')
        else:
            left_leg_force = 0
        if left_hand_dict.get('acceleration') != None:
            left_leg_acceleration = left_hand_dict.get('acceleration')
        else:
            left_leg_acceleration = 0
        if right_leg_dict.get('force') != None:
            right_leg_force = left_hand_dict.get('force')
        else:
            right_leg_force = 0
        if right_leg_dict.get('acceleration') != None:
            right_leg_acceleration = left_hand_dict.get('acceleration')
        else:
            right_leg_acceleration = 0
        with sqlite3.connect('User_Data.db') as db:
            c = db.cursor()
            sql = 'INSERT INTO lefthandvalues(force,flex,acceleration,username,date) VALUES(?,?,?,?,?)'
            c.execute(sql, [left_hand_force, left_hand_flex, left_hand_acceleration, username, datetime.date.today()])
            db.commit()

        with sqlite3.connect('User_Data.db') as db:
            c = db.cursor()
            sql = 'INSERT INTO righthandvalues(force,flex,acceleration,username,date) VALUES(?,?,?,?,?)'
            c.execute(sql,
                      [right_hand_force, right_hand_flex, right_hand_acceleration, username, datetime.date.today()])
            db.commit()

        with sqlite3.connect('User_Data.db') as db:
            c = db.cursor()
            sql = 'INSERT INTO rightlegvalues(force,acceleration,username,date) VALUES(?,?,?,?)'
            c.execute(sql, [right_leg_force, right_leg_acceleration, username, datetime.date.today()])
            db.commit()

        with sqlite3.connect('User_Data.db') as db:
            c = db.cursor()
            sql = 'INSERT INTO leftlegvalues(force,acceleration,username,date) VALUES(?,?,?,?)'
            c.execute(sql, [left_leg_force, left_leg_acceleration, username, datetime.date.today()])
            db.commit()

        db.close()


class cerebralPalsyWindowExercise(Screen):
    def insertIntoDatabase(self):
        global left_hand_dict
        global right_hand_dict
        global left_leg_dict
        global right_leg_dict
        global username
        if left_hand_dict.get('force') != None:
            left_hand_force = left_hand_dict.get('force')
        else:
            left_hand_force = 0
        if left_hand_dict.get('flex') != None:
            left_hand_flex = left_hand_dict.get('flex')
        else:
            left_hand_flex = 0
        if left_hand_dict.get('acceleration') != None:
            left_hand_acceleration = left_hand_dict.get('acceleration')
        else:
            left_hand_acceleration = 0
        if right_hand_dict.get('force') != None:
            right_hand_force = left_hand_dict.get('force')
        else:
            right_hand_force = 0
        if right_hand_dict.get('flex') != None:
            right_hand_flex = left_hand_dict.get('flex')
        else:
            right_hand_flex = 0
        if right_hand_dict.get('acceleration') != None:
            right_hand_acceleration = left_hand_dict.get('acceleration')
        else:
            right_hand_acceleration = 0
        if left_leg_dict.get('force') != None:
            left_leg_force = left_hand_dict.get('force')
        else:
            left_leg_force = 0
        if left_hand_dict.get('acceleration') != None:
            left_leg_acceleration = left_hand_dict.get('acceleration')
        else:
            left_leg_acceleration = 0
        if right_leg_dict.get('force') != None:
            right_leg_force = left_hand_dict.get('force')
        else:
            right_leg_force = 0
        if right_leg_dict.get('acceleration') != None:
            right_leg_acceleration = left_hand_dict.get('acceleration')
        else:
            right_leg_acceleration = 0
        with sqlite3.connect('User_Data.db') as db:
            c = db.cursor()
            sql = 'INSERT INTO lefthandvalues(force,flex,acceleration,username,date) VALUES(?,?,?,?,?)'
            c.execute(sql, [left_hand_force, left_hand_flex, left_hand_acceleration, username, datetime.date.today()])
            db.commit()

        with sqlite3.connect('User_Data.db') as db:
            c = db.cursor()
            sql = 'INSERT INTO righthandvalues(force,flex,acceleration,username,date) VALUES(?,?,?,?,?)'
            c.execute(sql,
                      [right_hand_force, right_hand_flex, right_hand_acceleration, username, datetime.date.today()])
            db.commit()

        with sqlite3.connect('User_Data.db') as db:
            c = db.cursor()
            sql = 'INSERT INTO rightlegvalues(force,acceleration,username,date) VALUES(?,?,?,?)'
            c.execute(sql, [right_leg_force, right_leg_acceleration, username, datetime.date.today()])
            db.commit()

        with sqlite3.connect('User_Data.db') as db:
            c = db.cursor()
            sql = 'INSERT INTO leftlegvalues(force,acceleration,username,date) VALUES(?,?,?,?)'
            c.execute(sql, [left_leg_force, left_leg_acceleration, username, datetime.date.today()])
            db.commit()

        db.close()

class rightSideStrokeWindowExercise(Screen):
    def insertIntoDatabase(self):
        global left_hand_dict
        global right_hand_dict
        global left_leg_dict
        global right_leg_dict
        global username
        if left_hand_dict.get('force') != None:
            left_hand_force = left_hand_dict.get('force')
        else:
            left_hand_force = 0
        if left_hand_dict.get('flex') != None:
            left_hand_flex = left_hand_dict.get('flex')
        else:
            left_hand_flex = 0
        if left_hand_dict.get('acceleration') != None:
            left_hand_acceleration = left_hand_dict.get('acceleration')
        else:
            left_hand_acceleration = 0
        if right_hand_dict.get('force') != None:
            right_hand_force = left_hand_dict.get('force')
        else:
            right_hand_force = 0
        if right_hand_dict.get('flex') != None:
            right_hand_flex = left_hand_dict.get('flex')
        else:
            right_hand_flex = 0
        if right_hand_dict.get('acceleration') != None:
            right_hand_acceleration = left_hand_dict.get('acceleration')
        else:
            right_hand_acceleration = 0
        if left_leg_dict.get('force') != None:
            left_leg_force = left_hand_dict.get('force')
        else:
            left_leg_force = 0
        if left_hand_dict.get('acceleration') != None:
            left_leg_acceleration = left_hand_dict.get('acceleration')
        else:
            left_leg_acceleration = 0
        if right_leg_dict.get('force') != None:
            right_leg_force = left_hand_dict.get('force')
        else:
            right_leg_force = 0
        if right_leg_dict.get('acceleration') != None:
            right_leg_acceleration = left_hand_dict.get('acceleration')
        else:
            right_leg_acceleration = 0
        with sqlite3.connect('User_Data.db') as db:
            c = db.cursor()
            sql = 'INSERT INTO lefthandvalues(force,flex,acceleration,username,date) VALUES(?,?,?,?,?)'
            c.execute(sql, [left_hand_force, left_hand_flex, left_hand_acceleration, username, datetime.date.today()])
            db.commit()

        with sqlite3.connect('User_Data.db') as db:
            c = db.cursor()
            sql = 'INSERT INTO righthandvalues(force,flex,acceleration,username,date) VALUES(?,?,?,?,?)'
            c.execute(sql,
                      [right_hand_force, right_hand_flex, right_hand_acceleration, username, datetime.date.today()])
            db.commit()

        with sqlite3.connect('User_Data.db') as db:
            c = db.cursor()
            sql = 'INSERT INTO rightlegvalues(force,acceleration,username,date) VALUES(?,?,?,?)'
            c.execute(sql, [right_leg_force, right_leg_acceleration, username, datetime.date.today()])
            db.commit()

        with sqlite3.connect('User_Data.db') as db:
            c = db.cursor()
            sql = 'INSERT INTO leftlegvalues(force,acceleration,username,date) VALUES(?,?,?,?)'
            c.execute(sql, [left_leg_force, left_leg_acceleration, username, datetime.date.today()])
            db.commit()

        db.close()



class leftSideStrokeWindowExercise(Screen):
    def insertIntoDatabase(self):
        global left_hand_dict
        global right_hand_dict
        global left_leg_dict
        global right_leg_dict
        global username
        if left_hand_dict.get('force') != None:
            left_hand_force = left_hand_dict.get('force')
        else:
            left_hand_force = 0
        if left_hand_dict.get('flex') != None:
            left_hand_flex = left_hand_dict.get('flex')
        else:
            left_hand_flex = 0
        if left_hand_dict.get('acceleration') != None:
            left_hand_acceleration = left_hand_dict.get('acceleration')
        else:
            left_hand_acceleration = 0
        if right_hand_dict.get('force') != None:
            right_hand_force = left_hand_dict.get('force')
        else:
            right_hand_force = 0
        if right_hand_dict.get('flex') != None:
            right_hand_flex = left_hand_dict.get('flex')
        else:
            right_hand_flex = 0
        if right_hand_dict.get('acceleration') != None:
            right_hand_acceleration = left_hand_dict.get('acceleration')
        else:
            right_hand_acceleration = 0
        if left_leg_dict.get('force') != None:
            left_leg_force = left_hand_dict.get('force')
        else:
            left_leg_force = 0
        if left_hand_dict.get('acceleration') != None:
            left_leg_acceleration = left_hand_dict.get('acceleration')
        else:
            left_leg_acceleration = 0
        if right_leg_dict.get('force') != None:
            right_leg_force = left_hand_dict.get('force')
        else:
            right_leg_force = 0
        if right_leg_dict.get('acceleration') != None:
            right_leg_acceleration = left_hand_dict.get('acceleration')
        else:
            right_leg_acceleration = 0
        with sqlite3.connect('User_Data.db') as db:
            c = db.cursor()
            sql = 'INSERT INTO lefthandvalues(force,flex,acceleration,username,date) VALUES(?,?,?,?,?)'
            c.execute(sql, [left_hand_force, left_hand_flex, left_hand_acceleration, username, datetime.date.today()])
            db.commit()

        with sqlite3.connect('User_Data.db') as db:
            c = db.cursor()
            sql = 'INSERT INTO righthandvalues(force,flex,acceleration,username,date) VALUES(?,?,?,?,?)'
            c.execute(sql,
                      [right_hand_force, right_hand_flex, right_hand_acceleration, username, datetime.date.today()])
            db.commit()

        with sqlite3.connect('User_Data.db') as db:
            c = db.cursor()
            sql = 'INSERT INTO rightlegvalues(force,acceleration,username,date) VALUES(?,?,?,?)'
            c.execute(sql, [right_leg_force, right_leg_acceleration, username, datetime.date.today()])
            db.commit()

        with sqlite3.connect('User_Data.db') as db:
            c = db.cursor()
            sql = 'INSERT INTO leftlegvalues(force,acceleration,username,date) VALUES(?,?,?,?)'
            c.execute(sql, [left_leg_force, left_leg_acceleration, username, datetime.date.today()])
            db.commit()

        db.close()



class arthritisWindowExercise(Screen):
    def insertIntoDatabase(self):
        global left_hand_dict
        global right_hand_dict
        global left_leg_dict
        global right_leg_dict
        global username
        if left_hand_dict.get('force') != None:
            left_hand_force = left_hand_dict.get('force')
        else:
            left_hand_force = 0
        if left_hand_dict.get('flex') != None:
            left_hand_flex = left_hand_dict.get('flex')
        else:
            left_hand_flex = 0
        if left_hand_dict.get('acceleration') != None:
            left_hand_acceleration = left_hand_dict.get('acceleration')
        else:
            left_hand_acceleration = 0
        if right_hand_dict.get('force') != None:
            right_hand_force = left_hand_dict.get('force')
        else:
            right_hand_force = 0
        if right_hand_dict.get('flex') != None:
            right_hand_flex = left_hand_dict.get('flex')
        else:
            right_hand_flex = 0
        if right_hand_dict.get('acceleration') != None:
            right_hand_acceleration = left_hand_dict.get('acceleration')
        else:
            right_hand_acceleration = 0
        if left_leg_dict.get('force') != None:
            left_leg_force = left_hand_dict.get('force')
        else:
            left_leg_force = 0
        if left_hand_dict.get('acceleration') != None:
            left_leg_acceleration = left_hand_dict.get('acceleration')
        else:
            left_leg_acceleration = 0
        if right_leg_dict.get('force') != None:
            right_leg_force = left_hand_dict.get('force')
        else:
            right_leg_force = 0
        if right_leg_dict.get('acceleration') != None:
            right_leg_acceleration = left_hand_dict.get('acceleration')
        else:
            right_leg_acceleration = 0
        with sqlite3.connect('User_Data.db') as db:
            c = db.cursor()
            sql = 'INSERT INTO lefthandvalues(force,flex,acceleration,username,date) VALUES(?,?,?,?,?)'
            c.execute(sql, [left_hand_force, left_hand_flex, left_hand_acceleration, username, datetime.date.today()])
            db.commit()

        with sqlite3.connect('User_Data.db') as db:
            c = db.cursor()
            sql = 'INSERT INTO righthandvalues(force,flex,acceleration,username,date) VALUES(?,?,?,?,?)'
            c.execute(sql,
                      [right_hand_force, right_hand_flex, right_hand_acceleration, username, datetime.date.today()])
            db.commit()

        with sqlite3.connect('User_Data.db') as db:
            c = db.cursor()
            sql = 'INSERT INTO rightlegvalues(force,acceleration,username,date) VALUES(?,?,?,?)'
            c.execute(sql, [right_leg_force, right_leg_acceleration, username, datetime.date.today()])
            db.commit()

        with sqlite3.connect('User_Data.db') as db:
            c = db.cursor()
            sql = 'INSERT INTO leftlegvalues(force,acceleration,username,date) VALUES(?,?,?,?)'
            c.execute(sql, [left_leg_force, left_leg_acceleration, username, datetime.date.today()])
            db.commit()

        db.close()



class P(FloatLayout):  # Layout for the popup window
    pass


class P1(FloatLayout):  # Layout for the popup window
    pass


class P2(FloatLayout):
    pass
class P3(FloatLayout):
    pass


class FullImage(Image):
    pass


def show_popup3():
    show = P2()
    popupWindow = Popup(title=" PLEASE WAIT ,", content=show, size_hint=(None, None), size=(400, 400),
                        auto_dismiss=True)
    popupWindow.open()



def show_popup():  # Function to create popup window

    show = P()  # Create a new instance of the P class

    popupWindow = Popup(title="Popup Window", content=show, size_hint=(None, None), size=(400, 400))
    # Create the popup window

    popupWindow.open()  # show the pop


def show_popup2():  # Function to create popup window

    show = P1()  # Create a new instance of the P class

    popup = Popup(title='Popup Window',
                  content=show,
                  size_hint=(None, None), size=(400, 400))
    # Create the popup window

    popup.open()  # show the pop

def show_popup4():  # Function to create popup window

    show = P3()  # Create a new instance of the P class

    popup = Popup(title='Please try again',
                  content=show,
                  size_hint=(None, None), size=(400, 400))
    # Create the popup window
 
    popup.open()  # show the pop
# function that displays the content


class calibrateWindow(Screen):
    def getMlPrediction(self):
        global impairment
        global username
        global left_hand_values
        global right_hand_values
        global left_leg_values
        global right_leg_values
        for values in left_hand_values:
            test_tuple.append(values)
        for values in right_hand_values:
            test_tuple.append(values)
        for values in left_leg_values:
            test_tuple.append(values)
        for values in right_leg_values:
            test_tuple.append(values)
        pred = np.array(test_tuple)
        pred= pred.reshape(1,-1)
        my_model = model.getModel()
        np_array = np.array([1,1,1,1,1,1,1,1,1,1])
        np_array = np_array.reshape(1, -1)
        answer=int
        try:
            print(pred)
            answer = my_model.predict(pred)
        except:
            show_popup4()

        if answer == 0:
            impairment = 'arthritis'
            print(impairment)
            data = (impairment, username)
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.submit(insertIntoDb, data)
                sm.current = 'arthritiswindow'
        if answer == 1:
            impairment = 'cerebral palsy'
            print(impairment)
            data = (impairment, username)
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.submit(insertIntoDb, data)
                sm.current = 'cerebralpalsywindow'
        if answer == 2:
            impairment = 'left side stroke'
            data = (impairment, username)
            with concurrent.futures.ThreadPoolExecutor() as executor:
                data =(impairment,username)
                executor.submit(insertIntoDb, data)
                sm.current = 'leftsidedstrokewindow'
        if answer == 3:
            impairment= 'perfectly healthy'
            data = (impairment, username)
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.submit(insertIntoDb, data)
                sm.current = 'perfectlyhealthywindow'
        if answer == 4:
            impairment = 'parkinson'
            data = (impairment, username)
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.submit(insertIntoDb, data)
                sm.current = 'parkinsondiseasewindow'
        if answer == 5:
            impairment= 'right side stroke'
            data = (impairment, username)
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.submit(insertIntoDb, data )
                sm.current = 'rightsidedstrokewindow'


# class to accept user info and validate it
class loginWindow(Screen):
    def returnImageSource(self):
        return 'plot.png'
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def validate(self):
        # Check if text space is empty
        if self.ids.username.text == "":
            return
        else:
            with sqlite3.connect('User_Data.db') as db:
                c = db.cursor()
            # validating if the username already exists
            find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
            c.execute(find_user, [(self.ids.username.text), (self.ids.password.text)])
            result = c.fetchall()

            if result:
                global username
                username = self.ids.username.text
                sm.current = 'logdata'

            else:
                show_popup2()


# class to accept sign up info
class signupWindow(Screen):
    username = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def signupbtn(self):
        if self.ids.username.text == "" and self.ids.password == "":
            return
        else:
            with sqlite3.connect('User_Data.db') as db:
                c = db.cursor()

            # Find Existing username if any take proper action
            find_user = ('SELECT username FROM user WHERE username = ?')
            c.execute(find_user, [(self.ids.username.text)])
            if c.fetchall():
                show_popup()

            else:  # Create new account
                insert = 'INSERT INTO user(username,password) VALUES(?,?)'
                c.execute(insert, [(self.ids.username.text), (self.ids.password.text)])
                db.commit()
                sm.current = 'login'


# class to display validation result
class logDataWindow(Screen):
    def checkLastSession(self):
        global username
        with sqlite3.connect('User_Data.db') as db:
            c = db.cursor()
            # validating if the username already exists
            find_user = ('SELECT impairment FROM user WHERE username = ?')
            c.execute(find_user, username)
            result = c.fetchone()
            result = result[0]
            global impairment
            impairment = result
            print(result)
            if result == 'arthritis':
                sm.current = 'arthritiswindow'
            if result == 'cerebral palsy':
                sm.current = 'cerebralpalsywindow'
            if result == 'perfectly healthy':
                sm.current = 'perfectlyhealthywindow'
            if result == 'left side stroke':
                sm.current = 'leftsidedstrokewindow'
            if result == 'right side stroke':
                sm.current = 'rightsidedstrokewindow'



# class for managing screens
class windowManager(ScreenManager):
    pass




class cerebralPalsyWindow(Screen):
    pass


class rightSidedStrokeWindow(Screen):

    pass


class leftSidedStrokeWindow(Screen):
    pass


class parkinsonDiseaseWindow(Screen):
    pass

class leftHandValues(Screen):
    def changeImage(self):
        self.ids.image.source='plot.png'
    pass
class perfectlyHealthyWindow(Screen):
    pass


class RightHandFlexWindowExercise(Screen):
    global impairment
    def exercise(self):
        popup = show_popup3()
        values = bluetoothHandler.exerciseforRightHandFlex()
        global right_hand_dict
        right_hand_dict["flex"] = values
        popup.dismiss()

    def back(self):


        if impairment == 'arthritis':
            sm.current = 'arthritisexercisewindow'
        if impairment == 'cerebral palsy':
            sm.current = 'cerebralpalsywindowexercise'
        if impairment == 'parkinson':
            sm.current = 'parkinsondiseasewindowexercise'
        if impairment == 'left side stroke':
            sm.current = 'leftsidestrokewindowexercise'
        if impairment == 'right side stroke':
            sm.current = 'rightsidestrokewindowexercise'


class LeftHandFlexWindowExercise(Screen):
    def exercise(self):
        popup = show_popup3()
        values = bluetoothHandler.exerciseforLeftHandFlex()
        global left_hand_dict
        left_hand_dict["flex"] = values
        popup.dismiss()

    def back(self):
        global impairment
        if impairment == 'arthritis':
            sm.current = 'arthritisexercisewindow'
        if impairment == 'cerebral palsy':
            sm.current = 'cerebralpalsywindowexercise'
        if impairment == 'parkinson':
            sm.current = 'parkinsondiseasewindowexercise'
        if impairment == 'left side stroke':
            sm.current = 'leftsidestrokewindowexercise'
        if impairment == 'right side stroke':
            sm.current = 'rightsidestrokewindowexercise'


class RightHandForceWindowExercise(Screen):
    def exercise(self):
        popup = show_popup3()
        values = bluetoothHandler.exerciseForRightHandForce()
        global right_hand_dict
        right_hand_dict["force"] = values
        popup.dismiss()

    def back(self):
        global impairment
        if impairment == 'arthritis':
            sm.current = 'arthritisexercisewindow'
        if impairment == 'cerebral palsy':
            sm.current = 'cerebralpalsywindowexercise'
        if impairment == 'parkinson':
            sm.current = 'parkinsondiseasewindowexercise'
        if impairment == 'left side stroke':
            sm.current = 'leftsidestrokewindowexercise'
        if impairment == 'right side stroke':
            sm.current = 'rightsidestrokewindowexercise'


class LeftHandForceWindowExercise(Screen):
    def exercise(self):
        popup = show_popup3()
        values = bluetoothHandler.exerciseForLeftHandForce()
        global left_hand_dict
        left_hand_dict["force"] = values
        popup.dismiss()

    def back(self):
        global impairment
        if impairment == 'arthritis':
            sm.current = 'arthritisexercisewindow'
        if impairment == 'cerebral palsy':
            sm.current = 'cerebralpalsywindowexercise'
        if impairment == 'parkinson':
            sm.current = 'parkinsondiseasewindowexercise'
        if impairment == 'left side stroke':
            sm.current = 'leftsidestrokewindowexercise'
        if impairment == 'right side stroke':
            sm.current = 'rightsidestrokewindowexercise'


class RightHandAccelerationWindowExercise(Screen):
    def exercise(self):
        popup = show_popup3()
        values = bluetoothHandler.exerciseforRightElbow()
        global right_hand_dict
        right_hand_dict["acceleration"] = values
        popup.dismiss()

    def back(self):
        global impairment
        if impairment == 'arthritis':
            sm.current = 'arthritisexercisewindow'
        if impairment == 'cerebral palsy':
            sm.current = 'cerebralpalsywindowexercise'
        if impairment == 'parkinson':
            sm.current = 'parkinsondiseasewindowexercise'
        if impairment == 'left side stroke':
            sm.current = 'leftsidestrokewindowexercise'
        if impairment == 'right side stroke':
            sm.current = 'rightsidestrokewindowexercise'


class LeftHandAccelerationWindowExercise(Screen):
    def exercise(self):
        popup = show_popup3()
        values = bluetoothHandler.exerciseforLeftElbow()
        global left_hand_dict
        left_hand_dict["acceleration"]=values
        popup.dismiss()

    def back(self):
        global impairment
        if impairment == 'arthritis':
            sm.current = 'arthritisexercisewindow'
        if impairment == 'cerebral palsy':
            sm.current = 'cerebralpalsywindowexercise'
        if impairment == 'parkinson':
            sm.current = 'parkinsondiseasewindowexercise'
        if impairment == 'left side stroke':
            sm.current = 'leftsidestrokewindowexercise'
        if impairment == 'right side stroke':
            sm.current = 'rightsidestrokewindowexercise'


class RightLegAccelerationWindowExercise(Screen):
    def exercise(self):
        popup = show_popup3()
        values = bluetoothHandler.exerciseForRightKnee()
        global right_leg_dict
        right_leg_dict["acceleration"] = values
        popup.dismiss()

    def back(self):
        global impairment
        if impairment == 'arthritis':
            sm.current = 'arthritisexercisewindow'
        if impairment == 'cerebral palsy':
            sm.current = 'cerebralpalsywindowexercise'
        if impairment == 'parkinson':
            sm.current = 'parkinsondiseasewindowexercise'
        if impairment == 'left side stroke':
            sm.current = 'leftsidestrokewindowexercise'
        if impairment == 'right side stroke':
            sm.current = 'rightsidestrokewindowexercise'


class LeftLegAccelerationWindowExercise(Screen):
    def exercise(self):
        popup=show_popup3()
        values = bluetoothHandler.exerciseForLeftKnee()
        global left_leg_dict
        left_leg_dict["acceleration"] = values
        popup.dismiss()

    def back(self):
        global impairment
        if impairment == 'arthritis':
            sm.current = 'arthritisexercisewindow'
        if impairment == 'cerebral palsy':
            sm.current = 'cerebralpalsywindowexercise'
        if impairment == 'parkinson':
            sm.current = 'parkinsondiseasewindowexercise'
        if impairment == 'left side stroke':
            sm.current = 'leftsidestrokewindowexercise'
        if impairment == 'right side stroke':
            sm.current = 'rightsidestrokewindowexercise'


class RightLegForceWindowExercise(Screen):
    def exercise(self):
        popup = show_popup3()
        values = bluetoothHandler.exerciseForRightSole()
        global right_leg_dict
        right_leg_dict["force"] = values
        popup.dismiss()

    def back(self):
        global impairment
        if impairment == 'arthritis':
            sm.current = 'arthritisexercisewindow'
        if impairment == 'cerebral palsy':
            sm.current = 'cerebralpalsywindowexercise'
        if impairment == 'parkinson':
            sm.current = 'parkinsondiseasewindowexercise'
        if impairment == 'left side stroke':
            sm.current = 'leftsidestrokewindowexercise'
        if impairment == 'right side stroke':
            sm.current = 'rightsidestrokewindowexercise'


class LeftLegForceWindowExercise(Screen):
    def exercise(self):
        popup = show_popup3()
        values = bluetoothHandler.exerciseForLeftSole()
        global left_leg_dict
        left_leg_dict["acceleration"] = values
        popup.dismiss()

    def back(self):
        global impairment
        if impairment == 'arthritis':
            sm.current = 'arthritisexercisewindow'
        if impairment == 'cerebral palsy':
            sm.current = 'cerebralpalsywindowexercise'
        if impairment == 'parkinson':
            sm.current = 'parkinsondiseasewindowexercise'
        if impairment == 'left side stroke':
            sm.current = 'leftsidestrokewindowexercise'
        if impairment == 'right side stroke':
            sm.current = 'rightsidestrokewindowexercise'


class ResultsWindow(Screen):
    def changeImageLeftHand(self):
        self.ids.image.source = 'lefthand.png'
    def plotLeftHand(self):
        global username
        with sqlite3.connect('User_Data.db') as db:
            c = db.cursor()
            # validating if the username already exists
        find_user = ('SELECT * FROM lefthandvalues WHERE username = ?')
        cols = ['id','username', 'Force(Newton)', 'Flex(Degrees)', 'rotation speed(rad/s)', 'date']
        c.execute(find_user, [username])
        result = c.fetchall()
        df = pd.DataFrame(result, columns=cols)

        df = df.drop(columns=['id','username', 'date'])
        print(df.head())

        df.plot(kind="bar")

        plt.title("Left Hand Values")
        plt.xlabel("Type of parameter")
        plt.ylabel("Values")
        str = "lefthand"
        plt.savefig(str, dpi=300, bbox_inches='tight')

    def changeImageRightHand(self):
        self.ids.image.source = 'righthand.png'

    def plotRightHand(self):
        with sqlite3.connect('User_Data.db') as db:
            c = db.cursor()
            # validating if the username already exists
        find_user = ('SELECT * FROM righthandvalues WHERE username = ?')
        cols = ['id','username', 'Force(Newton)', 'Flex(Degrees)', 'rotation speed(rad/s)', 'date']
        c.execute(find_user, [username])
        result = c.fetchall()
        df = pd.DataFrame(result, columns=cols)

        df = df.drop(columns=['id','username', 'date'])
        print(df.head())
        df.plot(kind="bar")

        plt.title("Right Hand Values")
        plt.xlabel("Type of parameter")
        plt.ylabel("Values")
        str = "righthand"
        plt.savefig(str, dpi=300, bbox_inches='tight')
    def changeImageLeftLeg(self):
        self.ids.image.source = 'leftleg.png'

    def plotLeftLeg(self):
        with sqlite3.connect('User_Data.db') as db:
            c = db.cursor()
            # validating if the username already exists
        find_user = ('SELECT * FROM leftlegvalues WHERE username = ?')
        cols = ['id','username', 'Force(Newton)', 'rotation speed(rad/s)', 'date']
        c.execute(find_user, [username])
        result = c.fetchall()
        df = pd.DataFrame(result, columns=cols)

        df = df.drop(columns=['id','username', 'date'])
        print(df.head())

        df.plot(kind="bar")

        plt.title("Left Leg Values")
        plt.xlabel("Type of parameter")
        plt.ylabel("Values")
        str = "leftleg"
        plt.savefig(str, dpi=300, bbox_inches='tight')

    def changeImageRightLeg(self):
        self.ids.image.source = 'rightleg.png'

    def plotRightLeg(self):
        with sqlite3.connect('User_Data.db') as db:
            c = db.cursor()
            # validating if the username already exists
        find_user = ('SELECT * FROM rightlegvalues WHERE username = ?')
        cols = ['id','username', 'Force(Newton)', 'rotation speed(rad/s)', 'date']
        c.execute(find_user, [username])
        result = c.fetchall()
        df = pd.DataFrame(result, columns=cols)

        df = df.drop(columns=['id','username', 'date'])
        print(df.head())
        df.plot(kind="bar")

        plt.title("Right Leg Values")
        plt.xlabel("Type of parameter")
        plt.ylabel("Values")
        str = "rightleg"
        plt.savefig(str, dpi=300, bbox_inches='tight')



# kv file
kv = Builder.load_file('../../PycharmProjects/python app/login.kv')
sm = windowManager()

# reading all the data stored

# adding screens
sm.add_widget(loginWindow(name='login'))
sm.add_widget(signupWindow(name='signup'))
sm.add_widget(logDataWindow(name='logdata'))
sm.add_widget(calibrateWindow(name='calibrateWindow'))
sm.add_widget(calibrateLeftHandWindow(name='calibratelefthandwindow'))
sm.add_widget(calibrateLeftLegWindow(name='calibrateleftlegwindow'))
sm.add_widget(calibrateRightLegWindow(name='calibraterightlegwindow'))
sm.add_widget(calibrateRightHandWindow(name='calibraterighthandwindow'))
sm.add_widget(calibrateLeftHandFlexWindow(name="calibratelefthandflexwindow"))
sm.add_widget(calibrateLeftHandForceWindow(name='calibratelefthandforcewindow'))
sm.add_widget(calibrateLeftHandAccelerationWindow(name='calibratelefthandaccelerationwindow'))
sm.add_widget(calibrateRightHandFlexWindow(name="calibraterighthandflexwindow"))
sm.add_widget(calibrateRightHandForceWindow(name='calibraterighthandforcewindow'))
sm.add_widget(calibrateRightHandAccelerationWindow(name='calibraterighthandaccelerationwindow'))
sm.add_widget(calibrateLeftLegForceWindow(name='calibrateleftlegforcewindow'))
sm.add_widget(calibrateLeftLegAccelerationWindow(name='calibrateleftlegaccelerationwindow'))
sm.add_widget(calibrateRightLegForceWindow(name='calibraterightlegforcewindow'))
sm.add_widget(calibrateRightLegAccelerationWindow(name='calibraterightlegaccelerationwindow'))
sm.add_widget(arthritisWindow(name='arthritiswindow'))
sm.add_widget(cerebralPalsyWindow(name='cerebralpalsywindow'))
sm.add_widget(rightSidedStrokeWindow(name='rightsidedstrokewindow'))
sm.add_widget(leftSidedStrokeWindow(name='leftsidedstrokewindow'))
sm.add_widget(parkinsonDiseaseWindow(name='parkinsondiseasewindow'))
sm.add_widget(perfectlyHealthyWindow(name='perfectlyhealthywindow'))
sm.add_widget(arthritisWindowExercise(name='arthritisexercisewindow'))
sm.add_widget(cerebralPalsyWindowExercise(name='cerebralpalsywindowexercise'))
sm.add_widget(parkinsonDiseaseWindowExercise(name='parkinsondiseasewindowexercise'))
sm.add_widget(leftSideStrokeWindowExercise(name='leftsidestrokewindowexercise'))
sm.add_widget(rightSideStrokeWindowExercise(name='rightsidestrokewindowexercise'))
sm.add_widget(RightHandForceWindowExercise(name='righthandforcewindowexercise'))
sm.add_widget(LeftHandForceWindowExercise(name='lefthandforcewindowexercise'))
sm.add_widget(RightHandFlexWindowExercise(name='righthandflexwindowexercise'))
sm.add_widget(LeftHandFlexWindowExercise(name='lefthandflexwindowexercise'))
sm.add_widget(RightHandAccelerationWindowExercise(name='righthandaccelerationwindowexercise'))
sm.add_widget(LeftHandAccelerationWindowExercise(name='lefthandaccelerationwindowexercise'))
sm.add_widget(RightLegForceWindowExercise(name='rightlegforcewindowexercise'))
sm.add_widget(LeftLegForceWindowExercise(name='leftlegforcewindowexercise'))
sm.add_widget(RightLegAccelerationWindowExercise(name='rightlegaccelerationwindowexercise'))
sm.add_widget(LeftLegAccelerationWindowExercise(name='leftlegaccelerationwindowexercise'))
sm.add_widget(ResultsWindow(name='resultswindow'))
sm.add_widget(leftHandValues(name="lefthandvalues"))
# class that builds gui
class loginMain(App):
    def build(self):
        return sm


# driver function
if __name__ == "__main__":
    with sqlite3.connect('User_Data.db') as db:
        c = db.cursor()

    c.execute(
        'CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL PRIMARY KEY,password TEXT NOT NULL,impairment TEXT );')
    c.execute(
        'CREATE TABLE IF NOT EXISTS lefthandvalues(id INTEGER NOT NULL PRIMARY KEY, username TEXT NOT NULL,force REAL NOT NULL,flex REAL NOT NULL ,acceleration REAL NOT NULL, date TEXT );')
    c.execute(
        'CREATE TABLE IF NOT EXISTS righthandvalues(id INTEGER NOT NULL PRIMARY KEY, username TEXT NOT NULL,force REAL,flex REAL ,acceleration REAL, date TEXT);')
    c.execute(
        'CREATE TABLE IF NOT EXISTS leftlegvalues(id INTEGER NOT NULL PRIMARY KEY, username TEXT NOT NULL,force REAL ,acceleration REAL, date TEXT);')
    c.execute(
        'CREATE TABLE IF NOT EXISTS rightlegvalues(id INTEGER NOT NULL PRIMARY KEY, username TEXT NOT NULL,force REAL ,acceleration REAL, date TEXT);')
    db.commit()
    db.close()
    model = MachineLearning.ML()
    bluetoothHandler = bluetooth.BluetoothHandler()
    loginMain().run()
    print(impairment)

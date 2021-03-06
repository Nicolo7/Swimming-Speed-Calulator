# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 18:29:22 2021

@author: nicol
"""

import os
import time
import datetime
import LCD

root_path = os.path.dirname(os.path.realpath(__file__))
user_path = os.path.join(root_path, 'Users.txt')
userList=[]
speedList=[]
weightList=[]

EMULATE_HX711=False

referenceUnit = 57

if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    print('ERROR, HX711.py NOT FOUND')
    exit(1)

def cleanAndExit():
    print("Cleaning...")

    if not EMULATE_HX711:
        GPIO.cleanup()
    print("ENDING SWIM SPEED TEST")
    
hx = HX711(5, 6)
hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(referenceUnit)

lcd = LCD.swimLCD()

class Swimmer():
    
    def __init__(self, name):
        
        if self.userCheck(name):
            self.name = name
            for x in range(len(userList)):
                if userList[x] == self.name:
                    self.speed = speedList[x]
                    self.weight = weightList[x]
        else:
            time.sleep(1)
            print('\nUser not found!')
            print('1::Switch Users')
            print('2::Create New User')
            choice = input('Type here: ')
                
            while(True):
                if (choice == '1'):
                    print("SWITCHING USERS")
                    self.switchUsers()
                    break
                elif (choice == '2'):
                    print('CREATING NEW USER')
                    time.sleep(0.75)
                    self.createNewUser()
                    break
                else:
                    print('\n************ERROR************\n\nInvalid Input.\n')
                    time.sleep(1)
                    print('1::Switch Users')
                    print('2::Create New User')
                    choice = input('Type here: ')
        
    def userCheck(self, name):
        if name in userList:
            return True
        else:
            return False
        
    def createNewUser(self):
        newName = input("Who is the new user?\n")
        self.name = newName
        self.speed = 10  # Default Setting.
        newWeight = input("How much do you weigh? (lbs)\n")
        self.weight = newWeight
        print('Nice to meet you ', self.name, '\n')
        print('Name: ', self.name)
        print('Speed: ', self.speed)
        print('Weight: ', self.weight)
        print('\n')
        userList.append(self.name)
        speedList.append(self.speed)
        weightList.append(self.weight)
        self.save()
        time.sleep(1)
        
    def save(self):
        with open(user_path, 'w') as filestream:
            for x in range(len(userList)):
                line = userList[x]
                line += ','
                line += str(speedList[x])   # line = name,speed,weight\n
                line += ','
                line += weightList[x]
                if not line.endswith('\n'): # When new user is created, a
                    line += '\n'            # newline doesnt get added.
                filestream.write(line)
                
    def switchUsers(self):
        print('Please enter a username you would like to switch to!')
        switch = input('Type here: ')
        
        while(self.userCheck(switch) == False):
            print('ERROR. User Not found.\nEnter in a new name.')
            switch = input('Type here: ')
                
        self.name = switch
        for x in range(len(userList)):
            if userList[x] == self.name:
                self.speed = speedList[x]
                self.weight = weightList[x]
        print('Welcome back ', self.name)
        
    def showUserInfo(self):
        print('User: ', self.name, '\nSpeed: ', self.speed, '\nWeight: ', self.weight)
        
    def showName(self):
        return self.name
    
    def changeWeight(self):
        newWeight = input('Please enter your new weight!\n')
        self.weight = newWeight
        for x in range(len(userList)):
            if userList[x] == self.name:
                weightList[x] = self.weight
        print('Change Successful!')
        self.showUserInfo()
    
    def swimTest(self):
        print('Please wait to apply any force as we begin to calibrate in 5 seconds.')
        time.sleep(1)
        print('Calibrating in 4 seconds.')
        time.sleep(1)
        print('Calibrating in 3 seconds.')
        time.sleep(1)
        print('Calibrating in 2 seconds.')
        time.sleep(1)
        print('Calibrating in 1 seconds.')
        time.sleep(1)
        print('***CALIBRATING***')
        
        hx.reset()
        hx.tare()
        
        print("Calibration complete!\n\n***BEGIN SWIMMING IN 5 SECONDS***\n\n")
        time.sleep(5)
        
        lastupdate = int(datetime.datetime.now().strftime("%S"))
        checkTime = lastupdate + 3
        if lastupdate == 57:
            checkTime = 0
        elif lastupdate == 58:
            checkTime = 1
        elif lastupdate == 59:
            checkTime = 2
        elif lastupdate == 60:
            checkTime = 3
        
        last50 = []
        
        while True:
            try:
                val = hx.get_weight(5)
                weight = round(val)*10          # grams
                force = weight * 0.098          # kg * m/s^2
                #print('weight: ', weight)
                #print('force: ', force)
                
                if len(last50) == 50:
                    last50.pop(0)
                else:
                    last50.append(force)
        
                hx.power_down()
                hx.power_up()
                time.sleep(0.01)
                
                current = int(datetime.datetime.now().strftime("%S"))
    
                if (checkTime == current):
                    lastupdate = int(datetime.datetime.now().strftime("%S"))
                    checkTime = lastupdate + 3
                    if lastupdate == 57:
                        checkTime = 0
                    elif lastupdate == 58:
                        checkTime = 1
                    elif lastupdate == 59:
                        checkTime = 2
                    elif lastupdate == 60:
                        checkTime = 3
                        
                    avgForce = 0
                    for x in last50:
                        avgForce += x
                    avgForce = avgForce/50
                    mass = int(self.weight)/2.205
                    speed = (avgForce * 3)/mass
                    
                    print(speed)
                    lcd.clearLcd()
                    firstline = 'Speed: '
                    firstline += speed
                    firstline += ' m/s'
                    secondline = 'User: '
                    secondline += currentSwimmer.showName()
                    lcd.lcdShowMessage(firstline, secondline)
        
            except (KeyboardInterrupt):
                cleanAndExit()
                lcd.clearLcd
                break

if __name__ == '__main__':
    
    with open(user_path, 'r') as filestream:
        for line in filestream:
            currentLine = line.split(',')
            userList.append(currentLine[0])
            speedList.append(currentLine[1])
            weightList.append(currentLine[2])
                
    user = input("Good afternoon. Who is using this program?\n")
    
    currentSwimmer = Swimmer(user)
    
    MMchoice = 7
    
    # MAIN MENU
    while (int(MMchoice) != 5):
        firstline = 'Hello '
        firstline += currentSwimmer.showName()
        secondline = 'Weight: '
        secondline += currentSwimmer.weight
        lcd.lcdShowMessage(firstline, secondline)
        
        print('What would you like to do today?')
        print('0 :: Switch Users')
        print('1 :: Create a new user')
        print('2 :: Do a speed test!')
        line4 = '3 :: Show '
        line4 += currentSwimmer.showName()
        line4 += '\'s stats'
        print(line4)
        print('4 :: Change weight')
        print('5 :: Exit')
        MMchoice = input('Type here: ')
        
        if(int(MMchoice) == 0):
            print('OPTION 0 HAS BEEN CHOSEN')
            currentSwimmer.switchUsers()
            
        elif(int(MMchoice) == 1):
            print('OPTION 1 HAS BEEN CHOSEN')
            currentSwimmer.createNewUser()
            
        elif(int(MMchoice) == 2):
            print('OPTION 2 HAS BEEN CHOSEN')
            currentSwimmer.swimTest()
            
        elif(int(MMchoice) == 3):
            print('Now showing stats!')
            time.sleep(1)
            currentSwimmer.showUserInfo()
            time.sleep(2)
            
        elif(int(MMchoice) == 4):
            currentSwimmer.changeWeight()
            
        elif(int(MMchoice) == 5):
            print('Thank you for using the system.\nHave a nice day!')
            
        else:
            print('ERROR. INVALID INPUT PLEASE TRY AGAIN.')
            time.sleep(1)
        
        currentSwimmer.save()

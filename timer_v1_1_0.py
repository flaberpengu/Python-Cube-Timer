##CUBE TIME

import time
import tkinter as tk
import math

class cubeTimer():
    def __init__(self):
        ##Defines parts of timer
        self.start_time = 0.0
        self.end_time = 0.0
        self.difference = 0.0
        self.formatted = ''
        self.hrs = 0
        self.mins = 0
        self.secs = 0
        self.ms = 0

    def get_time(self,num):
        ##Gets time since epoch
        if num == 1:
            self.start_time = time.time()
        elif num == 2:
            self.end_time = time.time()

    def get_difference(self):
        ##Finds difference bwteen start and end times
        self.difference = self.end_time - self.start_time
        return self.difference

    def format_time(self,time):
        if time >= 3600:
            self.hrs = time // 3600
            time -= (self.hrs*3600)
        if time >= 60:
            self.mins = time // 60
            time -= (self.mins*60)
        self.secs = time // 1
        self.secs = math.floor(self.secs)
        time -= (self.secs)
        if self.hrs >= 1:
            self.formatted = (str(self.hrs) + ':' + str(self.mins) + ':' + str(self.secs) + '.' + str(math.floor((round(time,3))*1000)))
        elif self.mins >= 1:
            self.formatted = (str(self.mins) + ':' + str(self.secs) + '.' + str(math.floor((round(time,3))*1000)))
        return self.formatted
        


class cubeGUI():
    def __init__(self):
        ##Instance variables for later use
        self.num = 0
        self.time_difference = 0
        ##Creates instance of timer class
        self.timer = cubeTimer()
        ##Creates GUI
        self.root = tk.Tk()
        self.title_label = tk.Label(text='Timer v1.1',height=5,width=10)
        self.title_label.grid(row=0,column=0)
        self.time_label = tk.Label(text='-',height=5,width=10)
        self.time_label.grid(row=1,column=0)
        self.start_button = tk.Button(text='Start',height=5,width=10,command=self.start_process)
        self.start_button.grid(row=2,column=0)
        self.end_button = tk.Button(text='End',state=tk.DISABLED,height=5,width=10,command=self.end_process)
        self.end_button.grid(row=2,column=1)

    def start_process(self):
        ##Sets variable
        self.num = 1
        ##Calls timer to get time
        self.timer.get_time(self.num)
        ##Configures necessary buttons
        self.start_button.configure(state=tk.DISABLED)
        self.end_button.configure(state=tk.NORMAL)

    def end_process(self):
        ##Sets variable
        self.num = 2
        ##Calls timer to get time
        self.timer.get_time(self.num)
        ##Configures necessary button
        self.end_button.configure(state=tk.DISABLED)
        ##Calls time difference
        self.time_difference = self.timer.get_difference()
        ##Puts it on screen
        self.time_label.configure(text=self.timer.format_time(self.time_difference))

myTimer = cubeGUI()

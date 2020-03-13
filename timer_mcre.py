import time
import tkinter as tk

class cubeTimer():
    def __init__(self):
        ##Defines parts of timer
        self.start_time = 0.0
        self.end_time = 0.0
        self.difference = 0.0

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

class cubeGUI():
    def __init__(self):
        ##Instance variables for later use
        self.num = 0
        self.time_difference = 0
        self.flag = False
        ##Creates instance of timer class
        self.timer = cubeTimer()
        ##Creates GUI
        self.root = tk.Tk()
        ##Label to show the solve time
        self.time_label = tk.Label(text='-',height=5,width=10)
        self.time_label.grid(row=1,columnspan=2,sticky=tk.W)
        ##Button to start timer
        self.start_button = tk.Button(text='Start',height=5,width=10,command=self.start_process)
        self.start_button.grid(row=2,column=0)
        ##Button to end timer, initialised as disabled
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
        while self.flag == False:
            self.time_difference = self.timer.get_difference()
            self.time_label.configure(text=self.time_difference)
            time.sleep(0.1)

    def end_process(self):
        ##Sets variable
        self.num = 2
        ##Calls timer to get time
        self.timer.get_time(self.num)
        ##Updates flag
        self.flag = True
        ##Configures necessary button
        self.end_button.configure(state=tk.DISABLED)
        ##Calls time difference
        self.time_difference = self.timer.get_difference()
        ##Puts it on screen
        self.time_label.configure(text=self.time_difference)

myTimer = cubeGUI()

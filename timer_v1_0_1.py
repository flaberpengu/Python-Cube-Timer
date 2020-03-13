##CUBE TIMER

import time
import tkinter as tk
import threading

global start_time
start_time = 0.0
global end_time
end_time = 0.0
global sleep_time
sleep_time = 0.0
global count
count = False

def get_time():
    temp_time = time.time()
    return temp_time

##start = input("y or n")
##if start == 'y':
##    start_time = get_time()
##end = input("y")
##end_time = get_time()
##difference = end_time - start_time
##print(difference)

def start():
    start_button.configure(state=tk.DISABLED)
    end_button.configure(state=tk.NORMAL)
    global start_time
    start_time = get_time()
    global count
    count = True
    sleep_timer()

def sleep_timer():
    def run():
        global count
        global sleep_time
        while count == True:
            time.sleep(0.1)
            sleep_time += 0.1
            change_count_label()
            if count == False:
                break
    thread = threading.Thread(target=run)
    thread.start()

def end():
    end_button.configure(state=tk.DISABLED)
    global end_time
    end_time = get_time()
    global count
    count = False
    display_difference()

root = tk.Tk()
title_label = tk.Label(text='Timer v1.0.1')
title_label.grid(row=0,column=0)
time_label = tk.Label(text='-')
time_label.grid(row=1,column=0)
count_label = tk.Label(text='-')
count_label.grid(row=3,column=0)
start_button = tk.Button(text='Start',command=start)
start_button.grid(row=2,column=0)
end_button = tk.Button(text='End',command=end,state=tk.DISABLED)
end_button.grid(row=2,column=1)

def display_difference():
    global start_time
    global end_time
    difference = end_time - start_time
    round(difference,2)
    time_label.configure(text=str(difference))

def change_count_label():
    global sleep_time
    count_label.configure(text=str(sleep_time))



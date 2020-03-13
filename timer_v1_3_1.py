import tkinter as tk
import time
import math
from random import randint

class CubeTimer(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.timer = ' '
        self.root = master
        self.start_time = 0.0
        self.end_time = 0.0
        self.final_time = 0.0
        self.difference = 0.0
        self.hrs = 0
        self.mins = 0
        self.secs = 0
        self.formatted = ''
        self.num = 1
        self.scramble = ''
        self.char = 'p'
        self.previous_move = 'q'
        self.moves = ["R","F","U","L","B","D","R'","F'","U'","L'","B'","D'","R2","F2","U2","L2","B2","D2"]
        self.randnum = 99
        self.count = 0
        ##Title label showing version number
        self.title_label = tk.Label(text='Timer v1.3.1',height=5)
        self.title_label.grid(row=0,columnspan=2,sticky=tk.W)
        ##Scramble label
        self.scramble_label = tk.Label(text='-',height=5)
        self.scramble_label.grid(row=1,columnspan=2,sticky=tk.W)
        self.root.bind('n',self.gen_scramble_b,'+')
        ##Label to show the solve time
        self.time_label = tk.Label(text='-',height=5)
        self.time_label.grid(row=2,columnspan=2,sticky=tk.W)
        ##Button to start timer
        self.start_button = tk.Button(text='Start',height=5,width=20,command=self.start_process)
        self.start_button.grid(row=3,column=0)
        ##Binds space to begin program
        self.root.bind('<space>',self.start_process_b,'+')
        ##Button to end timer, initialised as disabled
        self.end_button = tk.Button(text='End',state=tk.DISABLED,height=5,width=20,command=self.end_process)
        self.end_button.grid(row=3,column=1)
        ##Info label
        self.info_label = tk.Label(text='Press space to use buttons\nPress r after a solve to reset the timer to 0\nPress n after a scramble or solve to generate a new scramble')
        self.info_label.grid(row=4,sticky=tk.W,columnspan=2)
        self.gen_scramble()

    def gen_scramble(self):
        for i in range(20):
            self.count += 1
            self.randnum = randint(0,len(self.moves)-1)
            self.char = self.moves[self.randnum]
            while (self.char == self.previous_move) or (self.char[0] == self.previous_move[0]):
                self.randnum = randint(0,len(self.moves)-1)
                self.char = self.moves[self.randnum]
            if self.count == 20:
                self.scramble = self.scramble + self.char
            else:
                self.scramble = self.scramble + self.char + str(' ')
            self.previous_move = self.char
        self.scramble_label.configure(text=self.scramble)
        self.scramble = ''
        self.previous_move = 'q'
        self.count = 0
        self.char = 'p'

    def gen_scramble_b(self,event):
        self.gen_scramble()

    def config_time(self,gtext):
        self.time_label.configure(text=gtext)

    def get_time(self,num):
        if num == 1:
            self.start_time = time.time()
        elif num == 2:
            self.end_time = time.time()
            return self.end_time
        elif num == 3:
            self.final_time = time.time()
            return self.final_time

    def get_difference(self,time):
        self.difference = time-self.start_time
        return self.difference

    def get_and_format_time(self,time):
        if time >= 3600:
            self.hrs = stime // 3600
            self.hrs = math.floor(self.hrs)
            time -= (self.hrs*3600)
        ##Creates minutes if needed
        if time >= 60:
            self.mins = time // 60
            self.mins = math.floor(self.mins)
            time -= (self.mins*60)
        ##Creates seconds (time = ms by the end)
        self.secs = time // 1
        self.secs = math.floor(self.secs)
        time -= (self.secs)
        ##Formats time as necessary
        if self.hrs >= 1:
            self.formatted = (str(self.hrs) + ':' + str(self.mins) + ':' + str(self.secs) + '.' + str(math.floor((round(time,3))*1000)))
        elif self.mins >= 1:
            self.formatted = (str(self.mins) + ':' + str(self.secs) + '.' + str(math.floor((round(time,3))*1000)))
        elif self.mins == 0:
            self.formatted = (str(self.secs) + '.' + str(math.floor((round(time,3))*1000)))
        return self.formatted

    def timer_tick(self):
        self.config_time(self.get_and_format_time(self.get_difference(self.get_time(self.num))))
        self.timer = self.after(10, self.timer_tick) # schedule this method to be called again in 1,000 millisconds (1 second)

    def start_process(self):
        ##Configures necessary buttons
        if self.num != 1:
            self.root.unbind('r')
        self.num = 1
        self.start_button.configure(state=tk.DISABLED)
        self.root.unbind('<space>')
        self.root.unbind('n')
        self.get_time(self.num)
        self.num = 2
        self.end_button.configure(state=tk.NORMAL)
        self.root.bind('<space>',self.end_process_b,'+')
        self.timer_tick()

    def start_process_b(self,event):
        self.start_process()

    def reset(self,event):
        self.start_button.configure(state=tk.NORMAL)
        self.gen_scramble()
        self.config_time('-')
        self.root.bind('<space>',self.start_process_b,'+')
        self.root.bind('n',self.gen_scramble_b,'+')

    def end_process(self):
        self.after_cancel(self.timer) # cancel the scheduled method call
        ##Configures necessary button
        self.num = 3
        self.end_button.configure(state=tk.DISABLED)
        self.root.unbind('<space>')
        self.config_time(self.get_and_format_time(self.get_difference(self.get_time(self.num))))
        self.root.bind('r',self.reset,'+')

    def end_process_b(self,event):
        self.end_process()

def main():
    root = tk.Tk()
    myTimer = CubeTimer(root)
    root.mainloop()

if __name__ == "__main__":
    main()

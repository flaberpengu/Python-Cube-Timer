import tkinter as tk

class CubeTimer(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.timer = ' '
        self.time_value = tk.IntVar()

        ##Label to show the solve time
        time_label = tk.Label(self, textvariable=self.time_value,height=5,width=10)
        time_label.grid(row=1,columnspan=2,sticky=tk.W)
        ##Button to start timer
        self.start_button = tk.Button(self, text='Start',height=5,width=10,command=self.start_process)
        self.start_button.grid(row=2,column=0)
        ##Button to end timer, initialised as disabled
        self.end_button = tk.Button(self, text='End',state=tk.DISABLED,height=5,width=10,command=self.end_process)
        self.end_button.grid(row=2,column=1)

    def timer_tick(self):
        self.time_value.set(self.time_value.get() + 1)
        self.timer = self.after(1000, self.timer_tick) # schedule this method to be called again in 1,000 millisconds (1 second)

    def start_process(self):
        ##Configures necessary buttons
        self.start_button.configure(state=tk.DISABLED)
        self.end_button.configure(state=tk.NORMAL)
        self.timer_tick()

    def end_process(self):
        self.after_cancel(self.timer) # cancel the scheduled method call

        ##Configures necessary button
        self.end_button.configure(state=tk.DISABLED)
        self.start_button.configure(state=tk.NORMAL)

def main():
    root = tk.Tk()
    myTimer = CubeTimer(root)
    myTimer.pack()
    root.mainloop()

if __name__ == "__main__":
    main()

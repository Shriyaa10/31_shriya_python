import tkinter as tk 
r = tk.Tk() 
r.title('Counting Seconds') 
button = tk.Button(r, text='Start', width=30, command=r.destroy) 
button.pack() 
r.mainloop() 

from tkinter import *
master = Tk() 
w = Canvas(master, width=80, height=60) 
w.pack() 
canvas_height=40
canvas_width=400
y = int(canvas_height / 2) 
w.create_line(0, y, canvas_width, y ) 
mainloop() 

#importing libraries
from tkinter import * 

tk = Tk()
tk.title('AllTech - Bouncing ball')
tk.resizable(False, False)
#creating robot and box
WIDTH, HEIGHT = 1000, 800
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()
#now we set starting point 0,0 as robot should start from center
radius = 50 
canvas_middle = [int(canvas['width'])/2, int(canvas['height'])/2]
ball = canvas.create_oval(canvas_middle[0] - radius, canvas_middle[1] - radius, canvas_middle[0] + radius, canvas_middle[1] + radius, fill='pink')

#setting ball movement 
xspeed = yspeed = 3

def moveBot():

    global xspeed, yspeed

    canvas.move(ball, xspeed, yspeed)

    (leftPos, topPos, rightPos, bottomPos) = canvas.coords(ball)

    if leftPos <= 0 or rightPos >= WIDTH:
        xspeed = -xspeed
    if topPos <= 0 or bottomPos >= HEIGHT:
        yspeed = -yspeed

    canvas.after(30, moveBot)

canvas.after(30, moveBot)
tk.mainloop()

from tkinter import *

canvas_width = 700
canvas_height = 600
width_brush =1

color = "Black"
x1=0
y1=0

master = Tk()
master.title( "Painting")
master.configure(bg="#dddddd")

def Menu_Help():
   top2 = Toplevel()
   top2.title("Help")
   Lb2 = Label(top2, text= "Draw what you want. Have Fun!")
   Lb2.pack()
   return

def Menu_License():
   top = Toplevel()
   top.title("Second Window")
   Lb = Label(top, text= "Software made with Python v3.11. \n Check Python license: https://docs.python.org/3/license.html \n Angelo Nicoli' 2023")
   Lb.pack()
   return

def Menu_Exit():
   master.quit()
   return

def Change_color(event):
   global color 
   color = "Green"

def Change_color2(event):
   global color 
   color = "Blue"

def Change_color3(event):
   global color 
   color = "Yellow"

def Change_color4(event):
   global color 
   color = "Red"

def Change_color5(event):
   global color 
   color = "Gray"

def Change_color6(event):
   global color 
   color = "LightSalmon"

def Change_color7(event):
   global color 
   color = "Violet"

def Change_color8(event):
   global color 
   color = "Purple"

def Change_color9(event):
   global color 
   color = "chocolate"

def Change_color10(event):
   global color 
   color = "RosyBrown"

def Change_color11(event):
   global color 
   color = "White"

def Change_color12(event):
   global color 
   color = "Black"   


def Change_color40(event):
   global color 
   color="Yellow"
   print("Yeppa")


def slide(event):
   global width_brush
   width_brush = horizontal.get()
  
def Del_Canvas():
   global w, canvas_width,canvas_height
   w.delete("all")


def paint( event ):
   global x1
   global y1
   global width_brush
   python_green = "#476042"
   #x1, y1 = ( event.x - 1 ), ( event.y - 1 )
   #x2, y2 = ( event.x + 1 ), ( event.y + 1 )
   #w.create_oval( x1, y1, x2, y2, fill = python_green )
   w.create_line( x1, y1, event.x, event.y, width = width_brush, fill = color)
   x1= event.x
   # y1= event.x PROVA PER FARE EFFETTI
   y1 = event.y



w = Canvas(master, width=canvas_width, height=canvas_height, bg="white")
w.grid(row=1, column=3, rowspan=6)
#w.bind( "<Button-1>", paint )
w.bind("<ButtonRelease-1>", paint)
w.bind("<B1-Motion>", paint)



Menu_01 = Button(text="Help", command = Menu_Help)
Menu_01.grid(row=0, column=0, columnspan=1, sticky=W+E)

Menu_02 = Button(text="License", command= Menu_License)
Menu_02.grid(row=0, column=2, columnspan=1, sticky=W)

Menu_03 = Button(text="Exit", command = Menu_Exit)
Menu_03.grid(row=0, column=1, columnspan=1, sticky=W+E)



Butn = Label(text="", bg="green", borderwidth=2)
Butn.grid(row=1, column=0,sticky=W+E, padx=5, ipadx=10)

Butn2 = Label(text="", bg="blue", borderwidth=2)
Butn2.grid(row=2, column=0,sticky=W+E, padx=5, ipadx=10)

Butn3 = Label(text="", bg="Yellow", borderwidth=2)
Butn3.grid(row=3, column=0,sticky=W+E, padx=5, ipadx=10)

Butn4 = Label(text="", bg="Red", borderwidth=2)
Butn4.grid(row=4, column=0,sticky=W+E, padx=5, ipadx=10)

Butn5 = Label(text="", bg="Gray", borderwidth=2)
Butn5.grid(row=5, column=0,sticky=W+E, padx=5, ipadx=10)

Butn6 = Label(text="", bg="LightSalmon", borderwidth=2)
Butn6.grid(row=1, column=1,sticky=W+E, padx=5, ipadx=10)

Butn7 = Label(text="", bg="Violet", borderwidth=2)
Butn7.grid(row=2, column=1,sticky=W+E, padx=5, ipadx=10)

Butn8 = Label(text="", bg="Purple", borderwidth=2)
Butn8.grid(row=3, column=1,sticky=W+E, padx=5, ipadx=10)

Butn9 = Label(text="", bg="chocolate", borderwidth=2)
Butn9.grid(row=4, column=1,sticky=W+E, padx=5, ipadx=10)

Butn10 = Label(text="", bg="RosyBrown", borderwidth=2)
Butn10.grid(row=5, column=1,sticky=W+E, padx=5, ipadx=10)

Butn11 = Label(text="", bg="White", borderwidth=2)
Butn11.grid(row=6, column=0, columnspan=1 ,sticky=W+E, padx=5, ipadx=10)

Butn12 = Label(text="", bg="Black", borderwidth=2)
Butn12.grid(row=6, column=1, columnspan=1 ,sticky=W+E, padx=5, ipadx=10)


Butn13 = Label(text="Brush Size", borderwidth=2)
Butn13.grid(row=8, column=0, columnspan=2 , padx=10,sticky=W+E)

horizontal  = Scale(master,from_=1, to=10, orient=HORIZONTAL, command=slide)
horizontal.grid(row=9,column=0, columnspan=2 , padx=10, sticky=W+E)

horizontal2  = Button(text = "Delete Canvas", command= Del_Canvas)
horizontal2.grid(row=9,column=3)


Butn.bind("<Button-1>", Change_color)
Butn2.bind("<Button-1>",Change_color2)
Butn3.bind("<Button-1>",Change_color3)
Butn4.bind("<Button-1>",Change_color4)
Butn5.bind("<Button-1>",Change_color5)

Butn6.bind("<Button-1>",Change_color6)
Butn7.bind("<Button-1>",Change_color7)
Butn8.bind("<Button-1>",Change_color8)
Butn9.bind("<Button-1>",Change_color9)
Butn10.bind("<Button-1>",Change_color10)

Butn11.bind("<Button-1>",Change_color11)
Butn12.bind("<Button-1>",Change_color12)

master.bind("<c>",Change_color40)




print(Butn2.cget("bg"))

mainloop()

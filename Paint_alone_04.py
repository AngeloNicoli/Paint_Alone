# Angelo Nicolì 2023-10-15

from Settings import *
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from Color_Frame import *
from PIL import ImageGrab
import random
import ctypes
import numpy as np
from PIL import Image,ImageTk


Grid_List=[]
Grid_ON = [False]
Texture_ON = [False]
Selected_Texture =["Texture/Tile_Wood_50px.png"]
print(Selected_Texture[0])

triangle_image = PhotoImage(file="images/Triangle.png")
triangle_resized = triangle_image.subsample(32, 32)

Brush_image = PhotoImage(file="images/Brush.png")
Brush_resized = Brush_image.subsample(32, 32)

Grid_image = PhotoImage(file="images/Brush.png")
Grid_resized = Brush_image.subsample(32, 32)

Texture_Image_01 = PhotoImage(file="Texture/Tile_Wood_50px.png")
Texture_Image_02 = PhotoImage(file="Texture/treasure_50px.png")
Texture_Image_03 = PhotoImage(file="Texture/tile_Castle_50px.png")


# Set zoom of Windows to 1 (Real Size Rendering)
ctypes.windll.shcore.SetProcessDpiAwareness(2)


def Receive_Color():

   #print(col)
   print("Eo")
   return(2)

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Create Menu bar

def Menu_Help():
   top2 = Toplevel()
   top2.title("Help")
   Lb2 = Label(top2, text= '''Draw what you want. Have Fun!. Manual is here.''')
   Lb2.pack()
   print("w")
   return

def Menu_License():
   top = Toplevel()
   top.title("Second Window")
   Lb = Label(top, text= "Software made with Python v3.11. \n Check Python license: https://docs.python.org/3/license.html \n Angelo Nicoli' 2023")
   Lb.pack()
   return

def new_file():
   Pages[canvas_page-1].delete("all")

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Create Menu bar
menubar = Menu(master)
master.config(menu=menubar)

# First Menu column
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="New (Free Draw)", command = new_file)
filemenu.add_command(label="New (Grid Draw)", command = new_file)
filemenu.add_command(label="New (Tech Draw)", command = new_file)

filemenu.add_separator()
filemenu.add_command(label="Load", command = new_file)
filemenu.add_separator()


filemenu.add_command(label="Exit", command=master.quit)

# Second Menu column
editmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)

editmenu.add_command(label="Resolution: 1024x768")
editmenu.add_command(label="Resolution:  800x600")

# Third Menu column
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)          

helpmenu.add_command(label="Help Index",command=Menu_Help)
helpmenu.add_command(label="License",command=Menu_License)

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Frame Creation

# Buttons, Mode
frame1 = Frame(master,bg="#3e3e42", width=1900, height=60, highlightbackground="black",highlightthickness=1)
# Left Window (Color Selection)
frame2 = Frame(master,bg="#252526", width=1400, height=50, highlightbackground="black",highlightthickness=1)
# Canvas Window 
frame3 = Frame(master,bg="#04252c", width=1400, height=900, highlightbackground="black",highlightthickness=1)
# Right Window
frame4 = Frame(master,bg="#252526", width= 1800, height=30, highlightbackground="black",highlightthickness=1)
# LOG Window
frame5 = Frame(master,bg="#3e3e42", width=90, height=30, highlightbackground="black",highlightthickness=1)
# Footer Window
frame6 = Frame(master,bg="#2d2d30", width=1900, height=30, highlightbackground="black",highlightthickness=1)
# Texture Window
frame7 = Frame(master,bg="#2d2d30", width=80, height=300, highlightbackground="black",highlightthickness=1)

frame1.grid(row=0,column=0, columnspan=3 , sticky="sewn")
frame2.grid(row=1,column=0,rowspan=2, sticky="sewn")
frame3.grid(row=1,column=1,sticky="sewn")
frame4.grid(row=1,column=2,rowspan=2,sticky="sewn")
frame5.grid(row=2,column=1,columnspan=1, sticky="sewn")
frame6.grid(row=3,column=0,columnspan=3, sticky="sewn")
frame7.grid(row=0,column=4,rowspan=4, sticky="sewn")

#frame7.grid_forget()
# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Size of Canvas
canvas_width = 1600
canvas_height = 1000
pixel_size = 50
n_pixel_x = canvas_width/pixel_size
n_pixel_y = canvas_height/pixel_size

#Create Matrix Savegame
pixel_color = [[0] * int(n_pixel_x) for j in range(int(n_pixel_y))]
texture_matrix = [[0] * int(n_pixel_x) for j in range(int(n_pixel_y))]

#(pixel_color[0][4])
#print(len(pixel_color))

# Set Mode value
width_brush =1
brush_Mode = 1
canvas_page = 1
Pages = [0,0]

x1 = 0
y1 = 0

def Save_Image():
   u = Pages[0].winfo_rootx()
   j = Pages[0].winfo_rooty()
   print(Pages[0].winfo_rootx())
   print(Pages[0].winfo_rooty())
   print(Pages[0].winfo_rooty())
   image = ImageGrab.grab(bbox =(u, j, u + canvas_width, j +canvas_height))
   file_path = filedialog.asksaveasfilename(defaultextension='.png')
   image.save(file_path)

def Change_color(event):
   global color_selected  
   color_list =["Green","Blue","Yellow","Red","Gray","LightSalmon","Violet","Purple", "chocolate","RosyBrown","White","Black"]
   print(color_selected)
   color_selected[0]  = color_list[event-1]

def Change_color40(event):
   global color_selected  
   color_selected ="Yellow"
   print("Yeppa")

def slide(event):
   global width_brush
   global pixel_size
   width_brush = Brush_Slider.get()
   pixel_size =  Pixel_Slider.get()
  
def Del_Canvas():
   global Pages, canvas_width,canvas_height
   Pages[canvas_page-1].delete("all")

def random_hex_color(event):
   global Random_Color_Select
   global color_selected  
   a = '#' 
   for el in range(6):
      a += random.choice('0123456789ABCDEF') 
      print(a)
   Random_Color_Select.configure(bg=a)
   color_selected[0]  = a 

def hex_color(event):
   HEX_R = hex(RGB_RED.get())[2:]
   HEX_B = hex(RGB_BLUE.get())[2:]
   HEX_G = hex(RGB_GREEN.get())[2:]
   if len(HEX_R) == 1:
      HEX_R = "0" + HEX_R
   if len(HEX_B) == 1:
      HEX_B = "0" + HEX_B
   if len(HEX_G) == 1:
      HEX_G = "0" + HEX_G

   Hex_RBG = "#" + str(HEX_R) + str(HEX_B) + str(HEX_G)
   Hex_Color_Text.configure(text= Hex_RBG)
   Hex_Button_Val.configure(bg= Hex_RBG)

def resize(event):
   Pages[0].configure(height=100, width=300)

def paint( event ):
   global x1
   global y1
   global width_brush
   global brush_Mode
   global pixel_size
   global canvas_page
   #print(color_selected[0])
   #x1, y1 = ( event.x - 1 ), ( event.y - 1 )
   #x2, y2 = ( event.x + 1 ), ( event.y + 1 )
   #w.create_oval( x1, y1, x2, y2, fill = "green" )

   if brush_Mode ==0:
      Pages[canvas_page-1].create_line( x1, y1, event.x, event.y, width = width_brush, fill = color_selected[0])
   if brush_Mode ==1 and Texture_ON[0] == False:
      cordx = (event.x//pixel_size) * pixel_size
      cordy = (event.y//pixel_size) * pixel_size
      #print(str(event.x//pixel_size) + " " + str(event.y//pixel_size))
      #print(str(cordx) + " " + str(cordy))
      Pages[canvas_page-1].create_rectangle(cordx, cordy, cordx + pixel_size +1, cordy + pixel_size + 1, width = 0,  fill = color_selected[0], tags="pixel")
      pixel_color[int(event.y//pixel_size)][int(event.x//pixel_size)] = color_selected[0]
   x1 = event.x
   # y1= event.x PROVA PER FARE EFFETTI
   y1 = event.y

   if Texture_ON[0]== True:
      cordx = (event.x//pixel_size) * pixel_size
      cordy = (event.y//pixel_size) * pixel_size
      Texture_Draw(cordx,cordy)
      #print("Texture")

   if Grid_ON[0] == True:
      Draw_Grid()

#def Mouse_position(event):
#   print(event.x,event.y)

def draw_pixel(row,column,color):
      #print(row,column,color)
      cordy = (row) * pixel_size
      cordx = (column) * pixel_size
      #print(str(row) + " " + str(column))
      if color == '0':
         color = "white"
      Pages[canvas_page-1].create_rectangle(cordx, cordy, cordx + pixel_size, cordy + pixel_size , width = 0, fill = color , tags="pixel")
      pixel_color[row][column] = color


def Pixel_Mode():
   global brush_Mode
   Pixel_Button.configure(text="Pixel Mode ON" , fg= "green")
   Brush_Button.configure(text="Brush Mode: ON", fg= "red")
   print("Pixel_Mode: ON")
   brush_Mode = 1
   return

def Brush_Mode():
   global brush_Mode
   Brush_Button.configure(text="Brush Mode: ON", fg= "green")
   Pixel_Button.configure(text="Pixel Mode OFF" , fg= "red")
   brush_Mode = 0
   return

def Draw_Grid():
   print("draw grid")
   Pages[0].delete("grid")
   Lines_Vertical = canvas_width/pixel_size
   Lines_Horizontal = canvas_height/pixel_size
   for i in range(int(Lines_Vertical)):
      Pages[canvas_page-1].create_line(i*pixel_size,0,i*pixel_size,canvas_height, tags="grid")
   print(Lines_Vertical)
   for i in range(int(Lines_Horizontal)):
      Pages[canvas_page-1].create_line(0,i*pixel_size,canvas_width,i*pixel_size, tags="grid")
   print(Lines_Horizontal)

def Texture_Draw(coordx,coordy):
   global Pages
   global img
   #print("Draw")
   img= ImageTk.PhotoImage(Image.open(str(Selected_Texture[0])))
   texture_matrix[coordy // pixel_size][coordx // pixel_size] = Selected_Texture[0]
   #print(texture_matrix)
   Texture_Grid()

def Texture_Grid():
   global Pages
   global img
   global img2
   for el in range(len(texture_matrix)):
      for els in range(len(texture_matrix[el])):
         #print(els)
         if texture_matrix[el][els] != 0:
            Pages[0].create_image(els*pixel_size,el*pixel_size,anchor=NW,image=img)
            img2= ImageTk.PhotoImage(Image.open("Texture/Tile_Wood_50px.png"))
            Pages[0].create_image(els*pixel_size,el*pixel_size+50,anchor=NW,image=img2)
            Pages[0].create_image(els*pixel_size,el*pixel_size+150,anchor=NW,image=img2)

def hex_color_selection(event):
   print(Hex_Color_Text["text"])
   color_selected[0] =  Hex_Color_Text['text']

def Grid_Mode():
   global Grid_Mode
   global Pages

   if Grid_ON[0] == False:
      Grid_ON[0] = True
      Grid_Mode.configure(text="Grid Mode ON" , fg="green")
      Draw_Grid()
   else:
      Grid_ON[0] = False    
      Grid_Mode.configure(text="Grid Mode OFF", fg="red")
      Pages[0].delete("grid")

def Texture_Mode():
   if Texture_ON[0] == False:
      Texture_ON[0] = True
      Texture_Mode.configure(text="Texture Mode: ON", fg="green")
   else:
      Texture_ON[0] = False   
      Texture_Mode.configure(text="Texture Mode: OFF", fg="red")

def Save_Grid():
   file_path = filedialog.asksaveasfilename(defaultextension='.txt')
   print(file_path)
   arr = np.array(pixel_color)
   #np.savetxt("Map.txt", arr, delimiter=',', fmt='%s')
   np.savetxt(file_path, arr, delimiter=',', fmt='%s')

def Load_Grid():
   file_path = filedialog.askopenfilenames()
   print(file_path)
   print(file_path[0])
   x = np.loadtxt(file_path[0], dtype="U", delimiter=",", quotechar='"')
   #print(x)
   #print(x[3])
   #print(x[3][2])
   print(len(x))
   for row in range(len(x)):
      print(row)
      print(x[row])
      for column in range(len(x[row])):
         print("Rows is " + str(row) + "Column is: " + str(column) + "color is: " + str(x[row][column]))
         draw_pixel(row,column,x[row][column])

def next_page():
   global canvas_page
   global Butn17
   canvas_page +=1
   print(canvas_page)
   Pages[1].grid(row=1, column=3, rowspan=6)
   Pages[0].grid_remove()
   Butn17.configure(text="Page" + str(canvas_page))

def previous_page():
   global canvas_page
   global Butn17
   canvas_page -=1
   print(canvas_page)
   Pages[0].grid(row=1, column=3, rowspan=6)
   Pages[1].grid_remove()
   Butn17.configure(text="Page" + str(canvas_page))

def Texture_Select(path_Texture):
   print("Press") 
   Selected_Texture[0] = path_Texture
   print(Selected_Texture[0])
   
def Pixel_Format():
   messagebox.showinfo("Information", "Pass to Grid Mode?")
   Draw_Grid()

Pages[1] = Canvas(frame3, width=canvas_width/2, height=canvas_height/2, bg="gray")
Pages[1].grid(row=0, column=0, rowspan=6)

Pages[0] = Canvas(frame3, width=canvas_width/2, height=canvas_height/2, bg="white")
Pages[0].grid(row=0, column=0, rowspan=6)

img= ImageTk.PhotoImage(Image.open("Tile_Wood_50px.png"))

# Comandiamo la posizione deel mouse
#w.bind( "<Button-1>", paint )

Pages[0].bind("<ButtonRelease-1>", paint)
Pages[0].bind("<B1-Motion>", paint)
#w.bind("<B1-Motion>", Mouse_position)

Pages[1].bind("<ButtonRelease-1>", paint)
Pages[1].bind("<B1-Motion>", paint)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

FreeDraw = Label(frame1,text = "Free Draw", font= 25, fg = "Black", bg="white")
Pixel_Button  = Button(frame1,text = "Pixel Mode ON", command= Pixel_Mode, font= 25, fg = "Green", compound = LEFT)
Brush_Button  = Button(frame1,text = "Brush Mode OFF", command= Brush_Mode, font= 25, fg = "red", image = Brush_resized, compound = LEFT)

GridDraw = Label(frame1,text = "Draw Pixel Grid",font= 25, fg = "Black", bg="gray")
Pixel_Grid = Button(frame1,text = "Pixel Grid", command= Pixel_Format, font= 25, fg = "red")
Grid_Mode  = Button(frame1,text = "Grid Mode OFF", command= Grid_Mode, font= 25, fg = "red")
Save_Image  = Button(frame1,text = "Save Image (png)", command= Save_Image, font= 25, fg = "blue")
Texture_Mode  = Button(frame1,text = "Texture Mode OFF", command= Texture_Mode, font= 25, fg = "red")

TechDraw = Label(frame1,text = "Technical Draw",font= 25, fg = "Black", bg="gray")

FreeDraw.grid(row=0,column=0, columnspan=2, sticky= W+E,padx=10, pady= 5)
TechDraw.grid(row=0,column=4, columnspan=2, sticky= W+E,padx=10, pady= 5)

Pixel_Button.grid(row=1,column=0,padx=10, pady= 5)
Brush_Button.grid(row=1,column=1,padx=10)
Pixel_Grid.grid(row=1,column=2,padx=10)

GridDraw.grid(row=0,column=2, columnspan=2, sticky= W+E,padx=10, pady= 5)
Grid_Mode.grid(row=1,column=4,padx=10)
Save_Image.grid(row=1,column=5,padx=10)
Texture_Mode.grid(row=1,column=3,padx=10)

# Cambiare ordine grid
def Del_Frame():
   frame2.destroy()
   frame3.destroy()
   frame4.destroy()
   frame5.destroy()
   frame6.destroy()
   frame7.destroy()
   frame3 = Frame(master,bg="#3e3e42", width=800, height=30, highlightbackground="black",highlightthickness=1)
   frame3.grid(row=2,column=1,columnspan=1, sticky="ew")

Delete_Btn  = Button(frame1,text = "Delete", command= Del_Frame, font= 25, fg = "red")
Delete_Btn.grid(row=1,column=10,padx=10)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Palette_Selector= Label(frame2,text="Palette Selector", bg="White", borderwidth=1,relief="solid")
Green_Color = Label(frame2,text="", bg="Green", borderwidth=1,relief="solid")
Blue_Color = Label(frame2,text="", bg="blue", borderwidth=1,relief="solid")
Yellow_Color = Label(frame2,text="", bg="Yellow", borderwidth=1,relief="solid")
Red_Color = Label(frame2,text="", bg="Red", borderwidth=1,relief="solid")
Gray_Color = Label(frame2,text="", bg="Gray", borderwidth=1,relief="solid")
White_Color = Label(frame2,text="", bg="White", borderwidth=1,relief="solid")

Salmon_Color = Label(frame2,text="", bg="LightSalmon", borderwidth=1,relief="solid")
Violet_Color = Label(frame2,text="", bg="Violet", borderwidth=1,relief="solid")
Purple_Color = Label(frame2,text="", bg="Purple", borderwidth=1,relief="solid")
Chocolate_Color = Label(frame2,text="", bg="Chocolate", borderwidth=1,relief="solid")
RosyBrown_Color = Label(frame2,text="", bg="RosyBrown", borderwidth=1,relief="solid")
Black_Color = Label(frame2,text="", bg="Black", borderwidth=1,relief="solid")

Random_Color = Label(frame2,text="Random Color")
Random_Color_Select = Label(frame2,text="", bg="White", borderwidth=1,relief="solid")
Brush_Size = Label(frame2,text="Brush Size", borderwidth=1,relief="solid")
Brush_Slider  = Scale(frame2,from_=1, to=10, orient=HORIZONTAL, command=slide, state=NORMAL, fg="red")

Pixel_Size = Label(frame2,text="Pixel Size", borderwidth=1,relief="solid")
Pixel_Slider  = Scale(frame2,from_=1, to=50, orient=HORIZONTAL, command=slide)
Pixel_Slider.set(pixel_size)

More_Color = Button(frame2,text="More Colors", command=lambda: Color_Selection(3,master))
RGB_RED = Scale(frame2,from_=0, to=255, orient=HORIZONTAL, command=hex_color)
RGB_BLUE = Scale(frame2,from_=0, to=255, orient=HORIZONTAL, command=hex_color)
RGB_GREEN = Scale(frame2,from_=0, to=255, orient=HORIZONTAL, command=hex_color)

Hex_Color_Text = Label(frame2,text="Color", borderwidth=1,relief="solid")
Hex_Color_Text["text"] = "#000000"

Hex_Button_Val = Label(frame2,text="", bg="chocolate", borderwidth=1,relief="solid")
Hex_Button_Val.configure(bg= "#000000")

Palette_Selector.grid(row=0, column=0, columnspan=2 ,sticky=W+E, padx=5, ipadx=10)
Green_Color.grid(row=1, column=0,sticky=W+E, padx=5, ipadx=10)
Blue_Color.grid(row=2, column=0,sticky=W+E, padx=5, ipadx=10)
Yellow_Color.grid(row=3, column=0,sticky=W+E, padx=5, ipadx=10)
Red_Color.grid(row=4, column=0,sticky=W+E, padx=5, ipadx=10)
Gray_Color.grid(row=5, column=0,sticky=W+E, padx=5, ipadx=10)
Salmon_Color.grid(row=1, column=1,sticky=W+E, padx=5, ipadx=10)
Violet_Color.grid(row=2, column=1,sticky=W+E, padx=5, ipadx=10)
Purple_Color.grid(row=3, column=1,sticky=W+E, padx=5, ipadx=10)
Chocolate_Color.grid(row=4, column=1,sticky=W+E, padx=5, ipadx=10)
RosyBrown_Color.grid(row=5, column=1,sticky=W+E, padx=5, ipadx=10)
White_Color.grid(row=6, column=0, columnspan=1 ,sticky=W+E, padx=5, ipadx=10)
Black_Color.grid(row=6, column=1, columnspan=1 ,sticky=W+E, padx=5, ipadx=10)

Random_Color.grid(row=7, column=0, columnspan=2 ,sticky=W+E, padx=5, pady = 5, ipadx=10)
Random_Color_Select.grid(row=8, column=0, columnspan=2 ,sticky=W+E, padx=5, pady = 5, ipadx=10)

Brush_Size.grid(row=9, column=0, columnspan=2 , padx=10,sticky=W+E)
Brush_Slider.grid(row=10,column=0, columnspan=2 , padx=10, sticky=W+E)
Brush_Slider.grid(row=11,column=0, columnspan=2 , padx=10, sticky=W+E)
Pixel_Size.grid(row=12, column=0, columnspan=2 , padx=10,sticky=W+E)
Pixel_Slider.grid(row=13,column=0, columnspan=2 , padx=10, sticky=W+E)

More_Color.grid(row=14, column=0, columnspan=2 , pady=10,sticky=W+E)

RGB_RED.grid(row=15, column=0, columnspan=2 , padx=10,sticky=W+E)
RGB_BLUE.grid(row=16, column=0, columnspan=2 , padx=10,sticky=W+E)
RGB_GREEN.grid(row=17, column=0, columnspan=2 , padx=10,sticky=W+E)
Hex_Color_Text.grid(row=18, column=0, columnspan=2 , padx=10,sticky=W+E)
Hex_Button_Val.grid(row=19, column=0,columnspan=2 ,sticky=W+E, padx=5, pady = 5, ipadx=10)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Butn160 = Button(frame4,text="Next Page", bg="white", command=next_page)
Butn16 = Button(frame4,text="Previous Page", bg="white", command = previous_page)
Butn17 = Label(frame4,text="Page:" + str(canvas_page), borderwidth=1,relief="solid")
Del_Button = Button(frame4,text = "Delete Canvas", command= Del_Canvas)
Save_File = Button(frame4,text = "Save Pixel", command=Save_Grid)
Load_File = Button(frame4,text = "Load Pixel", command=Load_Grid)

logText = Label(frame5,text="LOG: ")

Butn18 = Label(frame6,text="Angelo Nicoli (2023) - Made with Python 3.11",bg="#2d2d30",fg="white")

Texture_01 = Button(frame7,text = "", image = Texture_Image_01,command=  lambda:Texture_Select("Texture/Tile_Wood_50px.png"), compound = LEFT)
Texture_01.grid(row=0, column=0, padx = 5, pady=5)

Texture_02 = Button(frame7,text = "", image = Texture_Image_02,command=  lambda: Texture_Select("Texture/treasure_50px.png"), compound = LEFT)
Texture_02.grid(row=1, column=0, padx = 5, pady=5)

Texture_03 = Button(frame7,text = "", image = Texture_Image_03, command=  lambda: Texture_Select("Texture/tile_Castle_50px.png"), compound = LEFT)
Texture_03.grid(row=2, column=0, padx = 5, pady=5)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Butn17.grid(row=2, column=0)
Del_Button.grid(row=3,column=0,pady=100)
Save_File.grid(row=4,column=0,pady=10)
Load_File.grid(row=5,column=0,pady=10)
Butn18.pack(anchor=E)

Butn16.grid(row=0, column=0, rowspan=1,padx=10, pady=30, ipadx=10)
Butn160.grid(row=1, column=0, rowspan=1,padx=10, pady=10)

logText.grid(row=1, column=0, rowspan=1,padx=10, pady=10)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def GestoreEventi():
   Green_Color.bind('<Button-1>', lambda event: Change_color(1))
   Blue_Color.bind('<Button-1>', lambda event: Change_color(2))
   Yellow_Color.bind("<Button-1>", lambda event: Change_color(3))
   Red_Color.bind("<Button-1>",lambda event: Change_color(4))
   Gray_Color.bind("<Button-1>",lambda event: Change_color(5))
   Salmon_Color.bind("<Button-1>",lambda event: Change_color(6))
   Violet_Color.bind("<Button-1>",lambda event: Change_color(7))
   Purple_Color.bind("<Button-1>",lambda event: Change_color(8))
   Chocolate_Color.bind("<Button-1>",lambda event: Change_color(9))
   RosyBrown_Color.bind("<Button-1>",lambda event: Change_color(10))
   White_Color.bind("<Button-1>",lambda event: Change_color(11))
   Black_Color.bind("<Button-1>",lambda event: Change_color(12))
   Random_Color_Select.bind("<Button-1>",random_hex_color)
   Hex_Button_Val.bind("<Button-1>",hex_color_selection)

GestoreEventi()
master.bind("<c>",Change_color40)

#print(Butn2.cget("bg"))

master.mainloop()

from tkinter import *
from Settings import *

Color_Palette = [None] * 11
Color_Palette[0] =["MediumVioletRed","DeepPink","PaleVioletRed","HotPink","LightPink","Pink"]
Color_Palette[1] =["DarkRed","Red","Firebrick","Crimson","IndianRed","LightCoral","Salmon","DarkSalmon","LightSalmon"]
Color_Palette[2] =["OrangeRed","Tomato","DarkOrange","Coral","Orange"]
Color_Palette[3] =["DarkKhaki","Gold","Khaki","PeachPuff","Yellow","PaleGoldenrod","Moccasin","PapayaWhip","LightGoldenrodYellow","LemonChiffon","LightYellow"]
Color_Palette[4] =["Maroon","Brown","SaddleBrown","Sienna","Chocolate","DarkGoldenrod","Peru","RosyBrown","Goldenrod","Goldenrod","SandyBrown",
                   "Tan","Burlywood","Wheat","NavajoWhite","Bisque","BlanchedAlmond","Cornsilk"]
Color_Palette[5] =["Indigo","Purple","DarkMagenta","DarkViolet","DarkSlateBlue","BlueViolet","DarkOrchid","Fuchsia","Magenta","SlateBlue","MediumSlateBlue",
                   "MediumOrchid","MediumPurple","Orchid","Violet","Plum","Thistle","Lavender"]
Color_Palette[6] = ["DarkGreen","Green","DarkOliveGreen","ForestGreen","SeaGreen","Olive","OliveDrab","MediumSeaGreen","LimeGreen","Lime","SpringGreen",
                   "MediumSpringGreen","DarkSeaGreen","MediumAquamarine","YellowGreen","LawnGreen","Chartreuse","LightGreen","GreenYellow","PaleGreen"]
Color_Palette[7] = ["MidnightBlue","Navy","DarkBlue","MediumBlue","Blue","RoyalBlue","SteelBlue","DodgerBlue","DeepSkyBlue","CornflowerBlue","SkyBlue",
                   "LightSkyBlue","LightSteelBlue","LightBlue","PowderBlue"]
Color_Palette[8] = ["MistyRose","AntiqueWhite","Linen","Beige","WhiteSmoke","LavenderBlush","OldLace","AliceBlue","Seashell","GhostWhite","Honeydew",
                   "FloralWhite","Azure","MintCream","Snow","Ivory","White"]
Color_Palette[9] = ["Teal","DarkCyan","LightSeaGreen","CadetBlue","DarkTurquoise","MediumTurquoise","Turquoise","Aqua","Cyan","Aquamarine","PaleTurquoise", "LightCyan"]
Color_Palette[10] = ["Black","DarkSlateGray","DimGray","SlateGray","Gray","LightSlateGray","DarkGray","Silver", "LightGray","Gainsboro"]


#print(Color_Palette)
#print(len(Color_Palette))
#print(len(Color_Palette[0]))
#print(len(Color_Palette[1]))

def Close_color():
    global color_selected
    color_selected[0] = ["Yellow"]
    #print(type(color_selected))
    #print(color_selected[0])
    print("eri")



# Create first time 
top = Toplevel()
top.title("My second Window")
top.configure(bg="#3e3e42")
#print(color_selected)
for i in range(len(Color_Palette)):
    for j in range(len(Color_Palette[i])):
        #print(Color_Palette[i][j])
        Butn = Label(top,text="", bg= Color_Palette[i][j], borderwidth=0.5,relief="solid")
        Butn.grid(row=j, column=i,sticky=W+E, padx=5, ipadx=10)
        Butn299 = Button(top,text="Print", borderwidth=0.5,relief="solid", command=Close_color)
        Butn299.grid(row=15, column=12,sticky=W+E, padx=5, ipadx=10)    
top.withdraw()


def Color_Selection(colors,master):
    global color_selected
    global top 
    top = Toplevel()
    top.title("My second Window")
    top.configure(bg="#3e3e42")
    color_selected[0]= "RED"
    #print(color_selected)
    for i in range(len(Color_Palette)):
        for j in range(len(Color_Palette[i])):
           #print(Color_Palette[i][j])
            Butn20 = Label(top,text="", bg= Color_Palette[i][j], borderwidth=0.5,relief="solid")
            Butn20.grid(row=j, column=i,sticky=W+E, padx=5, ipadx=10)
            Butn299 = Button(top,text="dddwwwwwwwd", borderwidth=0.5,relief="solid", command=Close_color)
            Butn299.grid(row=15, column=12,sticky=W+E, padx=5, ipadx=10)    
    #print(color_selected)
    color_selected[0]  = "Blue"
    #print(color_selected)
    top.deiconify()
    
def Color_Choose():
    #print(34)
    pass


top.bind("<B1-Motion>", Color_Choose)



  


from tkinter import *

#-----------------------------function----------------------------
def increase():
    a= int(shamila1["text"]) #shamila1["text"] = "0"
    shamila1["text"] = f"{a+1}"

def decrease():
    a= int(shamila1["text"])
    shamila1["text"] = f"{a-1}"
    
#------------------------------Screen----------------------------  
#create a window or screen
#create a Tk class object name "app"
app = Tk() 
app.title("firstapp")
app.geometry("200x100")

#-----------------------Button & Label-----------------------------
#create a object shamila for "-" Button
shamila = Button(app, text = "-", height= 2, width= 5, command = decrease )
shamila.grid(row = 0,column = 0)

#create a object shamila1 for Label
shamila1 = Label(app, text = "0", fg = "red")
shamila1.grid(row = 0, column = 1)

#create a object shamila2 for "+" Button
shamila2 = Button(app, text = "+", height= 2, width= 5, command = increase)
shamila2.grid(row=0, column= 2)

app.mainloop() #object.method()



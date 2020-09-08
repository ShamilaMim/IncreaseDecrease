from tkinter import *
def increase():
    a= int(shamila1["text"]) #shamila1["text"] = "0"
    shamila1["text"] = f"{a+1}"

def decrease():
    a= int(shamila1["text"])
    shamila1["text"] = f"{a-1}"

    


    



    
app = Tk()
app.title("firstapp")
app.geometry("200x100")

shamila = Button(app, text = "-", height= 2, width= 5, command = decrease )
shamila.grid(row = 0,column = 0)

shamila1 = Label(app, text = "0", fg = "red")
shamila1.grid(row = 0, column = 1)

shamila2 = Button(app, text = "+", height= 2, width= 5, command = increase)
shamila2.grid(row=0, column= 2)















app.mainloop() #object.method()



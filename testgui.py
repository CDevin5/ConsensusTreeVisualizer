from Tkinter import *
import Image, ImageTk

def sel():
   selection = "Value = " + str(var.get())
   print selection
   label.config(text = selection)

root = Tk()
var = DoubleVar()
scale = Scale( root, from_=51, to = 100, variable = var, orient=HORIZONTAL)
scale.pack(anchor=CENTER)

label = Label(root)
label.config(text = "Press Instructions for additional help")

label.pack(side = "bottom", fill = "both", expand = "yes")

def stopProg(e):
    """ exits program """
    root.destroy()
    
button1=Button(root,text="Exit", fg = "red")
button1.pack(fill = X)
button1.bind('<Button-1>',stopProg)

def transfertext(e):
    """ print's instructions for user"""
    label.configure(text="Use the scale bar to navigate between consensus trees")
    
button2=Button(root,text="Instructions")
button2.pack(fill = X)
button2.bind('<Button-1>',transfertext)

def callback(e):
    """ Uses exceptions to change the image"""
    addon = str(int(var.get())) 
    if addon != "100":
        addon = '0' + addon
    path = "C:\Users\Sophia\Dropbox\\5C_Hackathon\ConsensusTreeVisualizer\images\TestTree-" + addon + ".png"
    img2 = ImageTk.PhotoImage(Image.open(path))
    label.configure(image = img2)
    label.image = img
  
root.bind("<B1-Motion>", callback)
root.mainloop()




### ConsensusTreeVisualizer, a Claremont Colleges Hackathon project.
### Dates: 15-16 November 2013
### Authors: Coline Devin, Benjamin Johnson, Rachel Sherman, Sophia Williams
### School: Harvey Mudd College

### GUI.py
### Author: Benjamin Johnson, Sophia Williams
### Creates a window with controls for viewing trees

from Tkinter import *
import Image, ImageTk

IMAGE_DIR = 'C:\Users\Sophia\Dropbox\\5C_Hackathon\ConsensusTreeVisualizer\images'

## main loop

def main():
   """ """
   root = Tk()
   var = DoubleVar()

   scale = Scale( root, from_=51, to = 100, variable = var, orient=HORIZONTAL)
   scale.pack(anchor=CENTER)

   label = Label(root)
   label.config(text = "Press Instructions for additional help")

   label.pack(side = "bottom", fill = "both", expand = "yes")

   button1=Button(root,text="Exit", fg = "red")
   button1.pack(fill = X)
   button1.bind('<Button-1>',lambda e: stopProg(e, root))

   button2=Button(root,text="Instructions")
   button2.pack(fill = X)
   button2.bind('<Button-1>',lambda e: transfertext(e, label))

   root.bind("<B1-Motion>", lambda e: callback(e, var, label))
   root.mainloop()

## Support functions

##def sel():
##   selection = "Value = " + str(var.get())
##   print selection
##   label.config(text = selection)

def stopProg(e, root):
    """ exits program """
    root.destroy()

def transfertext(e, label):
    """ print's instructions for user"""
    label.configure(text="Use the scale bar to navigate between consensus trees")
    
def callback(e, var, label):
    """ Uses exceptions to change the image"""
    addon = str(int(var.get())) 
    if addon != "100":
        addon = '0' + addon
    path = IMAGE_DIR + "/TestTree-" + addon + ".png"
    img2 = ImageTk.PhotoImage(Image.open(path))
    label.configure(image = img2)
    label.image = img

if __name__ == "__main__":
    main()
  





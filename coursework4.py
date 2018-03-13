import tkinter as tk
from tkinter.filedialog import askopenfilename

root = tk.Tk()
wtitle = root.title("Threshold")
winWidth = 1200
winHeight = 600
root.geometry("%dx%d+0+0" % (winWidth, winHeight))
w = 400
h = 600

class App:
    
    "Defining Menu"
    def menuFunction():     
       "Initializing menu" 
       menubar=tk.Menu(root)
       "Initializing drop-down menu elements" 
       filemenu=tk.Menu(menubar,tearoff=0)
       filemenu.add_command(label="Open Image", command=openFile())
       filemenu.add_command(label="Save Image")
       filemenu.add_command(label="Exit",command=root.destroy)
       "Initializing File button" 
       menubar.add_cascade(label="File",menu=filemenu)
       root.config(menu=menubar)

    def frameLeft():       
        left_frame = tk.Frame(root, width = w, height = h, bg = 'yellow')    
        left_frame.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)    

    def frameRight():
        right_frame = tk.Frame(root, width = w, height = h, bg = 'red')
        right_frame.pack(side = tk.RIGHT, expand = True, fill = tk.BOTH)

    def openFile():
        filename = askopenfilename()
        return filename       

App.menuFunction()
App.frameLeft()
App.frameRight()
root.pack_propagate(0)
root.mainloop()

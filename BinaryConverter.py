from tkinter import Frame,Canvas, Button, Label, Menu #include more tkinter widgets here
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
import os


from GreyScaleImage import GreyScaleImage
from ColourImage import ColourImage



## GUI for binary image creator
class BinaryConverter(Frame):
    
    CANVAS_SIZE = 500  # Square Region size used to display images
   
    def __init__(self, master=None):

        Frame.__init__(self, master)

        self.canvasLeft = Canvas(width=500, height=500, bg="white")
        self.canvasLeft.grid(column=1, row=3)

        self.canvasRight = Canvas(width=500, height=500, bg="white")
        self.canvasRight.grid(column=2, row=3)
        
        self.grid()  # use the grid manager

        self.master.title("Binary Image Creator")

        menubar = Menu(self)
        fileMenu = Menu(self)

        menubar.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_cascade(label="Open", command=self._loadFile)


        self.filePath = Label(self.master)
        self.filePath.grid(column=1, row=2)
                
        self._imagedata = None     # Store here the loaded Image Data, i.e. an object of class GreyScaleImage or ColourImage. 
		                           # This will not change until a new data file is loaded. 
        self._processedData = None # Store here a BinaryImage object that is the result of binarising the loaded data.
        self._pixelSize = 2        # This is used to size the pixels in our display. See method _display()

        vals = GreyScaleImage()._openGreyScaleImage("GreyImage.txt")
        self._display(self.canvasLeft, vals)
        self.master.configure(menu=menubar)

    def _display(self, canvas, inputPts): 
          s = self._pixelSize # renaming so that the last line of this method is shorter and easier to read
          for pt in inputPts:
              [x,y,v]=pt    # x and y are both integers.
                            # v is a string, which comes from the output of _determineColorValue
              canvas.create_rectangle(s*x, s*y, s*(x+1), s*(y+1), fill=v, width=0)

    def _loadFile(self):
        filename = askopenfilename()

        self.filePath = Label(self.master, text=self._pathOfFile(filename))
        
        return filename
        

    def _pathOfFile(self, filename):

        if filename is None:
            return None
        else:
            pathOfFile = os.path.realpath(filename)

        return pathOfFile
        

        
        

  
if __name__ == "__main__":
    BinaryConverter().mainloop()

from tkinter import *
from tkinter import Frame,Canvas  #include more tkinter widgets here



from GreyScaleImage import GreyScaleImage
from ColourImage import ColourImage


## GUI for binary image creator
class BinaryConverter(Frame):

    
    CANVAS_SIZE = 500  # Square Region size used to display images
   
    def __init__(self, master=None):
        self.master = Tk("450x450")
        self.master.title("Binary Image Creator")
        canvasLeft = Canvas(self.master,bg="white")
        canvasLeft.pack(side="left", expand=True, fill="both")
        
        canvasRight = Canvas(self.master,bg="white")
        canvasRight.pack(side="right", expand=True, fill="both")
        
        
        Frame.__init__(self, master)
            
        """vals = GreyScaleImage()._openGreyScaleImage("GreyImage.txt")
        self._display(canvasRight, vals)"""
        
        self.grid()  # use the grid manager

        

        

        self._imagedata = None     # Store here the loaded Image Data, i.e. an object of class GreyScaleImage or ColourImage. 
		                           # This will not change until a new data file is loaded. 
        self._processedData = None # Store here a BinaryImage object that is the result of binarising the loaded data.
        self._pixelSize = 2        # This is used to size the pixels in our display. See method _display()

        

    def _display(self, canvas, inputPts): 
          s = self._pixelSize # renaming so that the last line of this method is shorter and easier to read
          for pt in inputPts:
              [x,y,v]=pt    # x and y are both integers.
                            # v is a string, which comes from the output of _determineColorValue
              canvas.create_rectangle(s*x, s*y, s*(x+1), s*(y+1), fill=v, width=0)

 
  
if __name__ == "__main__":

    BinaryConverter().mainloop()

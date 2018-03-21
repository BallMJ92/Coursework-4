from tkinter import Frame,Canvas, Button, Label, Menu, Entry #include more tkinter widgets here
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
from GreyScaleImage import GreyScaleImage
from ColourImage import ColourImage
import os

## GUI for binary image creator
class BinaryConverter(Frame):
    
    CANVAS_SIZE = 500  # Square Region size used to display images
   
    def __init__(self, master=None):

        Frame.__init__(self, master)

        # Creating left canvas
        self.canvasLeft = Canvas(width=500, height=500, bg="white")
        # Aligning left canvas
        self.canvasLeft.grid(column=1, row=3)

        # Creating right canvas
        self.canvasRight = Canvas(width=500, height=500, bg="white")
        # Aligning right canvas
        self.canvasRight.grid(column=2, row=3)
        
        self.grid()  # use the grid manager

        self.master.title("Binary Image Creator")

        # Creating menu bar for opening and saving files
        menubar = Menu(self)
        fileMenu = Menu(self)

        # Initiating cascade feature on menubar
        menubar.add_cascade(label="File", menu=fileMenu)
        # Adding filemenu button to open file with linked with command
        fileMenu.add_cascade(label="Open", command=self._openFile)
        # Adding filemenu button to save file with linked with command
        fileMenu.add_cascade(label="Save", command=self._saveFile)

        # Initiating label to hold the file path of selected image file
        self.filePath = Label(self.master, text=None)
        # Aligning label to be above left canvas
        self.filePath.grid(column=1, row=2)

        # Initiating label to display text relating to threshold
        self.thresholdLabel = Label(self.master, text="Select Threshold (0-255)")
        # Aligning label to be above left canvas
        self.thresholdLabel.grid(column=2, row=2, sticky="w", padx=70)

        # Creating text entry box in same column as threshold label
        self.thresholdEntry = Entry(self.master, width=4)
        # Aligning text entry box next to label
        self.thresholdEntry.grid(column=2, row=2, sticky="e", padx=180)

        # Creating threshold calculate button next to text entry box
        self.thresholdCalculate = Button(self.master, width=6, text="Process")
        # Aligning button and specifying position next to entry box
        self.thresholdCalculate.grid(column=2, row=2, sticky="e", padx=125)
        
                
        self._imagedata = None     # Store here the loaded Image Data, i.e. an object of class GreyScaleImage or ColourImage. 
		                           # This will not change until a new data file is loaded. 
        self._processedData = None # Store here a BinaryImage object that is the result of binarising the loaded data.
        self._pixelSize = 2        # This is used to size the pixels in our display. See method _display()

        """self.vals = GreyScaleImage()._openGreyScaleImage("GreyImage.txt")
        self._display(self.canvasLeft, vals)"""
        self.master.configure(menu=menubar)

    def _display(self, canvas, inputPts): 
          s = self._pixelSize # renaming so that the last line of this method is shorter and easier to read
          for pt in inputPts:
              [x,y,v]=pt    # x and y are both integers.
                            # v is a string, which comes from the output of _determineColorValue
              canvas.create_rectangle(s*x, s*y, s*(x+1), s*(y+1), fill=v, width=0)

    def _openFile(self):
        # Open the file dialog to select an image file
        self.file_chosen = askopenfilename()
        "print(self.file_chosen[-4:])"
        
        # Statement to run once open file dialog has finished
        if self.file_chosen[-4:] == ".txt":
            # Updating label to display file location
            self.filePath.config(text=self.file_chosen)
            try:
                with open(self.file_chosen, "r") as file:
                    fline = file.readline()
                    # Testing if first line is either Greyscale or colour image
                    if fline.strip() == "Greyscale Image":
                        # Clearing canvas before displaying image
                        self.canvasLeft.delete("all")
                        # Accessing and passing file location to _openGreyScaleImage 
                        self.vals = GreyScaleImage()._openGreyScaleImage(self.file_chosen)
                        # Passing Binary and X/Y coordinated to display function
                        self._display(self.canvasLeft, self.vals)
                    elif fline.strip() == "Colour Image":
                        self.canvasLeft.delete("all")
                        self.vals = ColourImage()._openColorImage(self.file_chosen)
                        self._display(self.canvasLeft, self.vals)
            except Exception:
                # Updating text on label if file cannot be read
                self.filePath.config(text="Incorrect filetype was selected. Please select txt image.")
        else:
            self.filePath.config(text="Incorrect filetype was selected. Please select txt image.")


    def _saveFile(self):
        print("Working")
  
if __name__ == "__main__":
    BinaryConverter().mainloop()

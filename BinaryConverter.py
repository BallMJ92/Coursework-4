from tkinter import Frame,Canvas, Button, Label, Menu, Entry #include more tkinter widgets here
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
from GreyScaleImage import GreyScaleImage
from ColourImage import ColourImage

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
        fileMenu.add_cascade(label="Open", command=self.openFile)
        # Adding filemenu button to save file with linked with command
        fileMenu.add_cascade(label="Save", command=self.saveFile)
        # Adding filemenu button to close application
        fileMenu.add_cascade(label="Close", command=self.closeApplication)

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
        # Automatically selecting threshold and placing in text entry box
        self.thresholdEntry.insert(0, "0")
        # Aligning text entry box next to label
        self.thresholdEntry.grid(column=2, row=2, sticky="e", padx=180)

        # Creating threshold calculate button next to text entry box
        self.thresholdCalculate = Button(self.master, command = self.processThreshold, width=6, text="Process")
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

    def openFile(self):
        # Open the file dialog to select an image file
        self.file_chosen = askopenfilename()
        "print(self.file_chosen[-4:])"
        self.inVals = []
        self.typeOfImage = ""
        self.threshold = []
        
        
        # Statement to run once open file dialog has finished
        if self.file_chosen[-4:] == ".txt":
            try:
                with open(self.file_chosen) as input_file:
                    fline = input_file.readline()
                    self.typeOfImage = fline.strip()
                    for line in input_file:
                        self.inVals.append(line.split())
                input_file.close()
            except Exception:
                self.filePath.config(text="Unknown file type was selected. Please select txt image.")

        print(self.inVals[0:50])
        
        if self.typeOfImage == "Greyscale Image":            
            # Updating label to display file location
            self.filePath.config(text=self.file_chosen)
            # Testing if first line is either Greyscale or colour image
            # Clearing canvas before displaying image
            self.canvasLeft.delete("all")
            # Accessing and passing file location to _openGreyScaleImage 
            self.vals = GreyScaleImage().dataForDisplay(self.inVals)
            # Passing Binary and X/Y coordinated to display function
            self._display(self.canvasLeft, self.vals)
            for i in self.inVals:
                for index in range(2, len(i), 3):
                    self.threshold.append(i[index])
            self.threshold = list(map(int, self.threshold))
            print("----------")
            print(self.threshold[0:50])
            print("---------")
            print(sum(self.threshold))
            self.greyThreshold = GreyScaleImage().getThreshold(self.threshold)
            # Clearing the threshold entry box
            self.thresholdEntry.delete(0, 'end')
            # Inserting the system selected threshold into entry box
            self.thresholdEntry.insert(0, str(self.greyThreshold))
        elif self.typeOfImage == "Colour Image":  


            
            # Updating label to display file location
            self.filePath.config(text=self.file_chosen)
            # Testing if first line is either Greyscale or colour image
            # Clearing canvas before displaying image
            self.canvasLeft.delete("all")
            # Accessing and passing file location to _openGreyScaleImage 
            self.vals = ColourImage().dataForDisplay(self.inVals)
            # Passing Binary and X/Y coordinated to display function
            self._display(self.canvasLeft, self.vals)
            print("-----------")
             
            for i in self.inVals:
                for index in range(2, 5):
                    self.threshold.append(i[index])
            self.threshold = [self.threshold[i:i+3] for i in range(0, len(self.threshold), 3)]
            
            print(self.threshold[0:50])

            pixelAverage = []
            for x in self.threshold:
                pixelAverage.append(sum(int(x))//len(int(x)))
            print("------")
            print(pixelAverage[0:20])
            
        
        else:
            self.filePath.config(text="Unknown file type was selected. Please select txt image.")

    def saveFile(self):
        print("Working")

    def closeApplication(self):
        self.master.destroy()

    def processThreshold(self):
        self.canvasRight.delete("all")
        self.binaryOutput = GreyScaleImage().binariseImage(self.inVals, self.thresholdEntry.get())
        self._display(self.canvasRight, self.binaryOutput)
  
if __name__ == "__main__":
    BinaryConverter().mainloop()

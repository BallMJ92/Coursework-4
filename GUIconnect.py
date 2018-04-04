# Matthew Ball MSc Information Technology 04/04/2018
class GUIconnect:
    # This is an abstract class, do not ammend it.
    
    def getThreshold(self):
       #This method must return the mean of the intensity for the image
       #This value will need to be converted to an integer, use int(). 
       raise NotImplementedError('getThreshold must be implemented by subclass')

   
    def binariseImage(self, threshold):
        #Your "Process" Button should call this method.
        #the "threshold" argument is the value extracted from the entry box in your GUI.
        #This method must return an object of type BinaryImage 
        raise NotImplementedError('binariseImage must be implemented by subclass')

    def dataForDisplay(self):
        #This method returns the data in a form that can be displayed. 
        #It will be passed as the parameter "inputPts" to the method _display() in the class BinaryConverter   
        raise NotImplementedError('dataForDisplay must be implemented by subclass')

# Matthew Ball MSc Information Technology 04/04/2018
from GUIconnect import GUIconnect
from BinaryImage import BinaryImage

class GreyScaleImage(GUIconnect):

   def getThreshold(self, meanIntensity):

       # Getting intensity value  
       intensity = sum(meanIntensity) // len(meanIntensity)
      
       return intensity
      
   def binariseImage(self, data, threshold):
      # Removing all commas from data list of list 
      data = [[x.strip(",") for x in group] for group in data]
      threshold = int(threshold)      
      binaryVals = []

      # Iterating over individual list within data list of list
      for i in data:
         # Assigning values to x, y and v variables
         x, y, v = i
         # Checking in value of v is less than value of threshold
         if int(v) < threshold:
            # Assigning new binary value to v
            v = 0
         elif int(v) >= threshold:
            v = 1
         else:
            pass

         # Assinging all values x, y, v to vals variable
         vals = int(x), int(y), int(v)
         # Appending all vals to the binaryVals list
         binaryVals.append(vals)
      
      return binaryVals

   
   def dataForDisplay(self, data):
      self.outVals = []        

      # Iterating over data list of list straight from in file
      try:
         for i in data:
            # Assigning values to individual x, y and v variables
            x, y, v = i
            # Removing commas from each variable
            x = x.replace(",", "")
            y = y.replace(",", "")
            v = v.replace(",", "")
            # Assigning values to vals variable including determined color value of v
            vals = int(x), int(y), str(self._determineColorValue(int(v)))
            self.outVals.append(vals)
      except Exception:
         # Raising value error to be caught in binary converter if unable to read data
         raise ValueError
      
      return self.outVals  
         
   def _determineColorValue(self,v):
       return ("#%02x%02x%02x" % (v, v, v))

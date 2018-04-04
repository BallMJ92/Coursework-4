# Matthew Ball MSc Information Technology 04/04/2018
from GUIconnect import GUIconnect
from BinaryImage import BinaryImage

class ColourImage(GUIconnect):


   def getThreshold(self, meanIntensity):

      # Getting intensity value
      intensity = sum(meanIntensity) // len(meanIntensity)
      
      return intensity

   def binariseImage(self, data, threshold):
      threshold = int(threshold)      
      binaryVals = []

      # Iterating over individual list within data list of list
      for i in data:
         x, y, r, g, b = i
         # Getting sum intensity of variables divided by variable amount of 3
         sumIntensity = (int(r)+int(g)+int(b))//3
         # Checking if sum intensity is less or greater than threshold
         if sumIntensity < threshold:
            # Reassigning binary value to variable v
            v = 0
         elif sumIntensity >= threshold:
            v = 1
         else:
            pass

         # Assigning variables to vals and appending to list
         vals = int(x), int(y), int(v)
         binaryVals.append(vals)
      
      return binaryVals
   
   def dataForDisplay(self, data):
      outVals = []

      # Iterating over data list of list
      for i in data:
         try:
            # Assigning values from list to x, y, r, g, b variables
            x, y, r, g, b = i
            x = x.replace(",", "")
            y = y.replace(",", "")
            r = r.replace(",", "")
            g = g.replace(",", "")
            b = b.replace(",", "")
            # Assigning values to vals variable including determined color value of v
            vals = int(x), int(y), str(self._determineColorValue(int(r), int(g), int(b)))
            # Appending vals variable to outVals list which is returned after function completes successfully
            outVals.append(vals)
         except Exception:
            # Raising value error to be caught in binary converter if unable to read data
            raise ValueError
         
      return outVals

   def _determineColorValue(self,r,g,b):
        return ("#%02x%02x%02x" % (r,g,b))

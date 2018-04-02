from GUIconnect import GUIconnect
from BinaryImage import BinaryImage

class ColourImage(GUIconnect):


   def getThreshold(self, meanIntensity):
      
      intensity = sum(meanIntensity) // len(meanIntensity)
      
      return intensity

   def binariseImage(self, data, threshold):
      threshold = int(threshold)
      
      binaryVals = []
      
      for i in data:
         x, y, r, g, b = i
         sumIntensity = (int(r)+int(g)+int(b))//3
         if sumIntensity < threshold:
            v = 0
         elif sumIntensity >= threshold:
            v = 1
         else:
            pass
         vals = int(x), int(y), int(v)
         binaryVals.append(vals)

      print(sumIntensity)
      
      return binaryVals
   
   def dataForDisplay(self, data):
      outVals = []

      for i in data:
         x, y, r, g, b = i
         x = x.replace(",", "")
         y = y.replace(",", "")
         r = r.replace(",", "")
         g = g.replace(",", "")
         b = b.replace(",", "")
         vals = int(x), int(y), str(self._determineColorValue(int(r), int(g), int(b)))
         outVals.append(vals)

      # Intensity of each pixel

         
      return outVals

   def _determineColorValue(self,r,g,b):
        return ("#%02x%02x%02x" % (r,g,b))

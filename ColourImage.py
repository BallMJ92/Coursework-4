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
         sumIntensity = r, g, b
         if int(round(sum(sumIntensity)/3)) < threshold:
            v = 0
         elif int(round(sum(sumIntensity)/3)) >= threshold:
            v = 1
         else:
            pass
         vals = x, y, BinaryImage()._determineColorValue(v)
         binaryVals.append(vals)
      
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



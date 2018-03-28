from GUIconnect import GUIconnect
from BinaryImage import BinaryImage

class ColourImage(GUIconnect):


   def getThreshold(self, t):
      v = 0           

      for i in t:
         v+=i

      # Average of all pixel intensity values
      tVals = int(v//len(t))

         
      return tVals

   def binariseImage(self, threshold):
      binaryVals = []
      
      for i in threshold:
         if i<tVals:
            binaryVals.append(int(1))
         else:
            binaryVals.append(int(0))

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


   def main(self):
      print(self.dataForDisplay("ColourImage.txt")[0])

if __name__ == "__main__":
   c = ColourImage()
   c.main()

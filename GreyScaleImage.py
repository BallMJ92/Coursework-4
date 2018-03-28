from GUIconnect import GUIconnect
from BinaryImage import BinaryImage

class GreyScaleImage(GUIconnect):

   def getThreshold(self, t):
      #super(GreyScaleImage, self).getThreshold()
      v = 0
      binaryVals = []
      
      for i in t:
         v+=int(i)

      self.x = int(v//len(t))

      

      """for index in range(2, len(c), 3):
         c[index] = int(x)

      print(c[0:50])

      c = [c[i:i+3] for i in range(0, len(c), 3)]
      
      print(c[0:50])"""

      return self.x
      
   def binariseImage(self):

      """for index in range(2, len(self.inVals), 3):
          n = int(self.inVals[index])
          if n >= self.x:
             self.inVals[index] = int(1)
          else:
             self.inVals[index] = int(0)

      print(self.inVals[0:50])"""
      
      self.t = [1 if i >= self.x else 0 for i in self.t]
      print(self.t[0:50])
      b = []

   
   def dataForDisplay(self, filename):
      self.inVals = []
      self.outVals = []
      self.t = []
      self.coordinates = []
      xyCoordinates = []
      
      try:
         with open(filename) as input_file:
            fline = input_file.readline()
            if fline.strip() == "Greyscale Image":
               for line in input_file:
                  self.inVals.append(line.split())
         input_file.close()
      except Exception:
         pass

      for i in self.inVals:
         x, y, v = i
         x = x.replace(",", "")
         y = y.replace(",", "")
         v = v.replace(",", "")
         vals = int(x), int(y), str(self._determineColorValue(int(v)))
         self.t.append(int(v))
         self.coordinates.extend((int(x), int(y)))
         self.outVals.append(vals)

      print("In vals")
      print(self.inVals[0:50])
      print("------")
      return self.outVals, self.getThreshold(self.t), self.t   
         
   def _determineColorValue(self,v):
            return ("#%02x%02x%02x" % (v, v, v))

   def main(self):
         self.dataForDisplay("GreyImage.txt")[1]
         self.binariseImage()

if __name__ == "__main__":
   c = GreyScaleImage()
   c.main()

        

from GUIconnect import GUIconnect
from BinaryImage import BinaryImage

class GreyScaleImage(GUIconnect):

   def getThreshold(self, t):
      #super(GreyScaleImage, self).getThreshold()
      v = 0
      for i in t:
         v+=int(i)

      x = int(v//len(t))
      return x
   
   def _openGreyScaleImage(self,filename):
      inVals = []
      outVals = []
      t = []
      
      try:
         with open(filename) as input_file:
            fline = input_file.readline()
            if fline.strip() == "Greyscale Image":
               for line in input_file:
                  inVals.append(line.split())
         input_file.close()
      except Exception:
         pass

      for i in inVals:
         x, y, v = i
         x = x.replace(",", "")
         y = y.replace(",", "")
         v = v.replace(",", "")
         vals = int(x), int(y), str(self._determineColorValue(int(v)))
         t.append(int(v))
         outVals.append(vals)

      return outVals, self.getThreshold(t)   
         
   def _determineColorValue(self,v):
            return ("#%02x%02x%02x" % (v, v, v))

   def main(self):
         self._openGreyScaleImage("GreyImage.txt")

if __name__ == "__main__":
   c = GreyScaleImage()
   c.main()

        

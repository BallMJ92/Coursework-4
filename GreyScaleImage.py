from GUIconnect import GUIconnect
from BinaryImage import BinaryImage

class GreyScaleImage(GUIconnect):

   t = 0  
   def _openGreyScaleImage(self,filename):
      filetype = "Greyscale Image"
      inVals = []
      outVals = []
      grey_v = 0
      
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
         grey_v += int(v)
         vals = int(x), int(y), str(self._determineColorValue(int(v)))
         outVals.append(vals)

      
      self.value = grey_v//len(inVals)

      return outVals, GUIconnect.getThreshold(self, self.value)   
         
   def _determineColorValue(self,v):
      return ("#%02x%02x%02x" % (v, v, v))
   
   def threshold(self):
      return t
   
   def main(self):
         self._openGreyScaleImage("GreyImage.txt")

if __name__ == "__main__":
   c = GreyScaleImage()
   c.main()

        

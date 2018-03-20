from GUIconnect import GUIconnect
from BinaryImage import BinaryImage

class GreyScaleImage(GUIconnect):

   def _openGreyScaleImage(self,filename):
      values = []

      try:
         with open(filename) as input_file:
            fline = input_file.readline()
            if fline.strip() == "Greyscale Image":
               for line in input_file:
                  values.append(line.split())
         input_file.close()
      except Exception:
         pass

      for i in values[1:200]:
         x, y, v = i
         x = x.replace(",", "")
         y = y.replace(",", "")
         v = v.replace(",", "")
         print(self._determineColorValue(int(v)))
         print(self._imageCoordinates(int(x), int(y)))
         
   def _determineColorValue(self,v):
            return ("#%02x%02x%02x" % (v, v, v))

   def _imageCoordinates(self, x, y):
            return (x, y)

   def main(self):
         self._openGreyScaleImage("GreyImage.txt")

if __name__ == "__main__":
   c = GreyScaleImage()
   c.main()

        

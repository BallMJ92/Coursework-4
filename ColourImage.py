from GUIconnect import GUIconnect
from BinaryImage import BinaryImage

class ColourImage(GUIconnect):

   def _openColorImage(self,filename):
      values = []

      try:
         with open(filename) as input_file:
            fline = input_file.readline()
            if fline.strip() == "Colour Image":
               for line in input_file:
                  values.append(line.split())
         input_file.close()
      except Exception:
         pass

      for i in values[1:200]:
         x, y, r, g, b = i
         x = x.replace(",", "")
         y = y.replace(",", "")
         r = r.replace(",", "")
         g = g.replace(",", "")
         b = b.replace(",", "")
         print(self._determineColorValue(int(r), int(g), int(b)))
         print(self._imageCoordinates(int(x), int(y)))        

   def _imageCoordinates(self, x, y):
      return (x, y)
    
   def _determineColorValue(self,r,g,b):
        return ("#%02x%02x%02x" % (r,g,b))


   def main(self):
      self._openColorImage("ColourImage.txt")

if __name__ == "__main__":
   c = ColourImage()
   c.main()

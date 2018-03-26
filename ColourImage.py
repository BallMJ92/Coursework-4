from GUIconnect import GUIconnect
from BinaryImage import BinaryImage

class ColourImage(GUIconnect):

   def getThreshold(self, t):
      v = 0
      for i in t:
         r, g, b = i
         v+=int(sum(r, g, b)//3)
      print(v)
   
   def _openColorImage(self,filename):
      inVals = []
      outVals = []
      t = []

      try:
         with open(filename) as input_file:
            fline = input_file.readline()
            if fline.strip() == "Colour Image":
               for line in input_file:
                  inVals.append(line.split())
         input_file.close()
      except Exception:
         pass

      for i in inVals:
         x, y, r, g, b = i
         x = x.replace(",", "")
         y = y.replace(",", "")
         r = r.replace(",", "")
         g = g.replace(",", "")
         b = b.replace(",", "")
         vals = int(x), int(y), str(self._determineColorValue(int(r), int(g), int(b)))
         t.append(int(r))
         t.append(int(g))
         t.append(int(g))
         outVals.append(vals)

      print(self.getThreshold(t))         
         
      return outVals           

   def _determineColorValue(self,r,g,b):
        return ("#%02x%02x%02x" % (r,g,b))


   def main(self):
      self._openColorImage("ColourImage.txt")

if __name__ == "__main__":
   c = ColourImage()
   c.main()

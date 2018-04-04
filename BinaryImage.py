# Matthew Ball MSc Information Technology 04/04/2018
class BinaryImage:

       def determinePixelValue(self, vals):
           image = []

           # Iterating over vals list
           for i in vals:
               # Extracting data from individual list and assigning to variables
               x, y, v = i
               # Reassigning variables and determined colour value to vals variable
               vals = int(x), int(y), self._determineColorValue(int(v))
               # Appending data to new image list
               image.append(vals)

           return image
            
       def _determineColorValue(self,b):
            v = 255*b
            return ("#%02x%02x%02x" % (v, v, v))

class BinaryImage:

       def determinePixelValue(self, vals):
           image = []
           for i in vals:
               x, y, v = i
               vals = int(x), int(y), self._determineColorValue(int(v))
               image.append(vals)

           return image
            
       def _determineColorValue(self,b):
            v = 255*b
            return ("#%02x%02x%02x" % (v, v, v))


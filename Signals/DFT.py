class DFT:

   def __init__(self, time, amplitude, frequencies):
      if (len(time) != len(amplitude)):
         print("Bad input")
      else:
         self.transform(time, amplitude, frequencies)
   
   def transform(self, time, ampltiude, frequencies):
      

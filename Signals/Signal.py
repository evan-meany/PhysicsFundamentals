import math
import numpy as np
import matplotlib.pyplot as plt

sampleRate = 44100.0

""" SOUND CLASS """
class Sound:
   def __init__(self, frequency, totalTime):
      self.time = []
      self.amplitude = []
      self.frequency = frequency
      self.totalTime = totalTime
      self.timeStep = 1 / sampleRate
      self.createSoundWave()


   def createSoundWave(self):
      self.time.clear()
      self.amplitude.clear()

      for currentTime in np.arange(0, self.totalTime, self.timeStep):
         self.time.append(currentTime)
         self.amplitude.append(math.sin(currentTime * self.frequency * 2 * math.pi))


""" SIGNAL CLASS """
class Signal:
   def __init__(self, sounds = []):
      self.time = []
      self.amplitude = []
      self.sounds = sounds
      self.findStepAndTotalTime()
      self.createSignalFromSounds()


   def findStepAndTotalTime(self):
      self.totalTime = 0
      for sound in self.sounds:
         if sound.totalTime > self.totalTime:
            self.totalTime = sound.totalTime
      self.timeStep = self.totalTime / sampleRate


   def createSignalFromSounds(self):
      self.time.clear()
      self.amplitude.clear()

      for currentTime in np.arange(0, self.totalTime, self.timeStep):
         self.time.append(currentTime)
      
      for index in range(len(self.time)):
         amplitudeTotal = 0

         for sound in self.sounds:
            if index < len(sound.time):
               amplitudeTotal += sound.amplitude[index]

         self.amplitude.append(amplitudeTotal)

   def scaleAmplitude(self, scaleTo):
      scaleFactor = scaleTo / max(self.amplitude)
      self.amplitude = [x * scaleFactor for x in self.amplitude]
      print("scale", scaleFactor)
      print(max(self.amplitude))


   def plot(self, labels, timeRange, plotAll):
         plt.plot(self.time, self.amplitude, label = labels[0])

         if plotAll == True:
            for i in range(len(self.sounds)):
               plt.plot(self.sounds[i].time, self.sounds[i].amplitude, label = labels[i + 1])

         plt.xlabel("Time (s)")
         plt.ylabel("Amplitude")
         plt.title("Sound Wave(s)")
         plt.xlim(timeRange)
         plt.legend()
         plt.show()


""" SIGNAL CREATE HELPER """
def createSignal(frequencies):
   sounds = []

   for frequency in frequencies:
      sound = Sound(frequency, 1)
      sounds.append(sound)
   
   return Signal(sounds)
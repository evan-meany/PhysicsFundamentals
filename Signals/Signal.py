import math
import numpy as np
import matplotlib.pyplot as plt

sampleRate = 44100.0

""" SOUND CLASS """
class Sound:
   def __init__(self, *args):
      self.time = []
      self.amplitude = []
      self.timeStep = 1 / sampleRate

      if len(args) == 0:
         self.totalTime = 0
      else:
         self.totalTime = args[1]
         self.createSoundWave(args[0])

   def createSoundWave(self, frequency):
      self.time.clear()
      self.amplitude.clear()

      for currentTime in np.arange(0, self.totalTime, self.timeStep):
         self.time.append(currentTime)
         self.amplitude.append(math.sin(currentTime * frequency * 2 * math.pi))


""" SIGNAL CLASS """
class Signal:
   def __init__(self, sounds = []):
      self.sounds = sounds
      if len(sounds) == 1:
         self.sound = sounds[0]
      else:
         self.sound = Sound()
         self.findStepAndTotalTime()
         self.createSignalFromSounds()


   def findStepAndTotalTime(self):
      self.sound.totalTime = 0
      for sound in self.sounds:
         if sound.totalTime > self.sound.totalTime:
            self.sound.totalTime = sound.totalTime


   def createSignalFromSounds(self):
      for currentTime in np.arange(0, self.sound.totalTime, self.sound.timeStep):
         self.sound.time.append(currentTime)
      
      for index in range(len(self.sound.time)):
         amplitudeTotal = 0

         for sound in self.sounds:
            if index < len(sound.time):
               amplitudeTotal += sound.amplitude[index]

         self.sound.amplitude.append(amplitudeTotal)

   def scaleAmplitude(self, scaleTo):
      scaleFactor = scaleTo / max(self.sound.amplitude)
      self.sound.amplitude = [x * scaleFactor for x in self.sound.amplitude]

   # 
   # def addSound(self, sound):


   def pushBackSound(self, sound):
      lastSignalIndex = len(self.sound.time)
      currentTime = self.sound.totalTime
      for i in range(len(sound.time)):
         currentTime += self.sound.timeStep
         self.sound.time.append(currentTime)
         self.sound.amplitude.append(sound.amplitude[i])
      self.sound.totalTime = currentTime

   def plot(self, labels, timeRange, plotAll):
         plt.plot(self.sound.time, self.sound.amplitude, label = labels[0])

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
      sound = Sound(frequency, 0.5)
      sounds.append(sound)
   
   return Signal(sounds)
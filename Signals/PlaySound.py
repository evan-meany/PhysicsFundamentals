import wave
import Signal
import struct

class PlaySound:
   def __init__(self, signal, wavefile = "output.wav"):
      self.wavefile = wavefile
      self.generateWaveFile(signal)
   
   def generateWaveFile(self, signal):
      waveCreate = wave.open(self.wavefile, 'wb')
      # wav params
      nchannels = 1
      sampwidth = 2
      nframes = len(signal.sound.time)
      comptype = "NONE"
      compname = "not compressed"
      waveCreate.setparams((nchannels, sampwidth, Signal.sampleRate, nframes, comptype, compname))

      for sample in signal.sound.amplitude:
         waveCreate.writeframes(struct.pack('h', int( sample * 32767.0 )))

      waveCreate.close()

      return
import Signal
import Music
import PlaySound
import winsound

""" MAIN """
def main():
   # aMajor = Music.Chord("A", "Major")
   # aMajor.printChordInfo()
   # aMajor.plotSignal()

   # dsDiminished = Music.Chord("DS", "Diminished")
   # dsDiminished.printChordInfo()
   # dsDiminished.plotSignal(False)

   cMinor = Music.Chord("C", "Major")
   print(max(cMinor.signal.amplitude))
   # cMinor.plotSignal()
   cMinor.signal.scaleAmplitude(0.5)
   print(max(cMinor.signal.amplitude))

   sound = PlaySound.PlaySound(cMinor.signal)
main()
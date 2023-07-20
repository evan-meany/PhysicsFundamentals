import Signal
import Music
import PlaySound
import winsound

""" MAIN """
def main():
   cMinor = Music.Chord("C", "Major")
   cMinor.plotSignal()
   cMinor.signal.scaleAmplitude(0.5)
   print(max(cMinor.signal.sound.amplitude))

   sound = PlaySound.PlaySound(cMinor.signal, "CMajor.wav")
   
   cNote = Signal.createSignal([Music.noteFrequencies["C"]])
   sound = PlaySound.PlaySound(cNote, "CNote.wav")
   eNote = Signal.createSignal([Music.noteFrequencies["E"]])
   sound = PlaySound.PlaySound(eNote, "ENote.wav")
   gNote = Signal.createSignal([Music.noteFrequencies["G"]])
   sound = PlaySound.PlaySound(gNote, "GNote.wav")
   empty = Signal.createSignal([0])
   sound = PlaySound.PlaySound(empty, "empty.wav")
   chordProg = Music.Composition(Music.Chord("D", "Minor").signal, Music.Chord("G", "Major").signal, Music.Chord("C", "Major").signal)
   chordProg = Music.Composition(Music.Chord("D", "Minor").signal, Music.Chord("G", "Major").signal, Music.Chord("E", "Major").signal)
   chordProg = Music.Composition(Music.Chord("A", "Minor").signal, Music.Chord("B", "Diminished").signal, Music.Chord("A", "Minor").signal,\
               Music.Chord("D", "Minor").signal, Music.Chord("G", "Major").signal, Music.Chord("C", "Major").signal,\
               Music.Note("C").signal, Music.Note("E").signal,Music.Note("G").signal,Music.Note("C").signal,)
   lotr = Music.Composition(Music.Note("C").signal)
   lotr.addSignals([Music.Note("D").signal])
   lotr.addSignals([Music.Note("E").signal])
   lotr.addSignals([Music.Note("G").signal])
   lotr.addSignals([Music.Note("E").signal])
   lotr.addSignals([Music.Note("D").signal])
   lotr.addSignals([Music.Note("C").signal])
   lotr.addSignals([Music.Note("C").signal])
   lotr.addSignals([Music.Note("E").signal])
   lotr.addSignals([Music.Note("G").signal])
   lotr.addSignals([Music.Note("A").signal])
   lotr.addSignals([Music.Note("C").signal])
   lotr.addSignals([Music.Note("B").signal])
   lotr.addSignals([Music.Note("G").signal])
   lotr.addSignals([Music.Note("E").signal])
   lotr.addSignals([Music.Note("F").signal])
   lotr.addSignals([Music.Note("E").signal])
   lotr.addSignals([Music.Note("D").signal])
   lotr.addSignals([Music.Note("C").signal])
   lotr.signal.scaleAmplitude(0.5)

   sound = PlaySound.PlaySound(lotr.signal, "ChordProg251.wav")

main()
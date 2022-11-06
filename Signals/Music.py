import Signal

""" NOTES """
notes = ["C", "CS", "D", "DS", "E", "F", "FS", "G", "GS", "A", "AS", "B"]

noteFrequencies = {
   "C": 523.25,
   "CS": 554.37,
   "D": 587.33,
   "DS": 622.25,
   "E": 659.25,
   "F": 698.46,
   "FS": 739.99,
   "G": 783.99,
   "GS": 830.61,
   "A": 880.00,
   "AS": 932.33,
   "B": 987.77,
}


""" CHORDS CLASS """
class Chord:
   def __init__(self, rootNote = "C", chordType = "Major"):
      self.name = rootNote + " " + chordType
      self.notes = []
      self.frequencies = []
      self.createChord(rootNote, chordType)
      self.createSignal()

   def createChord(self, rootNote, chordType):

      noteSequence = []
      if chordType == "Major":
         noteSequence = [0, 4, 7]
      elif chordType == "Minor":
         noteSequence = [0, 3, 7]
      elif chordType == "Diminished":
         noteSequence = [0, 3, 6]
      elif chordType == "Augmented":
         noteSequence = [0, 4, 8]
      
      rootIndex = 0
      for i in range(len(notes)):
         if notes[i] == rootNote:
            rootIndex = i
            break

      for i in noteSequence:
         note = notes[(rootIndex + i) % 12]
         self.notes.append(note)

      for note in self.notes:
         self.frequencies.append(noteFrequencies[note])

   def createSignal(self):
      self.signal = Signal.createSignal(self.frequencies)

   def plotSignal(self, plotAll = True):
      labels = [self.name]
      labels.extend(self.notes)
      self.signal.plot(labels, [0, 0.01], plotAll)

   def printChordInfo(self):
      print("Name: ", self.name)
      print("Notes: ", self.notes)
      print("Frequencies: ", self.frequencies)
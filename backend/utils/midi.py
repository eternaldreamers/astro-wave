from midiutil import MIDIFile
from mingus.core import chords
import os

class Midi:
    NOTES = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']
    OCTAVES = list(range(11))
    NOTES_IN_OCTAVE = len(NOTES)
    errors = {
        'notes': 'Bad input, please refer this spec-\n'
    }

    def __init__(self, data_property, chord_progression, tiempo, duration, octave, track):
        self.data_property = data_property
        self.chord_progression = chord_progression
        self.tiempo = tiempo
        self.duration = duration
        self.octave = octave
        self.track = track

    @staticmethod
    def swap_accidentals(note):
        if note == 'Db':
            return 'C#'
        if note == 'D#':
            return 'Eb'
        if note == 'E#':
            return 'F'
        if note == 'Gb':
            return 'F#'
        if note == 'G#':
            return 'Ab'
        if note == 'A#':
            return 'Bb'
        if note == 'B#':
            return 'C'

        return note

    @classmethod
    def note_to_number(self, cls, note, octave):
        note = self.swap_accidentals(note)
        assert note in self.NOTES, self.errors['notes']
        assert octave in self.OCTAVES, self.errors['notes']

        note = self.NOTES.index(note)
        note += (self.NOTES_IN_OCTAVE * octave)

        assert 0 <= note <= 127, self.errors['notes']

        return note

    def generate_midi(self):
        array_of_notes = [chords.from_shorthand(chord)[0] for chord in self.chord_progression]
        array_of_note_numbers = [self.note_to_number(note, self.octave) for note in array_of_notes]

        track = self.track
        channel = 0
        time = 1
        tempo = self.tiempo
        volume = 100

        MyMIDI = MIDIFile(1)
        MyMIDI.addTempo(track, time, tempo)

        for i, pitch in enumerate(array_of_note_numbers):
            MyMIDI.addNote(track, channel, pitch, time + (i*4), self.duration, volume)

        with open(f"{self.data_property}.mid", "wb") as output_file:
            MyMIDI.writeFile(output_file)

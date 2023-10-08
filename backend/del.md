moon
https://images-assets.nasa.gov/image/PIA00405/PIA00405~medium.jpg

earth
https://images-assets.nasa.gov/image/PIA18033/PIA18033~medium.jpg

mars
https://images-assets.nasa.gov/image/PIA08636/PIA08636~small.jpg


venus
https://images-assets.nasa.gov/image/PIA00270/PIA00270~medium.jpg


mercury
https://images-assets.nasa.gov/image/PIA15161/PIA15161~medium.jpg

jupiter
https://images-assets.nasa.gov/image/PIA00343/PIA00343~small.jpg

saturn
https://images-assets.nasa.gov/image/PIA03152/PIA03152~small.jpg

uranus
https://images-assets.nasa.gov/image/stsci-h-p1906c-f-514x514.a/stsci-h-p1906c-f-514x514.a~orig.png

neptune
https://images-assets.nasa.gov/image/PIA01492/PIA01492~medium.jpg

Andromeda Galaxy
https://images-assets.nasa.gov/image/PIA04921/PIA04921~medium.jpg



## Propiedades
- moons
- gravity
- temperatue
- rings
- water
- craters
- radiation
- density
- size
- volcanoes
- aurora


{
    "img_id": "65228911233296e311cca4f3",
    "moons": 1,
    "gravity": "9.81",
    "temperature": "14.0",
    "rings": 0,
    "water": "71.0",
    "craters": 0,  // La Tierra tiene cráteres, pero no es una característica definitoria como en otros cuerpos celestes.
    "radiation": "0.0",  // La atmósfera terrestre y el campo magnético protegen a la Tierra de la mayoría de la radiación cósmica.
    "density": "5.52",
    "size": "12742.0",  // Diámetro en km
    "volcanoes": 1500,  // Estimación del número de volcanes activos e inactivos en la Tierra.
    "auroras": 2  // Auroras Boreales y Australes
}

from midiutil import MIDIFile
from mingus.core import chords

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
    def note_to_number(cls, note, octave):
        note = swap_accidentals(note)
        assert note in NOTES, errors['notes']
        assert octave in OCTAVES, errors['notes']

        note = NOTES.index(note)
        note += (NOTES_IN_OCTAVE * octave)

        assert 0 <= note <= 127, errors['notes']

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

# Uso:
midi_instance = Midi(
    data_property="density",
    chord_progression=["F#m7b5", "Bm7b5", "Em7", "Amaj7", "C#m7", "F#m7", "Bm7"],
    tiempo=500,
    duration=1,
    octave=4,
    track=0
)
midi_instance.generate_midi()


from midiutil import MIDIFile
from mingus.core import chords

chord_progression = ["Cmaj7", "Cmaj7", "Fmaj7", "Gdom7","Edom7"]

NOTES = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']
OCTAVES = list(range(11))
NOTES_IN_OCTAVE = len(NOTES)

errors = {
    'notes': 'Bad input, please refer this spec-\n'
}


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


def note_to_number(note: str, octave: int) -> int:
    note = swap_accidentals(note)
    assert note in NOTES, errors['notes']
    assert octave in OCTAVES, errors['notes']

    note = NOTES.index(note)
    note += (NOTES_IN_OCTAVE * octave)

    assert 0 <= note <= 127, errors['notes']

    return note


array_of_notes = []
for chord in chord_progression:
    array_of_notes.append(chords.from_shorthand(chord)[0])

array_of_note_numbers = []
for note in array_of_notes:
    OCTAVE = 8
    array_of_note_numbers.append(note_to_number(note, OCTAVE))

track = 0
channel = 0
time = 1  # In beats modifica la pista
duration = 10   # In beats modifica el tamaño de los acordes
tempo = 1000  # In BPM
volume = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
# automatically)
MyMIDI.addTempo(track, time, tempo)

for i, pitch in enumerate(array_of_note_numbers):
    MyMIDI.addNote(track, channel, pitch, time + (i*4), duration, volume)

with open("pure-edm-fire-bass.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)


import subprocess

class Midi:
    # ... (resto de la clase)

    def midi_to_mp3(self, soundfont_path):
        midi_path = f"{self.data_property}.mid"
        mp3_path = f"{self.data_property}.mp3"
        
        # Convertir MIDI a WAV usando FluidSynth
        subprocess.run(["fluidsynth", "-ni", soundfont_path, midi_path, "-F", "temp.wav", "-r", "44100"])
        
        # Convertir WAV a MP3 usando ffmpeg (necesitas tener ffmpeg instalado)
        subprocess.run(["ffmpeg", "-i", "temp.wav", mp3_path])
        
        # Eliminar el archivo WAV temporal
        subprocess.run(["rm", "temp.wav"])


midi_instance = Midi(
    # ... (parámetros)
)
midi_instance.generate_midi()
midi_instance.midi_to_mp3("/path/to/your/soundfont.sf2")


midi_instance = Midi(
    # ... (parámetros)
)
midi_instance.generate_midi()
midi_instance.midi_to_mp3("/path/to/your/soundfont.sf2")

El archivo .sf2 es un SoundFont, que es esencialmente una colección de samples de audio que se utilizan para convertir los datos MIDI en sonido audible. No se "genera" en el sentido tradicional dentro de tu código; en su lugar, debes obtenerlo de una fuente externa.

Los SoundFonts .sf2 son archivos preexistentes que contienen instrumentos muestreados. Estos archivos se utilizan para dar a los archivos MIDI un sonido específico cuando se reproducen. Por ejemplo, un archivo MIDI podría tener una nota que se supone que suene como un piano, pero sin un SoundFont, el sistema no sabría cómo debe sonar ese piano.

Para usar FluidSynth para convertir archivos MIDI a audio, necesitas un archivo SoundFont .sf2. Hay muchos SoundFonts disponibles en línea, y algunos son gratuitos. Como mencioné anteriormente, un SoundFont popular es GeneralUser GS, que puedes descargar desde aquí. Una vez descargado, tendrás un archivo .sf2 que puedes usar con FluidSynth.

Para usarlo en el método midi_to_mp3 que proporcioné anteriormente, simplemente proporciona la ruta al archivo .sf2 descargado cuando llames al método:

python
Copy code
midi_instance.midi_to_mp3("/ruta/donde/descargaste/el/soundfont.sf2")
Reemplaza "/ruta/donde/descargaste/el/soundfont.sf2" con la ubicación real del archivo .sf2 en tu sist
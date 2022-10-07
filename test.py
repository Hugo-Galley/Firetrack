from os import path
from pydub import AudioSegment

src = "Song/2055.mp3"
dst = "test.wav"

sound = AudioSegment.from_mp3(src)
sound.export(dst,format="wav")
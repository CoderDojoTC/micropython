from os import path
from pydub import AudioSegment

# files
# src = "/Users/dan/Documents/ws/robot-media/mp3-files/Excited-R2D2.mp3"
src = "Excited-R2D2.mp3"
# dst = "/Users/dan/Documents/ws/robot-media/wav-files/Excited-R2D2.wav"
dst = "Excited-R2D2.wav"
# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")
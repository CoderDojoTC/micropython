import pydub
import 

song = pydub.AudioSegment.from_mp3("Excited-R2D2.mp3")
song.export(dst, format="wav")
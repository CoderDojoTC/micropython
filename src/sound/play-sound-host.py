# import required libraries
from pydub import AudioSegment 
from pydub.playback import play 
  
# Import an audio file 
# Format parameter only
# for readability 
# /Users/dan/Documents/ws/robot-media/wav-files
wav_file = AudioSegment.from_file(file = "/Users/dan/Documents/ws/robot-media/wav-files/R2D2-yeah.wav", format = "wav") 
  
# Play the audio file
play(wav_file)
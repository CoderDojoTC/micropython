import wave

filename = '/sounds/cylon-by-your-command.wav'
# use the wave class open function
f = wave.open(filename,'rb')

# get sample stats of the wave file
rate = f.getframerate()
bytesDepth = f.getsampwidth()
channels = f.getnchannels()
frameCount = f.getnframes()

print('Rate: ', rate)
print('bytes depth', bytesDepth)
print('channels:', channels)
print('frameCount:', frameCount)
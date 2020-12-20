import wave
import os

filepath = os.path.dirname(__file__) + '/'

print('filepath = ',filepath)
filename = filepath + 'stereo.wav'


f = wave.open(filename,'r')
nframes = f.getnframes()
nchannels = f.getnchannels()
strdata = f.readframes(nframes)
print('len_strdata',len(strdata))
monodata = strdata[43::2]  #提取第一个通道的数据,去掉wav开头44bit的字节头
print('len_monodata',len(monodata))

fw = wave.open(filepath + 'mono.wav','w')
fw.setnchannels(1)
fw.setsampwidth(2)
fw.setframerate(16000)
fw.writeframes(monodata)
fw.close()




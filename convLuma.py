import sys

#Entradas: video, w, h, nF

video = sys.argv[1]
w = int(sys.argv[2])
h = int(sys.argv[3])
nF = int(sys.argv[4])
out = "../../Results/convLuma_" + video

def convLuma(seq, w, h, nF):
	f = open("../../origCfP/" + seq, 'rb')
	r = open(out, 'wb')
	res = h * w
	
	for frames in range(0,nF):
		Y = f.read(res)
		r.write(Y)
		f.read(res/2)
	f.close()
	r.close()

convLuma(video, w, h, nF)

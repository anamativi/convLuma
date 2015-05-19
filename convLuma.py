import sys

#Entradas: video, nF

video = sys.argv[1] + ".yuv"
nF = int(sys.argv[2])
out = "../../Results/convLuma_" + video

def convLuma(seq, nF):
	size = seq.split("_")
	size = size[1].split("x")
	h = int(size[0])
	w = int(size[1])
	f = open("../../origCfP/" + seq, 'rb')
	r = open(out, 'wb')
	res = h * w
	
	for frames in range(0,nF):
		Y = f.read(res)
		r.write(Y)
		f.read(res/2)
	f.close()
	r.close()

convLuma(video, nF)

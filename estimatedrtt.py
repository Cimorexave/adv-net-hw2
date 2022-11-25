def read_file() -> list:
	samplertt = []
	file = open('samplertt.txt','r')
	while True:
		line = file.readline()[:-1]
		if not line:
			break;
		samplertt.append(float(line))
	file.close()	
	return samplertt

def estimatedrtt_cal(samplertt) -> list:
	alpha = 0.125
	result = []

	result.append((1-alpha)*samplertt[0] + alpha*samplertt[0])
	for item in range(49):
		reslut.append(
			round(((1 - alpha) * result[item]) + (alpha * samplertt[item+1]), 2))
		
	return result

print(estimatedrtt_cal(read_file()))


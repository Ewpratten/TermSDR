from scipy.interpolate import interp1d

m = None

def buildMap(rows):
	global m
	m = interp1d([1,-1],[1,rows])

def remap(data):
	output = []
	for item in data:
		num = item.real
		output.append(m(num))
	return output
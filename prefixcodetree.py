class PrefixCodeTree:

	def __init__(self):
		self.codebook={}
	
	def insert(self, codeword, symbol):
		str_key = ''.join(str(x) for x in codeword)
		self.codebook[str_key] = symbol

	def decode(self, encoded_data, datalen):
		bits = []
		for data in encoded_data:
			bits.append('{0:08b}'.format(data))
		bits = ''.join(bits)

		de = []
		com = ''
		for i in range(datalen):
			com += bits[i]
			
			if com in self.codebook:
				de.append(self.codebook[com])
				com = ''

		return ''.join(de)
	

if __name__ == '__main__':
	codebook = {
		'x1': [0],
		'x2': [1, 0, 0],
		'x3': [1, 0, 1],
		'x4': [1, 1]
	}

	codeTree = PrefixCodeTree()
	
	for sym in codebook:
		codeTree.insert(codebook[sym], sym)

	message = codeTree.decode(b'\xd2\x9f\x20', 21)
	print(message)

# Python program to demonstrate
# hamming code

class Hamming:

	correctHamming=''

	def start(self, data):

		m = len(data)
		r = self.calcRedundantBits(m)

		arr = self.posRedundantBits(data, r)
		arr = self.calcParityBits(arr, r)

		print("Data transferred (calcParityBits) is ", arr)

		self.correctHamming=arr
		return arr

	def calcRedundantBits(self, m):

		for i in range(m):
			if(2**i >= m + i + 1):
				return i

	def posRedundantBits(self, data, r):
		j = 0
		k = 1
		m = len(data)
		res = ''
		data=data[::-1]
		for i in range(1, m+r+1):
			if(i == 2**j):
				res = res + 'p'
				j += 1
			else:
				res = res + data[-1 * k]
				k += 1
		print(res)
		return res


	def calcParityBits(self, arr, r):
		n = len(arr)

		auxCheck=''
		movementsList=[]
		movementsList.append(arr)

		for i in range(r):
			par=2**i
			auxPar = self.getBinary(par).find('1')

			for j in range(n):
				if self.getBinary(j+1)[auxPar]=='1':
					auxCheck += arr[j]
				else:
					auxCheck += ' '
			# print("AuxCheck es", auxCheck)


			posPAuxCheck = auxCheck.find('p')
			# print("pos es", posPAuxCheck, "y arr es", arr)
			auxCheck=self.chekParity(auxCheck)
			arr = arr.replace('p', auxCheck[posPAuxCheck],1)
			movementsList.append(auxCheck)
			auxCheck=''

		movementsList.append(arr)
		movementsList[0] = movementsList[0].replace('p',' ')
		# print("Los movimientos realizados son", movementsList)


		return movementsList


	def getBinary(self, num):
		aux = bin(num)[2::]

		while len(aux)!=5:
			aux='0'+aux

		return aux

	def chekParity(self, arr):
		count = arr.count('1')

		if count%2==1:
			arr = arr.replace("p","1")
		else:
			arr = arr.replace("p","0")

		return arr




	def detectError(self, newArr):

		# n = len(arr)
		# res = 0
		#
		# # Calculate parity bits again
		# for i in range(nr):
		# 	val = 0
		# 	for j in range(1, n + 1):
		# 		if(j & (2**i) == (2**i)):
		# 			val = val ^ int(arr[-1 * j])
		#
		# 	# Create a binary no by appending
		# 	# parity bits together.
		#
		# 	res = res + val*(10**i)

		# Convert binary to decimal
		return int(str(1), 2)

	def calcParityBitsForError(self, newArr):
		n = len(newArr)

		auxCheck=''
		movementsList=[]
		movementsList.append(newArr)

		for i in range(5):
			par=2**i
			auxPar = self.getBinary(par).find('1')

			for j in range(n):
				if self.getBinary(j+1)[auxPar]=='1':
					auxCheck += newArr[j]
				else:
					auxCheck += ' '


			posPAuxCheck = 2**i-1
			# print("pos es", posPAuxCheck, "y arr es", arr)
			auxCheck=self.chekParity(auxCheck)
			# newArr = newArr.replace('p', self.correctHamming[posPAuxCheck], 1)
			movementsList.append(auxCheck)
			auxCheck=''


		movementsList[0] = movementsList[0].replace('p',' ')
		# print("Los movimientos realizados son", movementsList)

		print(movementsList)
		return movementsList


if __name__ == "__main__":
	hamming = Hamming()
	hamming.start('101100101110')
	# hamming.calcParityBitsForError('00011111010011010')




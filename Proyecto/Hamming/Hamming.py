# Python program to demonstrate
# hamming code

class Hamming:

	def start(self, data):

		# Calculate the no of Redundant Bits Required
		m = len(data)
		r = self.calcRedundantBits(m)

		# Determine the positions of Redundant Bits
		arr = self.posRedundantBits(data, r)
		print("posRedundantBits es", arr)

		# Determine the parity bits
		arr = self.calcParityBits(arr, r)

		# Data to be transferred
		print("Data transferred (calcParityBits) is ", arr)

		# Stimulate error in transmission by changing
		# a bit value.
		# 10101001110 -> 11101001110, error in 10th position.

		# arr = '00011111010011011'
		aux='00011111010011011'


		# print("Error Data is " + arr)
		# correction = self.detectError(arr, r)
		# if (correction == 0):
		# 	print("There is no error in the received message.")
		# else:
		# 	print("The position of error is ", len(arr) - correction + 1, "from the left")

		return arr

	def calcRedundantBits(self, m):

		# Use the formula 2 ^ r >= m + r + 1
		# to calculate the no of redundant bits.
		# Iterate over 0 .. m and return the value
		# that satisfies the equation

		for i in range(m):
			if(2**i >= m + i + 1):
				return i

	def posRedundantBits(self, data, r):

		# Redundancy bits are placed at the positions
		# which correspond to the power of 2.
		j = 0
		k = 1
		m = len(data)
		res = ''

		# If position is power of 2 then insert '0'
		# Else append the data
		for i in range(1, m + r+1):
			if(i == 2**j):
				res = res + 'p'
				j += 1
			else:
				res = res + data[-1 * k]
				k += 1

		return res


	def calcParityBits(self, arr, r):
		n = len(arr)

		auxCheck=''
		movementsList=[]
		movementsList.append(arr)

		# print("=============\n")
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


	def detectError(self, arr, nr):
		n = len(arr)
		res = 0

		# Calculate parity bits again
		for i in range(nr):
			val = 0
			for j in range(1, n + 1):
				if(j & (2**i) == (2**i)):
					val = val ^ int(arr[-1 * j])

			# Create a binary no by appending
			# parity bits together.

			res = res + val*(10**i)

		# Convert binary to decimal
		return int(str(res), 2)


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



if __name__ == "__main__":
	hamming = Hamming()
	hamming.start('101100101110')




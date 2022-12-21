# Python program to demonstrate
# hamming code

class Hamming:
    correctHamming = ''
    paridadPar = True

    def start(self, data):

        m = len(data)
        r = self.calcRedundantBits(m)

        arr = self.posRedundantBits(data, r)
        arr = self.calcParityBits(arr, r)

        print(arr)

        self.correctHamming = arr
        return arr

    def calcRedundantBits(self, m):

        for i in range(m):
            if (2 ** i >= m + i + 1):
                return i

    def posRedundantBits(self, data, r):
        j = 0
        k = 1
        m = len(data)
        res = ''
        data = data[::-1]
        for i in range(1, m + r + 1):
            if (i == 2 ** j):
                res = res + 'p'
                j += 1
            else:
                res = res + data[-1 * k]
                k += 1
        print(res)
        return res

    def calcParityBits(self, arr, r):

        n = len(arr)

        auxCheck = ''
        movementsList = []
        movementsList.append(arr)

        for i in range(r):
            par = 2 ** i
            auxPar = self.getBinary(par).find('1')

            for j in range(n):
                if self.getBinary(j + 1)[auxPar] == '1':
                    auxCheck += arr[j]
                else:
                    auxCheck += ' '
            # print("AuxCheck es", auxCheck)

            posPAuxCheck = auxCheck.find('p')
            # print("pos es", posPAuxCheck, "y arr es", arr)
            auxCheck = self.chekParity(auxCheck)
            arr = arr.replace('p', auxCheck[posPAuxCheck], 1)
            movementsList.append(auxCheck)
            auxCheck = ''

        movementsList.append(arr)
        movementsList[0] = movementsList[0].replace('p', ' ')
        # print("Los movimientos realizados son", movementsList)

        return movementsList

    def getBinary(self, num):
        aux = bin(num)[2::]

        while len(aux) != 5:
            aux = '0' + aux

        return aux

    def chekParity(self, arr):
        count = arr.count('1')

        if self.paridadPar:
            if count % 2 == 1:
                arr = arr.replace("p", "1")
            else:
                arr = arr.replace("p", "0")
        else:
            if count % 2 == 1:
                arr = arr.replace("p", "0")
            else:
                arr = arr.replace("p", "1")

        return arr

    def calcParityBitsForError(self, newArr):
        n = len(newArr)
        newArrOriginal = newArr
        bits = [newArr[0], newArr[1], newArr[3], newArr[7], newArr[15]]

        newArr = newArr[:0] + 'p' + newArr[0 + 1:]
        newArr = newArr[:1] + 'p' + newArr[1 + 1:]
        newArr = newArr[:3] + 'p' + newArr[3 + 1:]
        newArr = newArr[:7] + 'p' + newArr[7 + 1:]
        newArr = newArr[:15] + 'p' + newArr[15 + 1:]

        # print(newArr)

        auxCheck = ''
        movementsList = []
        movementsList.append(newArr)

        for i in range(5):
            par = 2 ** i
            auxPar = self.getBinary(par).find('1')

            for j in range(n):
                if self.getBinary(j + 1)[auxPar] == '1':
                    auxCheck += newArr[j]
                else:
                    auxCheck += ' '

            movementsList.append(auxCheck)
            auxCheck = ''

        # movementsList[0] = movementsList[0].replace('p',' ')
        # print("Los movimientos realizados son", movementsList)
        movementsList[0] = newArrOriginal
        movementsList[1] = movementsList[1].replace('p', bits[0])
        movementsList[2] = movementsList[2].replace('p', bits[1])
        movementsList[3] = movementsList[3].replace('p', bits[2])
        movementsList[4] = movementsList[4].replace('p', bits[3])
        movementsList[5] = movementsList[5].replace('p', bits[4])

        print(movementsList)

        testParity = []
        testParity.append([1, ''])

        testParity.append(self.checkIfError(movementsList[1], int(bits[0])))
        testParity.append(self.checkIfError(movementsList[2], int(bits[1])))
        testParity.append(self.checkIfError(movementsList[3], int(bits[2])))
        testParity.append(self.checkIfError(movementsList[4], int(bits[3])))
        testParity.append(self.checkIfError(movementsList[5], int(bits[4])))

        print(testParity)

        indexError = (testParity[1][1] * 2 ** 0) + (testParity[2][1] * 2 ** 1) + (testParity[3][1] * 2 ** 2) + (
                    testParity[4][1] * 2 ** 3) + (testParity[5][1] * 2 ** 4)
        # print("La posicion del error es", indexError)

        if indexError == 0:
            indexError = 'No hay error'
        else:
            indexError = 'La posicion del error es ' + str(indexError)

        print(indexError)
        return [movementsList, testParity, indexError]

    def checkIfError(self, str, aux):
        count = str.count('1')

        if self.paridadPar:

            if str[aux] == 1:
                if count % 2 == 0:
                    return ['Error', 1]
                else:
                    return ['Correcto', 0]
            else:
                if count % 2 == 1:
                    return ['Error', 1]
                else:
                    return ['Correcto', 0]

        else:

            if str[aux] == 1:
                if count % 2 == 0:
                    return ['Error', 0]
                else:
                    return ['Correcto', 1]
            else:
                if count % 2 == 1:
                    return ['Error', 0]
                else:
                    return ['Correcto', 1]


if __name__ == "__main__":
    hamming = Hamming()



    var = hamming.start('101100101110')
    if hamming.paridadPar:
        aux = '11010011110101100'

    else:
        aux = '01100111001011110'

    print(hamming.calcParityBitsForError(aux))

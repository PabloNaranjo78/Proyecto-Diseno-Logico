class Bases:
    def __init__(self):
        self.length = None
        self.decimal = None
        self.binary = ""
        self.number = None
        self.hexadecimal = None
        self.validValues = "01234567"
        self.conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                                5: '5', 6: '6', 7: '7',8: '8', 9: '9',
                                10: 'A',11: 'B', 12: 'C', 13: 'D',
                                14: 'E', 15: 'F'}

    def is_valid(self, num):
        self.number = int(num)

        if (self.composition(num) and 0 <= self.number <= 777):
            self.length = len(str(self.number))
            if self.number == 0:
                self.decimal = 0
                self.binary = "0"
                self.hexadecimal = "0"
            return True
        else:
            return False

    def composition(self, num):
        for x in num:
            if x not in self.validValues:
                return False
        return True

    def to_decimal(self, aux):
        num = int(aux)
        count = 0
        base = 1
        while(num):
            last = num % 10
            num = int(num/10)
            count += last * base
            base *= 8
        self.decimal = count

    def to_binary(self, num):
        if num > 1:
            self.to_binary(num // 2)
        self.binary += str(num % 2)

    def to_hexadecimal(self, num):
        hexa = ""
        while (num > 0):
            remainder = num % 16
            hexa = self.conversion_table[remainder] + hexa
            num = num // 16
        self.hexadecimal = hexa

    def get_decimal(self):
        return self.decimal

    def get_binary(self):
        aux = self.binary
        self.binary = ""
        return aux

    def get_hexadecimal(self):
        return self.hexadecimal

    def conversion(self, num):
        self.to_decimal(num)
        self.to_binary(self.get_decimal())
        self.to_hexadecimal(self.get_decimal())
        return (self.get_decimal(), self.get_binary(), self.get_hexadecimal())

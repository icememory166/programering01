DOL = input('Type your birthdate in the "YYYYMMDD" format ')
DOLL = list(map(int, DOL))

def add(digit):
    digitT = 0
    for i in digit:
        digitT += i
    digitT = str(digitT)
    digitT = [int(i) for i in digitT]
    digitT = digitT[0]
    return digitT


DigitOfLifeY = add(DOLL[:4])
DigitOfLifeM = add(DOLL[4:6])
DigitOfLifeD = add(DOLL[6:])
DigitOfLife = int(DigitOfLifeY) + int(DigitOfLifeM) + int(DigitOfLifeD)
print(f"Your digit of life is {DigitOfLife}")

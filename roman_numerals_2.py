import math

def RomanizeThousands(i):
    thousands = math.floor((i % 10000) / 1000)  # extract the value in the thousands digit
    if thousands == 0:
        return ""
    elif thousands == 1:
        return "M"
    elif thousands == 2:
        return "MM"
    elif thousands == 3:
        return "MMM"
    else:
        return "[Invalid value]"

def RomanizeHundreds(i):
    hundreds = math.floor((i % 1000) / 100)  # extract the value in the hundreds digit
    if hundreds == 0:
        return ""
    elif hundreds == 1:
        return "C"
    elif hundreds == 2:
        return "CC"
    elif hundreds == 3:
        return "CCC"
    elif hundreds == 4:
        return "CD"
    elif hundreds == 5:
        return "D"
    elif hundreds == 6:
        return "DC"
    elif hundreds == 7:
        return "DCC"
    elif hundreds == 8:
        return "DCCC"
    elif hundreds == 9:
        return "CM"
    else:
        return "[Invalid value]"

def RomanizeTens(i):
    tens = math.floor((i % 100) / 10) # extract the value in the tens digit
    if tens == 0:
        return ""
    elif tens == 1:
        return "X"
    elif tens == 2:
        return "XX"
    elif tens == 3:
        return "XXX"
    elif tens == 4:
        return "XL"
    elif tens == 5:
        return "L"
    elif tens == 6:
        return "LX"
    elif tens == 7:
        return "LXX"
    elif tens == 8:
        return "LXXX"
    elif tens == 9:
        return "XC"
    else:
        return "[Invalid value]"

def RomanizeOnes(i):
    ones = i % 10 # extract the value in the ones digit
    if ones == 0:
        return ""
    elif ones == 1:
        return "I"
    elif ones == 2:
        return "II"
    elif ones == 3:
        return "III"
    elif ones == 4:
        return "IV"
    elif ones == 5:
        return "V"
    elif ones == 6:
        return "VI"
    elif ones == 7:
        return "VII"
    elif ones == 8:
        return "VIII"
    elif ones == 9:
        return "IX"
    else:
        return "[Invalid value]"

def RomanNumeralize(i):
    return RomanizeThousands(i) + RomanizeHundreds(i) + RomanizeTens(i) + RomanizeOnes(i)

print "535 -> ", RomanNumeralize(535)
print "3999 -> ", RomanNumeralize(3999)
print "149 -> ", RomanNumeralize(149) 
print "4000 -> ", RomanNumeralize(4000) 

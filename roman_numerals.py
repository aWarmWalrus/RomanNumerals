import math

def RomanizeThousands(i):
    thousands = math.floor((i % 10000) / 1000)  # extract the value in the thousands digit
    switcher = {
            0: "",
            1: "M",
            2: "MM",
            3: "MMM",
    }
    return switcher.get(thousands, "[Invalid value]")

def RomanizeHundreds(i):
    hundreds = math.floor((i % 1000) / 100)  # extract the value in the hundreds digit
    switcher = {
            0: "",
            1: "C",
            2: "CC",
            3: "CCC",
            4: "CD",
            5: "D",
            6: "DC",
            7: "DCC",
            8: "DCCC",
            9: "CM",
    }
    return switcher.get(hundreds, "[Invalid value]")

def RomanizeTens(i):
    tens = math.floor((i % 100) / 10) # extract the value in the tens digit
    switcher = {
            0: "",
            1: "X",
            2: "XX",
            3: "XXX",
            4: "XL",
            5: "L",
            6: "LX",
            7: "LXX",
            8: "LXXX",
            9: "XC",
    }
    return switcher.get(tens, "[Invalid value]")

def RomanizeOnes(i):
    ones = i % 10 # extract the value in the ones digit
    switcher = {
            0: "",
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "IIX",
            9: "IX",
    }
    return switcher.get(ones, "[Invalid value]")


def RomanNumeralize(i):
    return RomanizeThousands(i) + RomanizeHundreds(i) + RomanizeTens(i) + RomanizeOnes(i)

print "535 -> ", RomanNumeralize(535)
print "3999 -> ", RomanNumeralize(3999)
print "149 -> ", RomanNumeralize(149) 
print "4000 -> ", RomanNumeralize(4000) 

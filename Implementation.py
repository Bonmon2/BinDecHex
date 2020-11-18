import BinHexDec

Num1 = BinHexDec.Nums(11, 10)
Num2 = BinHexDec.Nums("12", 10)

print(Num2 - Num1)
print(Num1 + 1)
print(Num1 - 12)

Num3 = BinHexDec.Nums(11, 2)
print(Num3.DecVal)
Num3.ToType(3)
print(Num3.DecVal)

Num4 = BinHexDec.Nums(-12, 5)
print(Num4)
print(1 + Num4)

print(1 - Num4)
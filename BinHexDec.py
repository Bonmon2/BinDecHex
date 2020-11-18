_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
_numerals = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def _valtypecheck(_numtype):
    if isinstance(_numtype, int):
        if _numtype > 36:
            raise ValueError("Sorry BinHexDec currently has now way of using bases over base 36")
        else:
            return _numtype
    elif isinstance(_numtype, float):
        raise TypeError("NumType cannot accept a type float")
    elif _numtype.lower() in ["bin", "dec", "hex"]:
        if _numtype == "bin":
            return 2
        elif _numtype == "dec":
            return 10
        else:
            return 16
    else:
        raise ValueError("Unknown type idetifier")

def _inputtednonnumvaltypecheck(var):
    if isinstance(var, int):
        return True
    elif isinstance(var, str):
        for x in range(len(var)):
            if var[x] in _alphabet:
                raise TypeError("You can't add a letter to a number, if this letter " + var[x] + " was meant to to represent a value please use the class so that the base can be identified")
        return True
    elif isinstance(var, float):
        raise ValueError("Nums cannot accept float values as they are often hard to implement into other bases")
    else:
        return False

class Nums():
    def __init__(self, NumVal, NumType):
        
        if not(isinstance(NumVal, str)):
            NumVal = str(NumVal)
        
        _temporarynumval = ""
        if NumVal[0] == "-":
            for x in range(len(NumVal) - 1):
                _temporarynumval = _temporarynumval + NumVal[x + 1]
            pnMultiplier = -1
            NumVal = _temporarynumval
        else:
            pnMultiplier = 1

        self.ValType = _valtypecheck(NumType)
        self.DecVal = self._toDec(NumVal) * pnMultiplier


    def __add__(self, var2):
        if _inputtednonnumvaltypecheck(var2):
            _sumval = self.DecVal + int(var2)
        else:
            _sumval = self.DecVal + var2.DecVal
        return _sumval

    def __radd__(self, var2):
        if _inputtednonnumvaltypecheck(var2):
            _sumval = self.DecVal + int(var2)
        else:
            _sumval = self.DecVal + var2.DecVal
        return _sumval


    def __sub__(self, var2):
        if _inputtednonnumvaltypecheck(var2):
            _subval = self.DecVal - int(var2)
        else:
            _subval = self.DecVal - var2.DecVal
        return _subval

    def __rsub__(self, var2):
        if _inputtednonnumvaltypecheck(var2):
            _subval = int(var2) - self.DecVal
        else:
            _subval = var2.DecVal - self.DecVal
        return _subval


    def __mul__(self, var2):
        if _inputtednonnumvaltypecheck(var2):
            _subval = self.DecVal * int(var2)
        else:
            _subval = self.DecVal * var2.DecVal
        return _subval

    def __rmul__(self, var2):
        if _inputtednonnumvaltypecheck(var2):
            _subval = self.DecVal * int(var2)
        else:
            _subval = self.DecVal * var2.DecVal
        return _subval

    
    def __div__(self, var2):
        if _inputtednonnumvaltypecheck(var2):
            _subval = self.DecVal/ int(var2)
        else:
            _subval = self.DecVal / var2.DecVal
        return _subval

    def __rdiv__(self, var2):
        if _inputtednonnumvaltypecheck(var2):
            _subval = int(var2) / self.DecVal
        else:
            _subval = var2.DecVal / self.DecVal
        return _subval


    def __str__(self):
        return str(self.DecVal)



    def ToDec(self):
        return self.DecVal


    def _toDec(self, _numval):
        _decnum = 0
        for i in range(len(str(_numval))):
            if _numval[i].lower() in _alphabet:
                for x in range(26):
                    if _numval[i].lower() == _alphabet[x]:
                        _numeraltotal = x + 11
                        print("pass")
                        break
            else:
                for x in range(10):
                    if _numval[i] == _numerals[x]:
                        _numeraltotal = x
                        break
            
            _decnum += _numeraltotal * self.ValType ** (len(str(_numval)) - i - 1)
        return _decnum

    def ToType(self, base):
        _valtypecheck(base)
        returnnum = ""
        _decval = self.DecVal
        while _decval > (base - 1):
            index = 1
            while (_decval / (base ** index) ) > base:
                index += 1

            _roundedresult = round(_decval / (base ** index))
            if isinstance(_roundedresult, int):
                returnnum = returnnum + str(_roundedresult)
            else:
                returnnum = returnnum + _alphabet[_roundedresult - 10]
            _decval = _decval % (base ** index)
        returnnum = returnnum + str(_decval)
        return returnnum
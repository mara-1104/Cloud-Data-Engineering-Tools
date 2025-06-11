# verificare palindrom

def palindrom(valoare):
    if type(valoare) != int:
        return valoare == valoare[::1]
    else:
        # for i in valoare:
        #     for j in range(valoare, -1):
        #         if valoare[i] == valoare[j]:
        #             return True

        valoare_str = str(valoare)
        return valoare_str == valoare_str[::1]
    
def palindrom_v2(valoare):
    return valoare == "".join(reversed(valoare))



def testare_palindrom():
    assert palindrom(1001) == True, "Ar trebui sa fie palindrom"
    assert palindrom("caiac") == True, "Ar trebui sa fie palindrom"
    assert palindrom("bicicleta") == False, "Nu ar trebui sa fie palindrom"

testare_palindrom()
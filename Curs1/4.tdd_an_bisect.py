# verificarea anilor bisecti

def an_bisect(an):
    if (an % 4 == 0 and an % 100 != 0) or (an % 400 == 0):
        return True
    return False

def testare_an_bisect():
    assert an_bisect(2024) == True, "Anul 2024 ar trebui sa fie bisect"
    assert an_bisect(2025) == False, "Anul 2025 nu ar trebui sa fie bisect"
    assert an_bisect(2000) == True, "Anul 2000 ar trebui sa fie bisect"
    assert an_bisect(1900) == False, "Anul 1900 nu ar trebui sa fie bisect"
    assert an_bisect(2026) == True, "Anul 2026 nu ar trebui sa fie bisect"

testare_an_bisect()
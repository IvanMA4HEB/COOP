class Test:
    prikol = 'cyka'
    spisok = []
    chislo = int()
    def __init__(self):
        self.prikol = 'cyka'
        self.spisok = []
        self.chislo = int()
    
    def zhoska(self):
        val = int(input('inp'))
        if val == (0):
            self.chislo = val
        elif val == (1):
            self.chislo = val
            
    def testik_aga(self):
        if self.chislo == (0):
            pass
            self.spisok.append(self.prikol)
        elif self.chislo == (1):
            self.spisok.append(self.prikol)
    
    def vivod_blyat(self):
        print(self.spisok)
            
test = Test()
test.zhoska()
test.testik_aga()
test.vivod_blyat()
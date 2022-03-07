class My_math:
    def __init__(self, x):
        self.x = x
        #self.y = y

    def factoriel(self):
    
        fact = 1 
        for i in range(1, self.x + 1):
            fact *= i
        print(fact)




m = My_math(5)
m.factoriel()
        
        
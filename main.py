class My_math:
    
    def factoriel(self, x):
    
        fact = 1 
        for i in range(1, x + 1):
            fact *= i
        print(fact)

    def addition(self, x ,y):
        print(x + y)


m = My_math()
m.factoriel(5)
m.addition(5,5)
        
        
class Adder:
    def __init__(self): 
        self.total = 0
    
    def __call__(self, value):
        if not isinstance(value, int):
            raise ValueError("ERRORE!")
        
        self.total += value
        return self
    
    def result(self):
        return self.total
    
add = Adder()
result = add(5)(3)(2).result()  
print(result)


class Geeks: 
     def __init__(self): 
          self._age = 0
       
     
     def get_age(self): 
         print("Método getter chamado") 
         return self._age 
       
     
     def set_age(self, a): 
         print("Método setter chamado") 
         self._age = a 
  
     
     age = property(get_age, set_age)  
  
mark = Geeks() 
  
mark.age = 10
  
print(mark.age)

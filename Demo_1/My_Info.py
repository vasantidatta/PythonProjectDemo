class My_Info:
        
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def function(self):
        
        print("My name is "+self.name)
        
    def function1(self):    
        print("My current age is ",self.age)
        
obj = My_Info ("vasanti",36)
obj.function()
obj.function1()
    
      
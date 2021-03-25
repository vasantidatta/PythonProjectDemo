class Addition:
    
    def add1(self,x):
        print("Adding 1 to x value")
        return x+1
    
    def add2(self,x,y):
        print("Adding x and y")
        return x+y
    
    def add3(self,x,y,z):
        print("adding x ,y and z")
        return x+y+z
    
add = Addition()    
    
a = add.add1(1)
b = add.add2(2,3)
c = add.add3(4,5,6)

print(a+bin)
print(b)
print(c)


    
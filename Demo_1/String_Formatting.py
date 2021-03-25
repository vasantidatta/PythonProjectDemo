# String formatting]

str = " my name is {} and my age is{}  "
a = " my "
d = " love"
b = 82
c = "my lucky number is {}"

print(str.format("vasanti"," 36" ))

print("hello, my name is {} and my wife is {}".format("datta","vasanti"))

print("where there is a {1} , there is a {0}".format("way","love"))

print("%s name is vasanti and %s roll no is %d" %(a,a,b))

print(c.format(b))


'''print(type(a))


print(str.strip())'''


print("nothing in the {} can trouble {} as much as {} own {}".format("world","you","your","thoughts"))

print("{2} comes {1} in this {0}...!".format("world","free","Nothing"))

# Escape characters :- allows us to insert illegal strings in another string

print("what goes \"around\" comes \"around.\"")

print("\"jelousy\" is hell, \"love\" is heaven.")

print(a*4)
print(d*4)

if (b==82):
    print("may roll number is %d" %(b))
    
def age():
    x=44
    print("my age is {} ".format(36)) 
    print("my datta is %d years old" %x)
    print("datta age is ",x)
    
age() 


    
    
       
    














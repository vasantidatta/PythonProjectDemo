class Employe_Info:
    
    def __init__(self,fname,lname,empid):
        
        self.fname = fname
        self.lname = lname
        self.empid = empid
        
    def information(self):
        
        print("Employe's firstname = "+self.fname+", "+"Employe's lastname = "+self.lname)
       # print("Employe's last name = "+self.lname)
        print("Employe's id = ",self.empid)
        
obj1 = Employe_Info("sam","paul",11091)
obj2 = Employe_Info("kamala","harris",11092)
obj3 = Employe_Info("joe","beaden",11093)

obj1.information()
obj2.information()
obj3.information()
       
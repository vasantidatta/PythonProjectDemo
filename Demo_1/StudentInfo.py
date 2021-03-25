class studentInfo:
    def __init__(self,stname,stid):
        self.stname=stname
        self.stid=stid
    def information(self):
        print("student name is  "+self.stname)
        print("student Id is ",self.stid)
st1 = studentInfo("vasanti",82)
st2 = studentInfo("datta",83)
st3 = studentInfo("shreesh",84)
st1.information()
st2.information()
st3.information()        
        
        
        
        
                
        
        
        
# list sorting

class ListSorting:
    
    Names = ['seema','riya','diya','sita','geeta','hema']    
    List = [20,22,25,36,38,42,46]
    NewList = []
    names = []
    names1 = []
    ''' Below code returns list of all numbers less than 30 '''    
    for x in List:
        if x>=30:
             
            NewList.append(x)
            NewList.sort()
            NewList.reverse()         
    print("NewList = ",NewList)
    ''' Below code returns all strings having 'i' in them'''
    for x in Names:
        if 'i' in x:
            names.append(x)
            names.sort()   
    print("names having i = ",names)  
    ''' Below code gives the output as all strings containing 'e' in them'''
    for x in Names:
        if 'e' in x:
            names1.append(x)
            names1.sort(reverse=True)
    
    print("names having e = ",names1)                  
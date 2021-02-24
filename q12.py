#Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
#print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
#print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]

def reverse_list(l):
    l1=[]
    for i in range(len(l)-1,-1,-1):
        l1.append(l[i])
    return l1    
        
    
print(reverse_list([12,13,14,15,16]))
  
        
    

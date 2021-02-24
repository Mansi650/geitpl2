#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

fruits = ['banana', 'orange', 'mango', 'lemon']
new_list = []
for i in range(len(fruits)-1,-1,-1):
    new_list.append(fruits[i])

print(fruits)
print(new_list)    
    

#Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_items(l):
    l1 = []
    for i in l:
        j = i.capitalize()
        l1.append(j)
    return l1

print(capitalize_list_items(["apple",'mango','orange','banana']))
    

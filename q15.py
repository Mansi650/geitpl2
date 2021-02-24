#Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
#food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
#print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
#numbers = [2, 3, 7, 9];
#print(remove_item(numbers, 3))  # [2, 7, 9]

def remove_item(l,s):
    l.remove(s)
    return l

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff,'Mango'))

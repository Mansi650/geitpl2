#Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
#print(sum_of_numbers(5))  # 15
#print(sum_all_numbers(10)) # 55
#print(sum_all_numbers(100)) # 5050

def sum_of_numbers(n):
    sum = 0
    for i in range(n+1):
        sum = sum+i
    return sum    

print(sum_of_numbers(10))

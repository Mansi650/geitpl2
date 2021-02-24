#Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

def sum_of_odds(n):
    sum = 0
    for i in range(n+1):
        if i%2!=0:
            sum = sum+i
    return sum

print(sum_of_odds(10))

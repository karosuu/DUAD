
def prime_number(number):   
    if number <=1:
        return False  
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
    
            
numbers_list = [1, 4, 6, 7, 13, 9, 67]

new_numbers = []

for number in numbers_list:
    if prime_number(number):
        new_numbers.append(number)
    
print(new_numbers)




    
    
    
    
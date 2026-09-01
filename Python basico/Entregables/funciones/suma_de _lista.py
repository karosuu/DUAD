def numbers_addition(numbered_list):
    total_sum = 0 
    for  number in numbered_list:
        total_sum += number
    return total_sum

def main():
    numbered_list = [28, 30, 56]
    sum_result  = numbers_addition(numbered_list)
    print(f"La suma de los numeros de la lista  es: {sum_result}")
    
if __name__ == "__main__":
    main()
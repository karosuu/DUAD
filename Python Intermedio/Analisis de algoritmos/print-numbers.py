def print_numbers_times_2(numbers_list):
    for number in range(len(numbers_list)):

        print(numbers_list[number] * 2)

    return numbers_list

numbers = [1, 2, 3, 4, 5]
print_numbers_times_2(numbers)

def is_even(number):
    if (number % 2 == 0):
        return True
    else:
        return False

# # is_even (1)
# # print(is_even (1))

# def is_odd(number):
#     return not is_even(number)
    
# is_number_even = is_odd(int(input('Please enter a number: ')))

# if is_number_even:
#     print('The number is odd.')
# else:
#     print('The number is even.')


def only_evens(list_of_nums):
    new_list = []

    for number in list_of_nums:
    #check if number is even
        if is_even(number):
        #if yes, store in new list
            new_list.append(number)


    return new_list

numbers_to_check = [2, 123, 96, 123, -2221, 58, 42, 77, 33]
even_numbers = only_evens(numbers_to_check)
print (even_numbers)
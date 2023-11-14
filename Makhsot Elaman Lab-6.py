# Task 1
#1.1
# def get_keys_with_value_true(input_dict):
#     return [key for key, value in input_dict.items() if value]
#
# # Example usage:
# input_dict = {
#     "a": True,
#     "b": False,
#     "c": True,
# }
#
# result = get_keys_with_value_true(input_dict)
# print(result)
#1.2
# def get_unique_elements(input_list):
#     unique_elements = [element for element in input_list if input_list.count(element) == 1]
#     return unique_elements
#
# # Example usage:
# input_list = [1, 2, 3, 1, 2, 4]
# result = get_unique_elements(input_list)
# print(result)
#1.3
# def get_date_in_format(input_date):
#     year, month, day = map(int, input_date.split('.'))
#     formatted_date = f"{day:02d}.{month:02d}.{year}"
#     return formatted_date
#
# # Example usage:
# input_date = "2023.10.23"
# result = get_date_in_format(input_date)
# print(result)
#1.4
#1.5
# def get_words_from_string(input_string):
#     words = input_string.split()
#     return words
#
# # Example usage:
# input_string = "This is a string with several words."
# result = get_words_from_string(input_string)
# print(result)
#Task 2
#2.1
#2.2
# def get_prime_numbers(n):
#     primes = []
#
#     for num in range(2, n + 1):
#         is_prime = True
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(num)
#
#     return primes
#
#
# # Example usage:
# n = 100
# result = get_prime_numbers(n)
# print(result)
#2.3
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# def get_prime_numbers_in_list(input_list):
#     primes = [num for num in input_list if is_prime(num)]
#     return primes
#
# # Example usage:
# input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 27, 36, 48, 54, 67, 71, 73, 75, 83, 89, 99]
# result = get_prime_numbers_in_list(input_list)
# print(result)
#2.4
#
# from datetime import datetime
#
# def get_difference_between_dates(date_str1, date_str2):
#     date_format = "%Y.%m.%d"
#     date1 = datetime.strptime(date_str1, date_format)
#     date2 = datetime.strptime(date_str2, date_format)
#
#     difference = abs((date2 - date1).days)
#     return difference
#
# # Example usage:
# date1 = "2023.10.23"
# date2 = "2023.10.25"
# result = get_difference_between_dates(date1, date2)
# print(result)
#Task 3
#3.1
#3.2
# def are_all_perfect_squares(numbers):
#     for num in numbers:
#         if not is_perfect_square(num):
#             return False
#     return True
#
# def is_perfect_square(num):
#     return num > 0 and int(num**0.5)**2 == num
#
# # Example usage
# input_numbers = [4, 25, 81]
# output = are_all_perfect_squares(input_numbers)
# print(output)
#3.3
# def sort_by_price(shopping_list):
#     return sorted(shopping_list, key=lambda x: x["price"])
#
# # Example usage
# input_shopping_list = [
#     {"name": "Apple", "price": 100},
#     {"name": "Banana", "price": 50},
#     {"name": "Orange", "price": 20}
# ]
#
# output = sort_by_price(input_shopping_list)
# print(output)
#3.4
# def get_words_starting_with_vowel(words):
#     vowels = set("aeiouAEIOU")
#     return [word for word in words if word[0] in vowels]
#
# # Example usage
# input_words = ["apple", "banana", "orange", "bear", "cat"]
# output = get_words_starting_with_vowel(input_words)
# print(output)



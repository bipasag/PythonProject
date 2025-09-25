
def remove_odds(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]  # keep only even numbers
    return even_numbers


def main():
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # example list
    new_list = remove_odds(original_list)
    print("Original list:", original_list)
    print("Even numbers only:", new_list)

main()

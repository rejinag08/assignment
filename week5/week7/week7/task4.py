def remove_uneven(numbers):
    return [num for num in numbers if num % 2 == 0]

def main_remove_uneven_test():
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even_list = remove_uneven(original_list)

    print(f"Original list: {original_list}")
    print(f"List with uneven numbers removed: {even_list}")

main_remove_uneven_test()
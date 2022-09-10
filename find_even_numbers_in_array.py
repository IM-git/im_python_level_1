def find_even_numbers_in_array(array: list) -> None:
    answer = []
    for num in array:
        if isinstance(num, int or float) and num % 2 == 0:
            answer.append(num)
    print(f"Even numbers: {' '.join(map(str, answer))}")


if __name__ == '__main__':
    find_even_numbers_in_array([1, 2, 4, 55, 66, 3, 55])
    find_even_numbers_in_array([])
    find_even_numbers_in_array([1, 2, 98, 99, 100, 0, -4, -888, -1, -0, 'a'])
    find_even_numbers_in_array([True, 'X', {1, 2, 3, 4, 55}, [2, 4, 8, 16]])

def find_value_in_array(value, array: list) -> None:
    if value in array:
        print(f"The value: {value}, index: {array.index(value)}")
    else:
        print(f"Sorry, the value:{value} is not in the array.")


if __name__ == '__main__':
    find_value_in_array('x', ['a', 1, True, 0.07, 1 / 3, 'x', {1, 2, '#404'}])
    find_value_in_array('', [])
    find_value_in_array(1, [2, 11, 111, 1111, 0.1, 999, 'AAA', '"'])
    find_value_in_array(True, [False, True, '', 00])
    find_value_in_array('text',
                        [['text', 'this is python!!!'],
                         ['text', 1234], ('text', len(['888'])),
                         {8, 7, 6}])
    find_value_in_array('qwerty', ['qwertyu', 'q', 'qwerty', 'hello world'])
    
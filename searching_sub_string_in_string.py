def searching_sub_string_in_string(sub_string: str, string: str) -> None:
    print(string.find(sub_string))


if __name__ == '__main__':
    searching_sub_string_in_string('seven', 'eight seven six five')
    searching_sub_string_in_string('four', 'eight seven six five')
    searching_sub_string_in_string('x', 'eight seven six five')
    searching_sub_string_in_string('', '')
    searching_sub_string_in_string('-', '][][][][ ]  +++-**+')
    searching_sub_string_in_string('\n', '][][][][ ]  +++-**+\n')
    searching_sub_string_in_string('\n', '][][][][ ]  +++-**+')

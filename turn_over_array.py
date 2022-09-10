from turn_over_values import TurnOverValues


class TurnOverArray(TurnOverValues):
    pass


if __name__ == '__main__':
    print(TurnOverArray([1, 2, 3, 4, 5, 6, 7]).turn_over_slice())
    print(TurnOverArray([1, 2, 3, 4, 5, 6, 7]).turn_over_standard())
    print(TurnOverArray([1, 2, 3, 4, 5, 6, 7]).turn_over_reversed())

    print(TurnOverArray([0, 2, 0, 4]).turn_over_slice())
    print(TurnOverArray([0, 2, 0, 4]).turn_over_standard())
    print(TurnOverArray([0, 2, 0, 4]).turn_over_reversed())

    print(TurnOverArray([1, 2, 'x', 4]).turn_over_slice())
    print(TurnOverArray([1, 2, 'x', 4]).turn_over_standard())
    print(TurnOverArray([1, 2, 'x', 4]).turn_over_reversed())

    print(TurnOverArray(
        ['xiaomi', 'samsung', 'apple', 'vivo']).turn_over_slice())
    print(TurnOverArray(
        ['xiaomi', 'samsung', 'apple', 'vivo']).turn_over_standard())
    print(TurnOverArray(
        ['xiaomi', 'samsung', 'apple', 'vivo']).turn_over_reversed())

    print(TurnOverArray([]).turn_over_slice())
    print(TurnOverArray([]).turn_over_standard())
    print(TurnOverArray([]).turn_over_reversed())

    print(TurnOverArray([True, False]).turn_over_slice())
    print(TurnOverArray([True, False]).turn_over_standard())
    print(TurnOverArray([True, False]).turn_over_reversed())

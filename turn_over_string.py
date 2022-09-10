from turn_over_values import TurnOverValues


class TurnOverString(TurnOverValues):
    pass


if __name__ == '__main__':
    print(TurnOverString(
        'ASDASasdasASD 544as TRqwerty').turn_over_slice())
    print(''.join(TurnOverString(
        'ASDASasdasASD 544as TRqwerty').turn_over_standard()))
    print(''.join(TurnOverString(
        'ASDASasdasASD 544as TRqwerty').turn_over_reversed()))

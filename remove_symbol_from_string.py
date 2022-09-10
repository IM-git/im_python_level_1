class RemoveSymbolFromString:

    def __init__(self, symbol: str, string: str):
        self.symbol = symbol
        self.string = string

    def remove_using_replace(self) -> str:
        return self.string.replace(self.symbol, '')

    def remove_standard_method(self) -> str:
        return ''.join(
            [value for value in self.string if value != self.symbol])


if __name__ == '__main__':
    print(RemoveSymbolFromString('x', 'xljsakdxldsasdXsadx1').
          remove_using_replace())
    print(RemoveSymbolFromString('x', 'xljsakdxldsasdXsadx1').
          remove_standard_method())

    print(RemoveSymbolFromString('0', 'XXXXXssssssssss@@@').
          remove_using_replace())
    print(RemoveSymbolFromString('0', 'XXXXXssssssssss@@@').
          remove_standard_method())

    print(RemoveSymbolFromString('*', '').
          remove_using_replace())
    print(RemoveSymbolFromString('*', '').
          remove_standard_method())

    print(RemoveSymbolFromString('1', 'xljsakdxldsasdXsadx1').
          remove_using_replace())
    print(RemoveSymbolFromString('1', 'xljsakdxldsasdXsadx1').
          remove_standard_method())

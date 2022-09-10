def quantity_symbols_to_string(string: str) -> None:
    print(len(string))


if __name__ == '__main__':
    quantity_symbols_to_string('')
    quantity_symbols_to_string('    ')
    quantity_symbols_to_string('\t\t\t')
    quantity_symbols_to_string('\n\n\n')
    quantity_symbols_to_string('123456')
    quantity_symbols_to_string('kgzgsglaflgslkal')
    quantity_symbols_to_string('KGZGSGLAFLGSLKAL')
    quantity_symbols_to_string('kl ljl  aljja ajkl+-+ 1 14%')
    quantity_symbols_to_string('[][][]00000    \n\n\n\n')
    quantity_symbols_to_string(f'{1}111{123}')
    quantity_symbols_to_string(f'{1}111{12}')
    quantity_symbols_to_string(f'{True}')

def bubble_sort(array: list):
    try:
        for step in range(len(array)-1):
            for number in range(len(array) - step - 1):
                if array[number] > array[number+1]:
                    array[number], array[number+1] = array[number+1],\
                                                     array[number]
        print(*array)
    except TypeError:
        print("This list doesn't consist only of numbers(int|float)")


if __name__ == '__main__':
    bubble_sort([3, 22, 1, 11, 15, 5])
    bubble_sort(['3', '22', '1', '11', '15', '5'])
    bubble_sort([55, 2, 2, 1, 11, 1, 55, 11])
    bubble_sort([55.5, 2, 2.2, 1, 11, 1.1, 55, 11])
    bubble_sort([55, 2, "", 1, 11, 1, 55, 11])
    bubble_sort([1])
    bubble_sort([""])
    bubble_sort([[], {}, ()])
    bubble_sort([int, float, str])
    bubble_sort([0, 0, 0, 0])
    bubble_sort([2, -1, 0, -8])

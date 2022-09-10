class TransportMatrix:

    def __init__(self, array: list):
        self.array = array

    def transport_with_zip(self):
        [print(list(value)) for value in zip(*self.array)]

    def transport_standard(self):
        answer = []
        for i in range(len(self.array[0])):
            answer.append([])
            for j in range(len(self.array)):
                answer[i].append(self.array[j][i])
        print(answer)


if __name__ == '__main__':
    TransportMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).transport_with_zip()
    TransportMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).transport_standard()

    TransportMatrix([[1, 2, 3], [7, 8, 9]]).transport_with_zip()
    TransportMatrix([[1, 2, 3], [7, 8, 9]]).transport_standard()

    TransportMatrix([[0, 2, 4], [3, 'x', 6]]).transport_with_zip()
    TransportMatrix([[0, 2, 4], [3, 'x', 6]]).transport_standard()

    TransportMatrix([[0], [3]]).transport_with_zip()
    TransportMatrix([[0], [3]]).transport_standard()

    TransportMatrix([[], []]).transport_with_zip()
    TransportMatrix([[], []]).transport_standard()

    TransportMatrix([[]]).transport_with_zip()
    TransportMatrix([[]]).transport_standard()

    TransportMatrix([[0, 1], [3, 77]]).transport_with_zip()
    TransportMatrix([[0, 1], [3, 77]]).transport_standard()

    TransportMatrix([[0, 1, 3, 5, 6],
                     [3, 7, 88, 9, 0],
                     [11, 13, 32, 7, 98],
                     [11, 111, 22, 45, 65]]).transport_with_zip()
    TransportMatrix([[0, 1, 3, 5, 6],
                     [3, 7, 88, 9, 0],
                     [11, 13, 32, 7, 98],
                     [11, 111, 22, 45, 65]]).transport_standard()

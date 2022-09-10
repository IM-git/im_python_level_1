class TurnOverValues:

    def __init__(self, values: list | str):
        self.values = values

    def turn_over_slice(self):
        return self.values[::-1]

    def turn_over_standard(self):
        answer = []
        for x in self.values:
            answer.insert(0, x)
        return answer

    def turn_over_reversed(self):
        return list(reversed(self.values))

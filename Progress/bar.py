import math

class Bar:
    length = 30
    completed_sign = '='
    head_sign = '>'
    rest_sign = '.'
    borders = ('[', ']')
    separator = '/'

    def __init__(self, iterations: int):
        self.iterations = iterations
        self.i = 0

        if self.iterations >= self.length:
            self.step = self.iterations / self.length
        else:
            self.step = self.length / self.iterations

        self.clear_length = 0
        self.completed_length = 0

    def next(self):
        self.i += 1

        self.completed_length = math.ceil(self.i / self.iterations * self.length)

        self.rest_length = self.length - self.completed_length

        rest = "." * self.rest_length
        counter = str(self.i) + '/' + str(self.iterations)
        percent = int(self.i / self.iterations * 100)
        completed = "=" * (self.completed_length - 1)

        if (self.completed_length - 1 >= 0):
            if (self.completed_length < self.length):
                completed += '>'
            else:
                completed += '='

        to_clear = '\b' * self.clear_length

        text = f'{counter} [{completed}{rest}] {percent}%'
        self.clear_length = len(text) + 1
        print(to_clear + text)
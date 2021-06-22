class List_integer:
    def __init__(self, integer):
        if isinstance(integer, List_integer):
            self.integer = integer.integer[:]
        else:
            self.integer = [int(char) for char in str(integer)]

    def print(self):
        print(self.integer)

    def repair(self):
        for index in range(len(self.integer) - 1, 0, -1):
            if self.integer[index] >= 10:
                self.integer[index - 1] += int(self.integer[index] / 10)
                self.integer[index] %= 10
            else:
                while self.integer[index] < 0:
                    self.integer[index] += 10
                    self.integer[index - 1] -= 1
        if self.integer[0] < 0:
            raise
        if self.integer[0] == 0:
            while self.integer[0] == 0 and len(self.integer) > 1:
                self.integer.pop(0)
        if self.integer[0] >= 10:  # just first one remains
            x = self.integer[0]
            self.integer[0] = x % 10
            x = int(x / 10)
            while x:
                self.integer.insert(0, x % 10)
                x = int(x / 10)

    def add(self, another_list_integer):
        if len(another_list_integer.integer) > len(self.integer):
            for index in range(1, len(self.integer) + 1):
                self.integer[-index] += another_list_integer.integer[-index]
            for index in range(len(another_list_integer.integer) - len(self.integer) - 1, -1, -1):
                self.integer.insert(0, another_list_integer.integer[index])
        else:
            for index in range(1, len(another_list_integer.integer) + 1):
                self.integer[-index] += another_list_integer.integer[-index]

        self.repair()

    def subtract(self, another_list_integer):
        if len(another_list_integer.integer) > len(self.integer) or another_list_integer.value() > self.value():
            raise
        for index in range(1, len(another_list_integer.integer) + 1):
            self.integer[-index] -= another_list_integer.integer[-index]
        self.repair()

    def value(self):
        strings = [str(integer) for integer in self.integer]
        a_string = "".join(strings)
        return int(a_string)

    def multiply(self, another_list_integer_or_just_integer):
        if isinstance(another_list_integer_or_just_integer, List_integer):
            x = another_list_integer_or_just_integer.value()
        else:
            x = another_list_integer_or_just_integer
        for index in range(len(self.integer)):
            self.integer[index] *= x

        self.repair()


if __name__ == "__main__":

    def right(total_space, string):
        string = str(string)
        print(' ' * (total_space - len(string)) + string)

    def print_adding(value_1, value_2):
        x = List_integer(value_1)
        y = List_integer(value_2)
        z = List_integer(value_1)
        z.add(y)

        if max(len(z.integer), len(x.integer), len(y.integer)) == len(y.integer):
            total = len(y.integer) + 1
        else:
            total = len(z.integer)

        right(total, value_1)
        right(total, '+' + str(value_2))
        print('-' * total)
        right(total, z.value())
        print()

    def print_subtracting(value_1, value_2):
        x = List_integer(value_1)
        y = List_integer(value_2)
        z = List_integer(value_1)
        z.subtract(y)

        if max(len(z.integer), len(x.integer), len(y.integer)) == len(y.integer):
            total = len(y.integer) + 1
        else:
            total = len(x.integer)

        right(total, value_1)
        right(total, '-' + str(value_2))
        right(total, '-' * max(len(y.integer) + 1, len(z.integer)))
        right(total, z.value())
        print()

    def print_multiplication(value_1, value_2):
        x = List_integer(value_1)
        y = List_integer(value_2)
        z = List_integer(x)
        z.multiply(y)

        if len(y.integer) == 1:
            total = max(len(x.integer), len(y.integer) + 1, len(z.integer))
            midway = max(len(y.integer) + 1, len(z.integer))
            right(total, value_1)
            right(total, '*' + str(value_2))
            right(total, '-' * midway)
            right(total, z.value())
        else:
            lengths = [len(x.integer), len(y.integer) + 1]
            my_list = []
            for index in range(len(y.integer)):
                my_list.append(List_integer(x))
                my_list[-1].multiply(y.integer[-(index+1)])
                lengths.append(len(my_list[-1].integer) + index)
            lengths.append(len(z.integer))
            total = max(lengths)
            right(total, value_1)
            right(total, '*' + str(value_2))
            right(total, '-' * max(lengths[1], lengths[2]))
            for index in range(len(y.integer)):
                right(total, str(my_list[index].value()) + ' ' * index)
            right(total, '-' * max(lengths[-2], lengths[-1]))
            right(total, z.value())
        print()

    for _ in range(int(input())):
        s = input()
        for index, token in enumerate(s):
            if not token.isnumeric():
                x = s[:index]
                y = s[index + 1:]
                if token == '+':
                    print_adding(int(x), int(y))
                elif token == '-':
                    print_subtracting(int(x), int(y))
                elif token == '*':
                    print_multiplication(int(x), int(y))
                break
        # x.multiply(y)
        # x.print()
        # print(x.value())

    # print_multiplication(x.value(), y.value())

"""
      123451234567890
                  *99
     ----------------
     1111061111111010
    1111061111111010
    -----------------
    12221672222221110
"""
    # for i in range(int(input())):
    #     s = input()
    #     num = [int(char) for char in s]
    #     n = len(num)
    #     generateNextPalindrome(num, n)


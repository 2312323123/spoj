# algorithm: https://en.wikipedia.org/wiki/Shunting-yard_algorithm
repeats = int(input())
for repeat in range(repeats):
    my_string = list(input())
    # my_string = '(a+b)*C'
    output = ''
    operators = []
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3,
        '(': 4,
        ')': 5
    }
    for token in my_string:
        if token.isalpha():  # number
            output += token
        elif token != '(' and token != ')':  # operator
            while len(operators) and (
                    precedence[operators[-1]] > precedence[token] or
                    precedence[operators[-1]] == precedence[token] and token != '^'
                    ) and (operators[-1] != '('):
                output += operators.pop(-1)
            operators.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators[-1] != '(':
                output += operators.pop(-1)
            if operators[-1] == '(':
                operators.pop(-1)
    while len(operators):
        output += operators.pop(-1)
    print(output)

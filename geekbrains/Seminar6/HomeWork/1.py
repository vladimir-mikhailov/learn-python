# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.

# Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

# Добавьте возможность использования скобок, меняющих приоритет операций.
# Пример:
# 1+2*3 => 7;
# (1+2)*3 => 9;

def split_to_lexemes(problem: str):
    problem = problem.replace(' ', '')
    lexemes = []
    acc = ''
    for char in problem:
        if char.isdigit() or char == '.':
            acc += char
        elif acc != '':
            lexemes.append(acc)
            lexemes.append(char)
            acc = ''
        else:
            lexemes.append(char)
    if acc != '':
        lexemes.append(acc)
    return lexemes


def solve(problem):
    if problem == []:
        return []

    if type(problem) == str:
        problem = split_to_lexemes(problem)

    if '(' in problem:
        begin = problem.index('(') + 1
        end = problem.index(')')
        if begin - 1 == 0:
            left = []
        else:
            left = problem[:begin - 1]
        if end == len(problem) - 1:
            right = []
        else:
            right = problem[end + 1:]
        return solve(left + solve(problem[begin:end]) + right)

    for operator in ['*', '/', '+', '-']:
        if operator in problem:
            i = problem.index(operator)
            left = problem[:i - 1]
            right = problem[i + 2:]
            operand_left = float(problem[i - 1])
            operand_right = float(problem[i + 1])

            match operator:
                case '*':
                    if len(problem) > 3:
                        return solve(left + [operand_left * operand_right] + right)
                    return [operand_left * operand_right]
                case '/':
                    if len(problem) > 3:
                        return solve(left + [operand_left / operand_right] + right)
                    return [operand_left / operand_right]
                case '+':
                    if len(problem) > 3:
                        return solve(left + [operand_left + operand_right] + right)
                    return [operand_left + operand_right]
                case '-':
                    if len(problem) > 3:
                        return solve(left + [operand_left - operand_right] + right)
                    return [operand_left - operand_right]


problem = '(1 + 1 + 2) * 3 + 12 / (2 * 2 + 1 + 1)'  # = 14
problem1 = '(1+2)*3'
problem2 = '1+2*3'

print(problem, '=', *solve(problem))
print(problem1, '=', *solve(problem1))
print(problem2, '=', *solve(problem2))

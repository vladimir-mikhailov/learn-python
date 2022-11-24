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

import re


def split_to_lexemes(problem: str):
    problem = problem.replace(' ', '')
    lexemes = []
    acc = ''
    for char in problem:
        if char.isdigit() or char == '.':
            acc += char
        elif acc:
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

    if isinstance(problem, str):
        problem = split_to_lexemes(problem)

    if '(' in problem:
        problem_str = ''.join([str(s) for s in problem])
        span = re.search(r"\(([0-9_+\-\./* ]+)\)", problem_str).span()
        begin = span[0] + 1
        end = span[1] - 1

        if begin - 1 == 0:
            left = ''
        else:
            left = problem_str[:begin - 1]

        if end == len(problem_str) - 1:
            right = ''
        else:
            right = problem_str[end + 1:]
        return solve(left + ''.join([str(s) for s in solve(problem_str[begin:end])]) + right)

    for operator in ['/', '*', '+', '-']:
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


# problem = '2*10/2 + (1 + (1 + (2 + 1))) * 3 + 12 / (2 * 2 + 1 + 1)'  # = 17
# problem = '1 + 1 + 2 + 1 * 3 + 12 / 2 * 2 + 1 + 1'
# problem1 = '(1+2)*3'
# problem2 = '1+2*3'

# print(problem, '=', *solve(problem))
# print(problem1, '=', *solve(problem1))
# print(problem2, '=', *solve(problem2))

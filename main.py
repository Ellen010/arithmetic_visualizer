def arithmetic_arranger(problems, display_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    first_operands = []
    second_operands = []
    operators = []
    answers = []
    arranged_problems = []
    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Incorrect problem format."
        first_operand, operator, second_operand = parts
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        if not first_operand.isdigit() or not second_operand.isdigit():
            return "Error: Numbers must only contain digits."
        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."
        first_operands.append(first_operand)
        second_operands.append(second_operand)
        operators.append(operator)
        if display_answers:
            if operator == '+':
                answers.append(str(int(first_operand) + int(second_operand)))
            else:
                answers.append(str(int(first_operand) - int(second_operand)))
    first_line = ''
    second_line = ''
    dashes = ''
    answer_line = ''
    for i in range(len(problems)):
        width = max(len(first_operands[i]), len(second_operands[i])) + 2
        first_line += first_operands[i].rjust(width) + '    '
        second_line += operators[i] + second_operands[i].rjust(width - 1) + '    '
        dashes += '-' * width + '    '
        if display_answers:
            answer_line += answers[i].rjust(width) + '    '
    if display_answers:
        arranged_problems = f"{first_line.rstrip()}\n{second_line.rstrip()}\n{dashes.rstrip()}\n{answer_line.rstrip()}"
    else:
        arranged_problems = f"{first_line.rstrip()}\n{second_line.rstrip()}\n{dashes.rstrip()}"
    return arranged_problems
print(f"\n{arithmetic_arranger(['32 + 698', '3801 - 2', '45 + 43', '123 + 49'])}")
print(f"\n{arithmetic_arranger(['32 + 8', '1 - 3801', '9999 + 9999', '523 - 49'], True)}")

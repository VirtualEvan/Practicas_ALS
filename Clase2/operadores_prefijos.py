def evaluate(all):
    """
    Evaluete expressions with prefix operands
    :param l: A given list whit to operands for each operator
    :return: Result number of eval
    """
    def is_operator(op):
        """
        Determinate if is a string is operator or not
        :param op: A string operand/operator
        :return: True if operator, False otherwise
        """
        return True if op in ['+', '-', '*', '/'] else False

    l = all[0]
    pos = all[1]

    if pos >= len(l):
        return -1

    operator = l[pos]
    pos += 1

    # Operator1
    if is_operator(operator):
        all[1] = pos
        print("Evaluar operador 1: ", l[1:])
        op1 = evaluate(all)
    else:
        op1 = l[pos]
        pos += 1


    # Operator2
    if is_operator(operator):
        all[1] = pos
        print("Evaluar operador 1: ", l[1:])
        op2 = evaluate(all)
    else:
        op2 = l[pos]
        pos += 1

    expression = op1 + operator + op2
    print(expression)

    return str(eval(expression))

l = "+ - 4 2 3".split()
# print("Expresion:", l)

# print("Resultado:", evaluate(l))

l = "+ 1 - 5 * 2 4".split()
# print("Expresion: ",l )

# print("Resultado:", evaluate(l))

exp = "+ - 4 * 6 1 8".split()
l = [exp, 0]
print("Expresion: ",l)

print("Resultado:", evaluate(l))

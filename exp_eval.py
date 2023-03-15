from stack_array import Stack


# You do not need to change this class
class PostfixFormatException(Exception):
    pass


def postfix_eval(input_str):
    '''Evaluates a postfix expression
    Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** >> << or numbers.
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed
    DO NOT USE PYTHON'S EVAL FUNCTION!!!'''
    lst = input_str.split()
    if len(lst) == 0:
        raise PostfixFormatException("Empty input")
    s = Stack(30)
    for item in lst:
        try:
            int(item)
            s.push(int(item))
        except ValueError:
            try:
                float(item)
                s.push(float(item))
            except ValueError:
                if item == '+':
                    if s.size() == 1:
                        raise PostfixFormatException("Insufficient operands")
                    n1 = s.pop()
                    n2 = s.pop()
                    s.push(n2 + n1)
                elif item == '-':
                    if s.size() == 1:
                        raise PostfixFormatException("Insufficient operands")
                    n1 = s.pop()
                    n2 = s.pop()
                    s.push(n2 - n1)
                elif item == '*':
                    if s.size() == 1:
                        raise PostfixFormatException("Insufficient operands")
                    n1 = s.pop()
                    n2 = s.pop()
                    s.push(n2 * n1)
                elif item == '/':
                    if s.size() == 1:
                        raise PostfixFormatException("Insufficient operands")
                    n1 = s.pop()
                    n2 = s.pop()
                    if n1 == 0:
                        raise ValueError
                    s.push(n2 / n1)
                elif item == '**':
                    if s.size() == 1:
                        raise PostfixFormatException("Insufficient operands")
                    n1 = s.pop()
                    n2 = s.pop()
                    s.push(n2 ** n1)
                elif item == '<<':
                    if s.size() == 1:
                        raise PostfixFormatException("Insufficient operands")
                    n1 = s.pop()
                    n2 = s.pop()
                    if type(n1) != int or type(n2) != int:
                        raise PostfixFormatException("Illegal bit shift operand")
                    s.push(n2 << n1)
                elif item == '>>':
                    if s.size() == 1:
                        raise PostfixFormatException("Insufficient operands")
                    n1 = s.pop()
                    n2 = s.pop()
                    if type(n1) != int or type(n2) != int:
                        raise PostfixFormatException("Illegal bit shift operand")
                    s.push(n2 >> n1)
                else:
                    raise PostfixFormatException("Invalid token")
    if not s.size() == 1:
        raise PostfixFormatException("Too many operands")
    else:
        return s.pop()


def infix_to_postfix(input_str):
    '''Converts an infix expression to an equivalent postfix expression
    Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << parentheses ( ) or numbers
    Returns a String containing a postfix expression '''

    rpn = ""
    lst = input_str.split()
    s = Stack(30)
    operators_l = ['+', '-', '*', '/', '<<', '>>']
    operators_r = ['**']
    operators_a = ['+', '-', '*', '/', '**', '<<', '>>']
    op_precedence = {'<<': 4, '>>': 4,
                     '**': 3,
                     '*': 2, '/': 2,
                     '+': 1, '-': 1}
    f_1 = False
    for item in lst:

        try:
            int(item)
            if len(input_str) == 1:
                rpn = rpn + item
            else:
                rpn = rpn + item + " "
        except ValueError:
            try:
                float(item)
                if len(input_str) == 3:
                    rpn = rpn + item
                else:
                    rpn = rpn + item + " "
            except ValueError:
                if item == '(':
                    s.push(item)
                elif item == ')':
                    temp = s.pop()
                    while not (temp == '(' or temp.isnumeric()):
                        rpn = rpn + temp + " "
                        temp = s.pop()
                elif item in operators_l:
                    while (not s.is_empty()) and (s.peek() in operators_a) and \
                                (op_precedence[item] <= op_precedence[s.peek()]):
                        rpn = rpn + s.pop() + " "
                    s.push(item)
                elif item in operators_r:
                    while (not s.is_empty()) and (s.peek() in operators_a) and \
                            (op_precedence[item] < op_precedence[s.peek()]):
                        rpn = rpn + s.pop() + " "
                    s.push(item)
    for i in range(s.size()):
        if s.size() == 1:
            rpn = rpn + s.pop()
        else:
            rpn = rpn + s.pop() + " "
    return rpn


def prefix_to_postfix(input_str):
    '''Converts a prefix expression to an equivalent postfix expression
    Input argument:  a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << or numbers
    Returns a String containing a postfix expression (tokens are space separated)'''
    # input_str = input_str[::-1]
    lst = input_str.split(" ")
    lst = lst[::-1]
    s = Stack(30)
    for item in lst:
        try:
            int(item)
            s.push(item)
        except ValueError:
            try:
                float(item)
                s.push(item)
            except ValueError:
                op1 = s.pop()
                op2 = s.pop()
                st = op1 + " " + op2 + " " + item
                s.push(st)
    return s.pop()

from calc import *
from copy import deepcopy


def eval_program(calc_prog, initVariables={}):
    """ Takes a calc program and runs it """
    if isprogram(calc_prog):
        dic = deepcopy(initVariables)
        return statements_mngr(program_statements(calc_prog), dic)
    else:
        print ("Input is not a calc program")


def statements_mngr(statements, in_dic):
    """ Recursive function that calls statement_mngr on the first statemnt
    in statements. Returns variable dictionary. """
    if not statements:
        return in_dic

    dic = deepcopy(in_dic)
    dic = statement_mngr(first_statement(statements), dic)

    return statements_mngr(rest_statements(statements), dic)


def statement_mngr(statement, in_dic):
    """ Identifies the type of statement the input is and calls the appropriate
    function. Returns variable dictionary. """
    dic = deepcopy(in_dic)

    if isassignment(statement):
        dic = assignment_mngr(statement, dic)
    elif isrepetition(statement):
        dic = repetition_mngr(statement, dic)
    elif isselection(statement):
        dic = selection_mngr(statement, dic)
    elif isinput(statement):
        dic = input_mngr(statement, dic)
    elif isoutput(statement):
        output_mngr(statement, dic)
    elif isbinary(statement):
        binaryexpr_mngr(statement, dic)
    elif iscondition(statement):
        condition_mngr(statement, dic)

    return dic


def repetition_mngr(repetition_expr, in_dic):
    """ Sends all statments to statement_mngr while condition is true """
    condition = repetition_condition(repetition_expr)
    statements = repetition_statements(repetition_expr)
    dic = deepcopy(in_dic)

    while condition_mngr(condition, dic):
        dic = statements_mngr(statements, dic)

    return dic

def assignment_mngr(expr, in_dic):
    """ Takes assignment statement and saves the variable value in dic """
    dic = deepcopy(in_dic)
    dic[assignment_variable(expr)] = \
        expression_mngr(assignment_expression(expr), dic)
    return dic


def selection_mngr(lst, in_dic):
    """ Runs first statement if condition is true, otherwise runs
    second condition if there is one """
    dic = deepcopy(in_dic)

    if condition_mngr(selection_condition(lst), dic):
        dic = statement_mngr(selection_true(lst), dic)
    elif hasfalse(lst):
        dic = statement_mngr(selection_false(lst), dic)

    return dic


def input_mngr(expr, in_dic):
    """ Takes input from user and saves in dic """
    dic = deepcopy(in_dic)

    var = input_variable(expr)
    s = "Enter value for " + var + ": "
    temp = input(s)
    temp_int = int(temp)
    temp_float = float(temp)
    if temp_int == temp_float:
        temp = temp_int
    else:
        temp = temp_float
    dic[var] = temp

    return dic


def output_mngr(expr, dic):
    """ Outputs the value of variable var to console """
    var = output_variable(expr)
    print(var, "=", dic[var])
    return


def expression_mngr(expr, dic):
    """ Takes an expression expr and returns it's value  """
    if isinstance(expr, str):
        return dic[expr]
    elif isinstance(expr, list):
        return binaryexpr_mngr(expr, dic)
    else:
        return expr


def condition_mngr(condition, dic):
    """ Takes a condition, checks what operator is used then
    applies it, and returns the result. """
    operator = condition_operator(condition)
    con_left = condition_left(condition)
    con_right = condition_right(condition)

    if operator == '=':
        return expression_mngr(con_left, dic) == \
            expression_mngr(con_right, dic)
    elif operator == '<':
        return expression_mngr(con_left, dic) < \
            expression_mngr(con_right, dic)
    elif operator == '>':
        return expression_mngr(con_left, dic) > \
            expression_mngr(con_right, dic)


def binaryexpr_mngr(bin_expr, dic):
    """ Takes a binary expression, checks what operator is used then
    applies it, and returns the result """
    operator = binary_operator(bin_expr)
    bin_left = binary_left(bin_expr)
    bin_right = binary_right(bin_expr)

    if operator == '+':
        return expression_mngr(bin_left, dic) + \
            expression_mngr(bin_right, dic)
    elif operator == '-':
        return expression_mngr(bin_left, dic) - \
            expression_mngr(bin_right, dic)
    elif operator == '*':
        return expression_mngr(bin_left, dic) * \
            expression_mngr(bin_right, dic)
    elif operator == '/':
        return expression_mngr(bin_left, dic) / \
            expression_mngr(bin_right, dic)

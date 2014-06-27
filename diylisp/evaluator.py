# -*- coding: utf-8 -*-

from types import Environment, LispError, Closure
from ast import is_boolean, is_atom, is_symbol, is_list, is_closure, is_integer
from asserts import assert_exp_length, assert_valid_definition, assert_boolean
from parser import unparse

"""
This is the Evaluator module. The `evaluate` function below is the heart
of your language, and the focus for most of parts 2 through 6.

A score of useful functions is provided for you, as per the above imports, 
making your work a bit easier. (We're supposed to get through this thing 
in a day, after all.)
"""

def eval_math(ast, env):
    return eval(str(evaluate(ast[1], env)) + ast[0] + str(evaluate(ast[2], env)))

def evaluate(ast, env):
    """Evaluate an Abstract Syntax Tree in the specified environment."""
    if is_boolean(ast):
	return ast
    elif is_integer(ast):
	return ast
    elif ast[0] in ['+', '-', '*', '/']:
	return eval_math(ast, env)
    elif is_list(ast):
	if ast[0] == "atom":
	    return is_atom(evaluate(ast[1], env))
	    #return is_atom(ast[1])
	elif ast[0] == "quote":
	    return ast[1]
	elif ast[0] == "eq":
	    assert_exp_length(ast, 3)
	    v1 = evaluate(ast[1], env)
	    v2 = evaluate(ast[2], env)
	    if not is_atom(v1) or not is_atom(v2):
		return False
	    else:
		return (v1 == v2)

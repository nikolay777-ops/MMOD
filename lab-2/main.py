import sympy as sp
from sympy import sympify, solve, diff, Interval, lambdify, S, solveset
from sympy.calculus.util import continuous_domain
from sympy.abc import x, y

from sympy import EmptySet 


def sol_is_not_empty(sol) -> bool:
    return solveset(diff(sol, y) > 0, y, S.Reals) is not EmptySet

def fun_is_continuous(fun) -> bool:
    return continuous_domain(fun, y, S.Reals).is_proper_superset(Interval(0, 1))

def find_inverse_func(input_text):
    funcs = []
    ex = sympify(input_text)
    expr = ex - y
    results = solve(expr, x)

    for result in results:
        if sol_is_not_empty(result) and fun_is_continuous(result):
            print(result)
            funcs.append(lambdify(y, result))

    return funcs


print(find_inverse_func(input()))

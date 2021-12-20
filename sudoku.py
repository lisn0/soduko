from __future__ import print_function

import random

from pyswip.prolog import Prolog

from puzzles import *

prolog = Prolog()


def pretty_print(table):
    print("".join(["/---", "----" * 8, "\\"]))
    for row in table:
        print("".join(["|", "|".join(" %s " % (i or " ") for i in row), "|"]))
    print("".join(["\\---", "----" * 8, "/"]))


def pretty_print4(table):
    print("".join(["/---", "----" * 3, "\\"]))
    for row in table:
        print("".join(["|", "|".join(" %s " % (i or " ") for i in row), "|"]))
    print("".join(["\\---", "----" * 3, "/"]))


def solve(problem):
    prolog.consult("./sudoku.pl")
    p = str(problem).replace("0", "_")
    print('hooooo ', p)
    result = list(prolog.query("L=%s,sudoku(L)" % p, maxresult=1))
    if result:
        result = result[0]
        return result["L"]
    else:
        return False


def solve2(problem):
    prolog.consult("./sudoku4.pl")
    p = str(problem).replace("0", "_")
    result = list(prolog.query("L=%s,sudoku4(L)" % p, maxresult=1))
    if result:
        result = result[0]
        return result["L"]
    else:
        return False


def main2():
    puzzle = random.choice([puzzle1, puzzle2])
    print("-- PUZZLE --")
    pretty_print(puzzle)
    print()
    print(" -- SOLUTION --")
    solution = solve(puzzle)
    if solution:
        pretty_print(solution)
    else:
        print("This puzzle has no solutions [is it valid?]")


def main3(puzzle=puzzl3):
    print("-- PUZZLE --")
    pretty_print4(puzzle)
    print()
    print(" -- SOLUTION --")
    solution = solve2(puzzle)
    if solution:
        pretty_print4(solution)
    else:
        print("This puzzle has no solutions [is it valid?]")


def user_input():
    x = 4
    y = 4
    list1 = []
    sublist = []
    for i in range(x):
        for j in range(y):
            print("input ",i+1,j+1,":")
            sublist.append(int(input()))
        list1.append(sublist)
        sublist = []
    main3(list1)


if __name__ == "__main__":
    prolog = Prolog()
    main3()

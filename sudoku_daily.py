from __future__ import print_function
from pyswip.prolog import Prolog


try:
    from html.parser import HTMLParser
except:
    from HTMLParser import HTMLParser

try:
    import urllib.request as urllib_request
except ImportError:
    import urllib as urllib_request


prolog = Prolog()


class DailySudokuPuzzle(HTMLParser):
    def __init__(self):
        self.puzzle = []
        self.__in_td = False
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        if tag == "td":
            for attr in attrs:
                if attr[0] == "class" and attr[1] == "InnerTDone":
                    self.__in_td = True
                    break
        elif tag == "input":
            if self.__in_td:
                self.puzzle.append(0)

    def handle_endtag(self, tag):
        if tag == "td":
            self.__in_td = False

    def handle_data(self, data):
        if self.__in_td:
            self.puzzle.append(int(data))


def pretty_print(table):
    print("".join(["/---", "----" * 8, "\\"]))
    for row in table:
        print("".join(["|", "|".join(" %s " % (i or " ") for i in row), "|"]))
    print("".join(["\\---", "----" * 8, "/"]))


def get_daily_sudoku(url):
    puzzle = DailySudokuPuzzle()
    f = urllib_request.urlopen(url)
    puzzle.feed(f.read().decode("latin-1"))
    puzzle = puzzle.puzzle
    return [puzzle[i * 9:i * 9 + 9] for i in range(9)]


def solve(problem):
    prolog.consult("sudoku.pl")
    p = str(problem).replace("0", "_")
    result = list(prolog.query("Puzzle=%s,sudoku(Puzzle)" % p, maxresult=1))
    if result:
        result = result[0]
        return result["Puzzle"]
    else:
        return False



def solve_daily_puzzle():
    URL = "http://www.sudoku.org.uk/daily.asp"

    print("Getting puzzle from:", URL)
    puzzle = get_daily_sudoku(URL)
    print("-- PUZZLE --")
    pretty_print(puzzle)
    print()
    print(" -- SOLUTION --")
    solution = solve(puzzle)
    if solution:
        pretty_print(solution)
    else:
        print("This puzzle has no solutions [is it valid?]")
if __name__ == "__main__":

    prolog = Prolog()
    solve_daily_puzzle()
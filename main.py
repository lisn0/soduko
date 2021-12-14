from sudoku import main2
from sudoku_daily import solve_daily_puzzle


def enter_puzzle():
    puzzle = input("enter puzzle as a list 9*9")

def menu():
    print("#############################################################################")
    print("########                                                             ########")
    print("########                                                             ########")
    print("######## ----------------------------------------------------------- ########")
    print("########                 Sudoku Solver Expert System                 ########")
    print("######## ----------------------------------------------------------- ########")
    print("########                                                             ########")
    print("########                    Choose a option:                         ########")
    print("########                                                             ########")
    print("########      1) solve puzzle                                        ########")
    print("########      2) solve daily puzzle from sudoku.org.uk               ########")
    print("########      3) Exit                                                ########")
    print("########                                                             ########")
    print("#############################################################################")
    print("* custom puzzle coming soon")
    while 1:
        choice_menu = {
                "2": solve_daily_puzzle,
                "1": main2,
                "3": exit,
                "4": enter_puzzle

            }

        choice = input("Enter a number from 1 to 3: >")

        choice_menu[choice]()


if __name__ == '__main__':
    menu()


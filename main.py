from sudoku import main2, main3
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
    print("########      1) solve 9x9 puzzle                                     ########")
    print("########      2) solve 4x4 puzzle                                        ########")
    print("########      3) solve daily puzzle from sudoku.org.uk               ########")
    print("########      4) Exit                                                ########")
    print("########                                                             ########")
    print("#############################################################################")
    print("* custom puzzle coming soon")
    while 1:
        choice_menu = {
                "2": solve_daily_puzzle,
                "1": main2,
                "3": main3,
                "4": exit

            }

        choice = input("Enter a number from 1 to 3: >")

        choice_menu[choice]()


if __name__ == '__main__':
    menu()


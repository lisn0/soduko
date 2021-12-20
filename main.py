from sudoku import main2, main3, user_input
from sudoku_daily import solve_daily_puzzle



def menu():
    print("#############################################################################")
    print("########                                                             ########")
    print("########                                                             ########")
    print("######## ----------------------------------------------------------- ########")
    print("########                 Sudoku Solver Expert System                 ########")
    print("######## ----------------------------------------------------------- ########")
    print("########                                                             ########")
    print("########                    Choose a option:                         ########")
    print("########      1) solve 9x9 puzzle                                    ########")
    print("########      2) solve 4x4 puzzle                                    ########")
    print("########      3) solve daily puzzle from sudoku.org.uk               ########")
    print("########      4) input 4x4 puzzle                                    ########")
    print("########      5) Exit                                                ########")
    print("#############################################################################")
    while 1:
        choice_menu = {
                "2": solve_daily_puzzle,
                "1": main2,
                "3": main3,
                "4": user_input,
                "5": exit
            }

        choice = input("Enter a number from 1 to 3: >")

        choice_menu[choice]()


if __name__ == '__main__':
    menu()

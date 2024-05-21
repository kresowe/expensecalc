from expenses import Expenses
from app_terminal_viewer import hello, show_menu, user_option, add_expense, show_total_value, show_stats, bye
from utils import DEFAULT_DUMMY_OPTION, OPTION_SHOW, OPTION_ADD, OPTION_EXIT

if __name__ == '__main__':
    expenses = Expenses()
    option = DEFAULT_DUMMY_OPTION

    hello()
    while option != OPTION_EXIT:
        show_menu()
        option = user_option()
        if option == OPTION_ADD:
            expense = add_expense()
            expenses.add_expense(expense)
        elif option == OPTION_SHOW:
            show_total_value(expenses)
            show_stats(expenses)
    bye()


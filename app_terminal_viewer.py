from typing import Optional
from utils import user_input_in_given_integers, user_input_value
from expenses import categories, Expenses


def hello() -> None:
    """Prints greetings when app starts."""
    print('Welcome to ExpenseCalc app!')


def bye() -> None:
    """Prints text when user closes app."""
    print('Bye!')


def show_menu() -> None:
    """Shows basic menu options."""
    print()
    print('What do you want to do?')
    print('1: Add new expense.')
    print('2: Show summary.')
    print('3: Exit.')
    print()


def user_option() -> int:
    """Asks user to type option.
    Then returns the option chosen by user or 0 if user provided invalid input."""
    options = (1, 2, 3)
    user_inp = input('Choose option: ')
    option = user_input_in_given_integers(user_inp, options)
    return option


def add_expense() -> Optional[dict]:
    """Asks user to type name of expense, choose its category, and provide value.
    Returns dict of form {'name': name, 'category': category, 'value': value} if user's input was valid.
    Returns None otherwise."""
    name = input('Give name to your expense: ')

    categories_ints = tuple(range(1, len(categories) + 1))
    category = user_category_of_expense(categories_ints)
    if category not in categories_ints:
        return None

    user_inp_amount = input('Value: ')
    value = user_input_value(user_inp_amount)
    if not value > 0:
        return None
    return {'name': name, 'category': category, 'value': value}


def print_categories() -> None:
    """Prints available categories with numbers."""
    for i in range(len(categories)):
        print(f'{i+1}: {categories[i]}')


def user_category_of_expense(categories_ints: tuple) -> int:
    """Asks user to choose expense category out of options.
    Returns user's choice or 0 if user provided invalid input."""
    print('Choose expense category:')
    print_categories()
    user_inp = input('Category: ')
    return user_input_in_given_integers(user_inp, categories_ints)


def show_total_value(expenses: Expenses) -> None:
    """Shows total value of expenses."""
    print(f'Total value: {expenses.total_value:.2f}')
    print()


def show_stats(expenses: Expenses) -> None:
    """Shows table with total value and share of each category of expense in form:
    Category | Sum | Share [%]
    """
    response = expenses.value_per_category_stats()

    labels = ('Category', 'Sum ', 'Share [%]')
    print(f'{labels[0]:<15}{labels[1]:>10}{labels[2]:>10}')
    print('-'*35)
    for category in response:
        print(f"{category:<15}{response[category]['total']:10.2f}{response[category]['share']:10.2f}")

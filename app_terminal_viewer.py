from typing import Optional
from utils import user_input_in_given_integers, user_input_value
from expenses import categories, Expenses


def hello() -> None:
    print('Welcome to ExpenseCalc app!')


def bye() -> None:
    print('Bye!')


def show_menu() -> None:
    print()
    print('What do you want to do?')
    print('1: Add new expense.')
    print('2: Show summary.')
    print('3: Exit.')
    print()


def user_option() -> int:
    options = (1, 2, 3)
    user_inp = input('Choose option: ')
    option = user_input_in_given_integers(user_inp, options)
    return option


def add_expense() -> Optional[dict]:
    name = input('Give name to your expense: ')

    categories_ints = tuple(range(1, len(categories) + 1))
    category = user_category_of_expense(categories_ints)
    if category not in categories_ints:
        return None

    user_inp_amount = input('Amount: ')
    value = user_input_value(user_inp_amount)
    if not value > 0:
        return None
    return {'name': name, 'category': category, 'value': value}


def print_categories() -> None:
    for i in range(len(categories)):
        print(f'{i+1}: {categories[i]}')


def user_category_of_expense(categories_ints: tuple) -> int:
    print('Choose expense category:')
    print_categories()
    user_inp = input('Category: ')
    return user_input_in_given_integers(user_inp, categories_ints)


def show_total_value(expenses: Expenses) -> None:
    print('Total value:', expenses.total_value)
    print()


def show_stats(expenses: Expenses) -> None:
    response = expenses.value_per_category_stats()

    labels = ('Category', 'Sum ', 'Share [%]')
    print(f'{labels[0]:<15}{labels[1]:>10}{labels[2]:>10}')
    print('-'*35)
    for category in response:
        print(f"{category:<15}{response[category]['total']:10.2f}{response[category]['share']:10.2f}")

from utils import user_input_in_given_integers, user_input_value
from expenses import categories


def hello():
    print('Welcome to ExpenseCalc app!')


def bye():
    print('Bye!')


def show_menu():
    print()
    print('What do you want to do?')
    print('1: Add new expense.')
    print('2: Show summary.')
    print('3: Exit.')
    print()


def user_option():
    options = (1, 2, 3)
    user_inp = input('Choose option: ')
    option = user_input_in_given_integers(user_inp, options)
    return option


def add_expense():
    name = input('Give name to your expense:')
    print('Choose expense category:')
    for i in range(len(categories)):
        print(f'{i+1}: {categories[i]}')
    user_inp = input('Category: ')
    categories_ints = tuple(range(1, len(categories) + 1))
    category = user_input_in_given_integers(user_inp, categories_ints)
    if category not in categories_ints:
        return None
    user_inp_amount = input('Amount: ')
    value = user_input_value(user_inp_amount)
    if not value > 0:
        return None
    return {'name': name, 'category': category, 'value': value}


def show_total_value(expenses):
    print('Total value:', expenses.total_value)


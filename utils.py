DEFAULT_DUMMY_OPTION = 0
OPTION_ADD = 1
OPTION_SHOW = 2
OPTION_EXIT = 3


def user_input_in_given_integers(user_inp, options):
    try:
        option = int(user_inp)
        if option not in options:
            raise ValueError
    except ValueError:
        print(f'Option should be one of {options}.')
        option = 0
    except Exception as e:
        print(f'Error {e}')
        option = 0
    return option


def user_input_value(user_inp):
    try:
        value = round(float(user_inp), 2)
        if value < 0:
            raise ValueError
    except ValueError:
        print('Value should be a positive decimal number.')
        value = 0.0
    except Exception as e:
        print(f'Error {e}')
        value = 0.0
    return value

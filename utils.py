DEFAULT_DUMMY_OPTION = 0
OPTION_ADD = 1
OPTION_SHOW = 2
OPTION_EXIT = 3


def user_input_in_given_integers(user_inp: str, options: tuple, option_else: int = DEFAULT_DUMMY_OPTION) -> int:
    """Tries to transform user input to int and checks if it is one of the accepted option in options.
    If input is accepted, returns this int. Otherwise, returns option_else.
    """
    try:
        option = int(user_inp)
        if option not in options:
            raise ValueError
    except ValueError:
        print(f'Option should be one of {options}.')
        option = option_else
    except Exception as e:
        print(f'Error {e}')
        option = option_else
    return option


def user_input_value(user_inp: str) -> float:
    """Tries to transform user input to float and checks if it is non-negative.
    If input is accepted, returns this float number. Otherwise, returns 0.0.
    """
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

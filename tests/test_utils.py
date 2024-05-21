import pytest
from utils import user_input_in_given_integers, user_input_value


@pytest.fixture
def options():
    return 1, 2, 3


def test_valid_user_option_returns_option(options):
    assert user_input_in_given_integers("1", options) == 1
    assert user_input_in_given_integers("2", options) == 2


def test_user_option_out_of_range_returns_0(options):
    assert user_input_in_given_integers("4", options) == 0


def test_invalid_user_option_returns_0(options):
    assert user_input_in_given_integers("aa", options) == 0


def test_wrong_user_option_prints_message(options, capsys):
    _ = user_input_in_given_integers("4", options)
    out, err = capsys.readouterr()
    assert out == f'Option should be one of {options}.\n'

    _ = user_input_in_given_integers("aa", options)
    out, err = capsys.readouterr()
    assert out == f'Option should be one of {options}.\n'


def test_valid_user_input_value_returns_value():
    assert user_input_value("10.5") == pytest.approx(10.5)


def test_input_correctly_rounded():
    assert user_input_value("10.511") == pytest.approx(10.51)
    assert user_input_value("10.508") == pytest.approx(10.51)


def test_invalid_user_input_value_returns_0():
    assert user_input_value("-10.5") == pytest.approx(0.0)
    assert user_input_value("aa") == pytest.approx(0.0)


def test_invalid_user_input_value_prints_message(capsys):
    _ = user_input_value("-10.5")
    out, err = capsys.readouterr()
    assert out == 'Value should be a positive decimal number.\n'

    _ = user_input_value("aa")
    out, err = capsys.readouterr()
    assert out == 'Value should be a positive decimal number.\n'

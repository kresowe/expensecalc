import pytest
from expenses import Expenses


@pytest.fixture
def expenses():
    return Expenses()


def test_no_expenses_total_is_0(expenses):
    assert expenses.total_value == pytest.approx(0.0)

    response = expenses.value_per_category_stats()
    for category in response:
        assert response[category]['total'] == pytest.approx(0.0)
        assert response[category]['share'] == pytest.approx(0.0)


def test_valid_expense_adds_correctly(expenses):
    expenses.add_expense({'name': 'pizza', 'category': 1, 'value': 30.0})
    assert len(expenses.expenses) == 1
    assert expenses.total_value == pytest.approx(30.0)
    assert expenses.expenses[0]['name'] == 'pizza'
    assert expenses.expenses[0]['category'] == 'Food'

    response = expenses.value_per_category_stats()
    assert response['Food']['total'] == pytest.approx(30.0)
    assert response['Food']['share'] == pytest.approx(100)
    for category in response:
        if category != 'Food':
            assert response[category]['total'] == pytest.approx(0.0)
            assert response[category]['share'] == pytest.approx(0)


def test_multiple_expenses_add_correctly(expenses):
    expenses.add_expense({'name': 'pizza', 'category': 1, 'value': 30.0})
    expenses.add_expense({'name': 'pasta', 'category': 1, 'value': 20.5})
    expenses.add_expense({'name': 'theatre', 'category': 2, 'value': 50.0})
    assert len(expenses.expenses) == 3
    assert expenses.total_value == pytest.approx(100.5)

    response = expenses.value_per_category_stats()
    assert response['Food']['total'] == pytest.approx(50.5)
    assert response['Food']['share'] == pytest.approx(round(50.5/100.5 * 100, 2))
    assert response['Entertainment']['total'] == pytest.approx(50.0)
    assert response['Entertainment']['share'] == pytest.approx(round(50./100.5 * 100, 2))
    for category in response:
        if category not in ('Food', 'Entertainment'):
            assert response[category]['total'] == pytest.approx(0.0)
            assert response[category]['share'] == pytest.approx(0)


def test_invalid_expense_doesnt_add(expenses):
    expenses.add_expense(None)
    assert len(expenses.expenses) == 0

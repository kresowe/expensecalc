from typing import Optional

# categories of expenses
categories = ('Food', 'Entertainment', 'Commuting', 'Bills', 'Other')


class Expenses:
    """Class for bookkeeping expenses."""
    def __init__(self) -> None:
        """Initializes expenses object."""
        self._expenses = []
        self._total_value = 0.
        self._value_per_category = {}
        for category in categories:
            self._value_per_category[category] = 0.

    def add_expense(self, expense: Optional[dict]) -> None:
        """Adds new expense to the list of expenses.
        It also updates total value and value of the corresponding category."""
        if expense is not None:
            name = expense['name']
            category = categories[expense['category']-1]
            value = expense['value']
            self._expenses.append({'name': name,
                                   'category': category,
                                   'value': value})
            self._total_value += value
            self._value_per_category[category] += value

    @property
    def total_value(self) -> float:
        return self._total_value

    @property
    def expenses(self) -> list:
        return self._expenses

    def value_per_category_stats(self) -> dict:
        """Returns total value per category of expense and share of this category in total expenses.
        Result is in form
        {'category1': {'total': total_value, 'share': share},
        'category2': {'total': total_value, 'share': share}, ... }
        """
        response = {}
        for category in self._value_per_category:
            val = self._value_per_category[category]
            if self.total_value == 0:
                share = 0
            else:
                share = round(val / self.total_value * 100, 2)
            response[category] = {'total': val, 'share': share}
        return response

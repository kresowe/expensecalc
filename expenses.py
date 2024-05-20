categories = ('Food', 'Entertainment', 'Commuting', 'Bills', 'Other')


class Expenses:
    def __init__(self):
        self._expenses = []
        self._total_value = 0.

    def add_expense(self, expense):
        if expense is not None:
            self._expenses.append({'name': expense['name'],
                                   'category': categories[expense['category']],
                                   'value': ['value']})
            self._total_value += expense['value']

    @property
    def total_value(self):
        return self._total_value

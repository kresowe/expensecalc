categories = ('Food', 'Entertainment', 'Commuting', 'Bills', 'Other')


class Expenses:
    def __init__(self):
        self._expenses = []
        self._total_value = 0.
        self._value_per_category = {}
        for category in categories:
            self._value_per_category[category] = 0.

    def add_expense(self, expense):
        if expense is not None:
            name = expense['name']
            category = categories[expense['category']]
            value = expense['value']
            self._expenses.append({'name': name,
                                   'category': category,
                                   'value': value})
            self._total_value += value
            self._value_per_category[category] += value

    @property
    def total_value(self):
        return self._total_value

    # def value_per_category_stats(self):

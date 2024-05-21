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
            category = categories[expense['category']-1]
            value = expense['value']
            self._expenses.append({'name': name,
                                   'category': category,
                                   'value': value})
            self._total_value += value
            self._value_per_category[category] += value

    @property
    def total_value(self):
        return self._total_value

    @property
    def expenses(self):
        return self._expenses

    def value_per_category_stats(self):
        response = {}
        for category in self._value_per_category:
            val = self._value_per_category[category]
            if self.total_value == 0:
                share = 0
            else:
                share = round(val / self.total_value * 100, 2)
            response[category] = {'total': val, 'share': share}
        return response

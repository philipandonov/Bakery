from bakery.table.table import Table


class InsideTable(Table):
    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def massage(self):
        return "Inside table's number must be between 1 and 50 inclusive!"

    @property
    def min_value(self):
        return 1

    @property
    def max_value(self):
        return 50

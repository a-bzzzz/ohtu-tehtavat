from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or as matcher

class QueryBuilder:
    def __init__(self, matcher = All):
        self.matcher = matcher

    def build(self):
        return self.matcher
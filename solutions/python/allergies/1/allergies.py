ALLERGY_SCORES = {
    1: "eggs",
    2: "peanuts",
    4: "shellfish",
    8: "strawberries",
    16: "tomatoes",
    32: "chocolate",
    64: "pollen",
    128: "cats",
}


class Allergies(object):

    def __init__(self, score):
        self._score = score
        self._lst = []

    def is_allergic_to(self, item):
        return item in self.lst

    @property
    def score(self):
        """ A property makes taking care of edge cases cleaner. """
        if self._score >= 256:
            return self._score - 256
        else:
            return self._score

    @score.setter
    def score(self, value):
        """ Needed for changing the property's value. """
        self._score = value

    @property
    def lst(self):
        for i in range(7, -1, -1):
            if self.score >= 2 ** i:
                self._lst.append(ALLERGY_SCORES[2 ** i])
                self.score = self.score - 2 ** i
        return self._lst

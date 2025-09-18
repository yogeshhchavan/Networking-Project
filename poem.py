class Poem:
    def __init__(self):
        self.lines = [
            (1, "The soul is free beyond the sky"),
            (2, "Love and hope never die"),
            (3, "Dreams take shape with gentle hand"),
            (4, "This is my land, my native land"),
            (5, "land mafia everywhere"),
        ]

    def clean(self):
        # Can preprocess lines if needed (e.g., strip spaces)
        self.lines = [(num, text.strip()) for num, text in self.lines]

    def getLines(self, word):
        """Return all lines containing the given word (case-insensitive)."""
        word = word.lower()
        result = []
        for num, text in self.lines:
            if word in text.lower():
                result.append((num, text))
        return result

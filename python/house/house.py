class Phrase:

    def __init__(self, noun, verb):
        self.noun = noun
        self.verb = verb

    def first(self):
        return f"This is the {self.noun}"

    def line(self):
        return f"that {self.verb} the {self.noun}"

PHRASES = [
    Phrase("house that Jack built", "lay in"),
    Phrase("malt", "ate"),
    Phrase("rat", "killed"),
    Phrase("cat", "worried"),
    Phrase("dog", "tossed"),
    Phrase("cow with the crumpled horn", "milked"),
    Phrase("maiden all forlorn", "kissed"),
    Phrase("man all tattered and torn", "married"),
    Phrase("priest all shaven and shorn", "woke"),
    Phrase("rooster that crowed in the morn", "kept"),
    Phrase("farmer sowing his corn", "belonged to"),
    Phrase("horse and the hound and the horn", None)
    ]


def recite(start_verse, end_verse):
    result = []
    verse = None
    for i in range(start_verse-1, end_verse):
        verse = [PHRASES[i].first()]
        for j in range(i-1, -1, -1):
            verse.append(PHRASES[j].line())
        verse = " ".join(verse) + "."
        result.append(verse)
    return result

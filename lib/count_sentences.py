import re

class MyString:
    def __init__(self, value=""):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        # Regular expression to match sentence-ending punctuation.
        sentences = re.split(r'(?<=[.!?]) +', self._value)
        # Filter out empty strings that may result from split
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)

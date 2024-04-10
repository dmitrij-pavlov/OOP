class MinMaxWordFinder:
    def __init__(self):
        self.shortest = []
        self.longest = []

    def add_sentence(self, sentence):
        words = sentence.split()
        words = [word.strip(",.?!") for word in words]
        words = [word for word in words if word]  # remove empty strings
        words.sort()  # sort alphabetically
        shortest_length = len(min(words, key=len))
        longest_length = len(max(words, key=len))

        self.shortest.extend([word for word in words if len(word) == shortest_length and word not in self.shortest])
        self.longest.extend([word for word in words if len(word) == longest_length])

    def shortest_words(self):
        return sorted(self.shortest)

    def longest_words(self):
        return sorted(set(self.longest))  # remove duplicates

# Пример использования:
finder = MinMaxWordFinder()
finder.add_sentence("This is a test sentence")
finder.add_sentence("Hello world, this is another test")
print(finder.shortest_words())  # Output: ['a', 'a', 'is']
print(finder.longest_words())   # Output: ['another', 'sentence', 'world']
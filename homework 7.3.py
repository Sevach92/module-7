class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                info = file.read().lower()
                for s in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    info = info.replace(s, '')
                all_words[name] = info.split()
        return all_words

    def find(self, word):
        for name, words in self.get_all_words().items():
           if word.lower() in words:
               return {name: words.index(word.lower())+1}
    def count(self, word):
        counter = 0
        for name, words in self.get_all_words().items():
            for word_ in words:
                if word.lower() == word_:
                    counter += 1
        return {name: counter}

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
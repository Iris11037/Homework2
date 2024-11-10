import re
class WordsFinder:
    def __init__(self, *file_name: str):
        self.file_name = file_name

    def get_all_words(self):
        all_words = {}
        for f in self.file_name:
            with open(f, encoding='utf-8') as file:
                words = []
                for i in file:
                    i = i .lower()
                    i = re.sub(r'[,.\=!\?;:\-]', '', i)
                    words.extend(i.split())
                    all_words[f] = words
        return all_words

    def find(self, word):
        find_dict = self.get_all_words()
        result_dict = {}
        index = 1
        word = word.lower()
        for file_name, words in find_dict.items():
            for i in words:
                if i == word:
                    result_dict[file_name] = index
                    break
                index += 1
        return result_dict

    def count(self, word):
        find_dict = self.get_all_words()
        result_dict = {}
        index = 1
        word = word.lower()
        for filename, words in find_dict.items():
            for i in words:
                if i == word:
                    result_dict[filename] = index
                    index += 1
        return result_dict

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))

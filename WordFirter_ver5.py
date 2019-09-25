class WordFilter:
    def __init__(self, word):
        self.ngWord = []
        self.ngWord.append(word)

        self.censored_phrase = '<censored>'

    def setCensored(self, phrase):
        self.censored_phrase = phrase

    def addNgWord(self, word):
        self.ngWord.append(word)

    def changeNgWord(self, ngword, reword):
        new_list = []
        for word in self.ngWord:
            new_word = word.replace(ngword, reword)
            new_list.append(new_word)
        self.ngWord = new_list

    def detect(self, sentence):
        for check in self.ngWord:
            if check in sentence:
                sentence = sentence.replace(check, self.censored_phrase)

        return sentence


def main():
    my_filter = WordFilter("アーセナル")
    my_filter.changeNgWord("アーセナル", "リバプール")
    my_filter.setCensored('XXXXX')
    print(my_filter.detect("昨日のアーセナルの試合アツかった！"))
    print(my_filter.detect("昨日のリバプールの試合アツかった！"))


if __name__ == '__main__':
    main()
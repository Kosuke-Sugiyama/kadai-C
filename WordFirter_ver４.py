class WordFilter:
    def __init__(self, word):
        self.ngWord = []
        self.ngWord.append(word)

        self.censored_phrase = '<censored>'

    def setCensored(self, phrase):
        self.censored_phrase = phrase

    def addNgWord(self, word):
        self.ngWord.append(word)

    def detect(self, sentence):
        for check in self.ngWord:
            if check in sentence:
                sentence = sentence.replace(check, self.censored_phrase)

        return sentence


def main():
    my_filter = WordFilter("アーセナル")
    my_filter.addNgWord("リバプール")
    my_filter.setCensored('XXXXX')
    print(my_filter.detect("昨日のアーセナルの試合アツかった！"))
    print(my_filter.detect("昨日のリバプールの試合アツかった！"))


if __name__ == '__main__':
    main()
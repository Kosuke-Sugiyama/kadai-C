class WordFilter:
    def __init__(self, word):
        self.word = word
        self.censored_phrase = '<censored>'

    def setCensored(self, phrase):
        self.censored_phrase = phrase

    def detect(self, sentence):
        if self.word in sentence:
            return sentence.replace(self.word, self.censored_phrase)

        return sentence


def main():
    my_filter = WordFilter("アーセナル")
    my_filter.setCensored('XXXXX')
    print(my_filter.detect("昨日のアーセナルの試合アツかった！"))
    print(my_filter.detect("昨日のリバプールの試合アツかった！"))


if __name__ == '__main__':
    main()
class WordFilter:
    def __init__(self, word):
        self.word = word

    def detect(self, sentence):
        return self.word in sentence


def main():
    my_filter = WordFilter("アーセナル")
    print(my_filter.detect("昨日のアーセナルの試合アツかった！"))
    print(my_filter.detect("昨日のリバプールの試合アツかった！"))


if __name__ == '__main__':
    main()
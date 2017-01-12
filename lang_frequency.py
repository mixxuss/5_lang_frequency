import argparse


def create_parser():
    # Creates a parser for filepath
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', nargs='?')
    return parser


def load_data(filepath):
    # Opens file by path in filepath variable and return list with words split by ' '
    text = open(filepath).read()
    return text.split()


def get_most_frequent_words(text):
    # Gets list with words and back dict in format {word:count}
    wordfreq = [text.count(p) for p in text]
    di = dict(zip(text, wordfreq))
    return max(di, key=di.get)


if __name__ == '__main__':
    parsed_args = create_parser()
    filepath = parsed_args.parse_args()
    print("The most frequent word is", get_most_frequent_words(load_data(filepath.filepath)))

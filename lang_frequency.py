import argparse
import collections
import re


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', nargs='?')
    return parser


def load_text_from_file(filepath):
    with open(filepath, 'r') as text:
        return text.read()


def make_words_list(text_str):
    return re.findall('\w+', text_str)


def get_most_common_words(words_list, words_amount):
    counter = collections.Counter(words_list)
    return counter.most_common(words_amount)


if __name__ == '__main__':
    parsed_args = create_parser()
    args = parsed_args.parse_args()
    only_words_text = make_words_list(load_text_from_file(args.filepath))
    results_amount = 5
    results = get_most_common_words(only_words_text, results_amount)
    for word in results:
        print('Word %s found %d times' % (word[0], word[1]))

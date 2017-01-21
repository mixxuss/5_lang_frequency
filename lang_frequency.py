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


def delete_symbols(text_str):
    return re.sub('[^a-z\ \']+', ' ', text_str).lower()


def make_a_list(text):
    return text.split()


def count_words(text_list):
    counter = collections.Counter(text_list)
    return counter


def get_most_common_words(counter, words_amount):
    return counter.most_common(words_amount)


if __name__ == '__main__':
    parsed_args = create_parser()
    args = parsed_args.parse_args()
    only_words_text = delete_symbols(load_text_from_file(args.filepath))
    text_list = make_a_list(only_words_text)
    words_counter = count_words(text_list)
    results_amount = 5
    results = get_most_common_words(words_counter, results_amount)
    for word in results:
        print('Word %s found %d times' % (word[0], word[1]))

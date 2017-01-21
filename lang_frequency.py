import argparse, collections


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', nargs='?')
    return parser


def load_text_from_file(filepath):
    with open(filepath, 'r') as text:
        return text.read()


def make_a_list(text):
    return text.lower().replace(',', ' ').replace('.', ' ').split()


def count_words(text_list):
    counter = collections.Counter(text_list)
    return counter


def get_most_common_words(counter, words_amount):
    return counter.most_common(words_amount)


if __name__ == '__main__':
    parsed_args = create_parser()
    args = parsed_args.parse_args()
    text_list = make_a_list(load_text_from_file(args.filepath))
    words_counter = count_words(text_list)
    results_amount = 5
    results = get_most_common_words(words_counter, results_amount)
    for word in results:
        print('Word %s found %d times' % (word[0], word[1]))
import argparse, collections


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', nargs='?')
    return parser


def load_text_from_file(filepath):
    with open(filepath, 'r') as text:
        return text.read()


def make_a_list(text):
    return text.split()


def get_most_frequent_words(text_list):
    cnt = collections.Counter()
    for word in text_list:
        cnt[word] += 1
    return cnt


def print_most_frequent_words(counter):
    return counter


if __name__ == '__main__':
    parsed_args = create_parser()
    filepath = parsed_args.parse_args()
    file = make_a_list(load_text_from_file(filepath.filepath))
    # print("The most frequent word is", get_most_frequent_words(file))
    print(print_most_frequent_words(get_most_frequent_words(file)))

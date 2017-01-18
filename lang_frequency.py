import argparse, collections


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', nargs='?')
    return parser


def load_text_from_file(filepath):
    with open(filepath, 'r') as text:
        return text.read()


def make_a_list(text):
    return text.lower().split()


def count_words(text_list):
    cnt = collections.Counter()
    for word in text_list:
        cnt[word] += 1
    return cnt


def get_most_frequent_words(counted_dict):
    words_dict = dict(counted_dict)
    top5_list = sorted(words_dict, key=words_dict.get, reverse=True)[:5]
    return top5_list


if __name__ == '__main__':
    parsed_args = create_parser()
    args = parsed_args.parse_args()
    file = make_a_list(load_text_from_file(args.filepath))
    print("The most frequent word is")
    for i in get_most_frequent_words(count_words(file)):
        print(i)

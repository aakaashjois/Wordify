import phonenumbers
from phonenumbers import NumberParseException
from nltk.corpus import words


def map_all_words_to_numbers():
    words_list = words.words()
    words_list = set(list(filter(lambda x: len(x) <= 10, words_list)))
    nums = list(map(words_to_number, words_list))
    word_num_map = dict()
    for w, n in zip(words_list, nums):
        w = w.upper()
        if n in word_num_map.keys():
            word_num_map[n].append(w)
        else:
            word_num_map[n] = [w]
    return word_num_map


ALL_WORDS_NUM = map_all_words_to_numbers()


def perform_validation(num):
    try:
        parsed = phonenumbers.parse(num, 'US')
        return phonenumbers.is_valid_number(parsed)
    except ModuleNotFoundError:
        return False
    except NumberParseException:
        return False


def validate_number(num):
    if num[0] == '+' and len(num[1:]) == 11:
        return perform_validation(num)
    elif len(num) == 11:
        return perform_validation('+' + num)
    elif len(num) == 10:
        return perform_validation(num)
    else:
        return False


def parse_number(num):
    chunks = []
    i = 0
    total = len(num)
    temp = ''
    while i < total:
        if num[i] == '0' or num[i] == '1':
            chunks += [temp] if temp != '' else []
            chunks += [num[i]]
            temp = ''
        else:
            temp += num[i]
        i += 1
    chunks += [temp] if temp != '' else []
    return chunks


def words_to_number(num):
    return phonenumbers.convert_alpha_characters_in_number(num)


def number_to_words(num):
    if num in ALL_WORDS_NUM.keys():
        return ALL_WORDS_NUM[num]
    else:
        return []

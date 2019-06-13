import ast
import phonenumbers
from phonenumbers import NumberParseException


with open('../utils/words.txt', 'r') as words:
    ALL_WORDS_NUM = ast.literal_eval(words.read())


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

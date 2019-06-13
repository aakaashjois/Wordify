from constants import ALL_WORDS_NUM

import phonenumbers
from phonenumbers import NumberParseException


def parse_number(number):
    number = number.replace('-', '')
    number = number.replace('(', '')
    number = number.replace(')', '')
    number = number.replace(' ', '')
    return number


def validate_number(number):
    def perform_validation(number):
        try:
            parsed = phonenumbers.parse(number, 'US')
            return phonenumbers.is_valid_number(parsed)
        except ModuleNotFoundError:
            return False
        except NumberParseException:
            return False

    if number[0] == '+' and len(number[1:]) == 11:
        return perform_validation(number)
    elif len(number) == 11:
        return perform_validation('+' + number)
    elif len(number) == 10:
        return perform_validation(number)
    else:
        return False


def make_chunks(number):
    chunks = []
    for chunk_size in range(1, len(number) + 1):
        for index in range(len(number) - chunk_size + 1):
            chunk = number[index: index + chunk_size]
            if chunk in ALL_WORDS_NUM.keys():
                chunks.append([chunk, index])
    return chunks


def get_all_combinations(number, chunks):
    def index_not_used(index, length, used_indices):
        for i in range(index, index + length):
            if i in used_indices:
                return False
        for i in range(index, index + length):
            used_indices.append(i)
        return True

    def number_to_word_combination(subsets, number, combinations, used_indices):
        temp_used_indices = used_indices.copy()
        for i in range(0, len(subsets)):
            used_indices = temp_used_indices.copy()
            chunk, index = subsets[i]

            if index_not_used(index, len(chunk), used_indices):
                for word in ALL_WORDS_NUM[chunk]:
                    combination = number[0: index] + word + number[
                                                            index + len(word):]

                    if combination not in combinations:
                        combinations.append(combination)
                        number_to_word_combination(subsets, combination,
                                                   combinations,
                                                   used_indices.copy())

    combinations = []
    used_indices = []
    number_to_word_combination(chunks, number, combinations, used_indices)
    return combinations

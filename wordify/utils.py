from .constants import ALL_WORDS_NUM

import phonenumbers
from phonenumbers import NumberParseException


def parse_number(number: str) -> str:
    """
    Removes unnecessary characters from the phone number
    :param number: (str) phone number
    :return: (str) parsed phone number
    """
    return number.replace('-', '') \
        .replace('(', '') \
        .replace(')', '') \
        .replace(' ', '')


def validate_number(number: str) -> bool:
    """
    Checks if the number entered is a valid US phone number based on the
    length and by using phonenumbers library
    :param number: (str) phone number
    :return: (bool) result of the validation
    """

    def perform_validation(number: str) -> bool:
        """
        Use phonenumbers to check if the number given is valid
        :param number: (str) phone number
        :return: (bool) the result of the validation
        """
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


def make_chunks(number: str) -> list:
    """
    Splits the entered phone number into subsets of sizes varying from 1 to
    the total length of phone number
    :param number: (str) phone number
    :return: (list) list containing the chunk and its start index in the phone
    number
    """
    chunks = []
    for chunk_size in range(1, len(number) + 1):
        for index in range(len(number) - chunk_size + 1):
            chunk = number[index: index + chunk_size]
            if chunk in ALL_WORDS_NUM.keys():
                chunks.append([chunk, index])
    return chunks


def get_all_combinations(number: str, chunks: list) -> list:
    """
    For a given number and its chunks, create all possible combinations of words
    and number
    :param number: (str) phone number
    :param chunks: (list) subsets of phone number
    :return: (list) combinations of words and numbers
    """

    def index_not_used(index: int, length: int, used_indices: list) -> bool:
        """
        Check if the index is already used for creating a word
        :param index: (int) the index at which the check happens
        :param length: (int) the length of the word to create
        :param used_indices: (list) list containing the all the indices which
        have been used
        :return: (bool) The boolean which tells if the index is already used
        """
        for i in range(index, index + length):
            if i in used_indices:
                return False
        used_indices.extend(iter(range(index, index + length)))
        return True

    def number_to_word_combination(chunks: list,
                                   number: str,
                                   combinations: list,
                                   used_indices: list) -> None:
        """
        Recursively creates all the possible combinations of chunks and numbers
        :param chunks: (list) all the subsets of the phone number
        :param number: (str) phone number
        :param combinations: (list) all the combinations created
        :param used_indices: (list) list containing the all the indices which
        have been used
        :return: None
        """
        temp_used_indices = used_indices.copy()
        for i in range(len(chunks)):
            used_indices = temp_used_indices.copy()
            chunk, index = chunks[i]

            if index_not_used(index, len(chunk), used_indices):
                for word in ALL_WORDS_NUM[chunk]:
                    combination = (number[:index] + word + number[
                        index + len(word):])

                    if combination not in combinations:
                        combinations.append(combination)
                        number_to_word_combination(chunks, combination,
                                                   combinations,
                                                   used_indices.copy())

    combinations = []
    used_indices = []
    number_to_word_combination(chunks, number, combinations, used_indices)
    return combinations

from utils import validate_number, parse_number
from utils import make_chunks, get_all_combinations
from constants import ALL_WORDS_NUM
from random import choice
import sys
import phonenumbers


def all_wordifications(number: str) -> None:
    """
    Prints all possible combinations of numbers and english words for the given
    phone number
    :param number: (str) phone number
    :return: None
    """
    if any(n.isalpha() for n in number):
        sys.exit('Number already contains words.')
    chunks = make_chunks(number)
    combinations = get_all_combinations(number, chunks)
    print('All combinations of words and number for {}:'.format(number))
    print(', '.join(combinations))


def number_to_words(number: str) -> None:
    """
    Prints a transformed version of the phone number which contains part of or
    complete number transformed into an english word
    :param number: (str) phone number
    :return: None
    """
    chunks = make_chunks(number)
    largest_chunk, index = chunks[-1]
    combinations = []
    for word in ALL_WORDS_NUM[largest_chunk]:
        combination = number[0: index] + word + number[index + len(word):]
        combinations.append(combination)
    print('The number {} can be wordified to {}'.format(number,
                                                        choice(combinations)))


def words_to_number(number: str) -> None:
    """
    Converts a number which contains english words or letters to digits
    :param number: (str) phone number
    :return: None
    """
    converted = phonenumbers.convert_alpha_characters_in_number(number)
    print('The number {} can be dewordified to {}'.format(number, converted))


if __name__ == '__main__':
    phone_number = input('Enter the phone number\n')
    phone_number = parse_number(phone_number)
    if not validate_number(phone_number):
        sys.exit('Invalid US phone number.')
    functions = {'1': number_to_words,
                 '2': words_to_number,
                 '3': all_wordifications}
    function = input('''What would you like to perform?
    1. Number to words
    2. Words to number
    3. All wordifications\n''')
    try:
        functions[function](phone_number)
    except KeyError:
        sys.exit('Invalid option selected.')

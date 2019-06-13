from utils import validate_number, make_chunks, get_all_combinations
from constants import ALL_WORDS_NUM
from random import choice
import sys
import phonenumbers


def all_wordifications(number):
    if not validate_number(number):
        sys.exit('Invalid US phone number.')
    if any(n.isalpha() for n in number):
        sys.exit('Number already contains words.')
    chunks = make_chunks(number)
    combinations = get_all_combinations(number, chunks)
    print('All combinations of words and number for {}:'.format(number))
    print(', '.join(combinations))


def number_to_words(number):
    if not validate_number(number):
        sys.exit('Invalid US phone number.')
    chunks = make_chunks(number)
    largest_chunk, index = chunks[-1]
    combinations = []
    for word in ALL_WORDS_NUM[largest_chunk]:
        combination = number[0: index] + word + number[index + len(word):]
        combinations.append(combination)
    print('The number {} can be wordified to {}'.format(number,
                                                        choice(combinations)))


def words_to_number(number):
    if not validate_number(number):
        sys.exit('Invalid US phone number.')
    converted = phonenumbers.convert_alpha_characters_in_number(number)
    print('The number {} can be dewordified to {}'.format(number, converted))


if __name__ == '__main__':
    phone_number = '+1347FICO023'
    all_wordifications(phone_number)

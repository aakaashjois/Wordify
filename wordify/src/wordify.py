import string
import itertools


class Wordify:

    def __init__(self, number: str) -> None:
        self.has_country_code = False
        self.combinations = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno',
                             'pqrs', 'tuv', 'wxyz']
        self.number = number
        self.all_perms = list()

    def preprocess_number(self) -> str:
        number = self.number.translate(str.maketrans('', '',
                                                     string.punctuation))
        if number[0] == '1' and len(number) == 11:
            self.has_country_code = True
            number = number[1:]
        if len(number) < 10 or len(number) > 11:
            raise ValueError(
                '{} is not a valid US phone number.'.format(number))
        return number

    def get_all_words(self):
        num_list = self.parse_number()
        comb = [self.combinations[num] for num in num_list]
        temp = [comb[0]]
        for i in range(1, len(comb)):
            temp.append(comb[i])
            self.all_perms = self.all_perms + list(map(lambda x: ''.join(x),
                                                       itertools.product(
                                                           *temp)))

    def parse_number(self):
        return list(map(int, self.number))


if __name__ == '__main__':
    ph_num = '18007246837'
    wordify = Wordify(ph_num)
    wordify.preprocess_number()
    wordify.get_all_words()
    print(wordify.all_perms)

import string


class Wordify:

    def __init__(self, number: str) -> None:
        self.has_country_code = False
        self.combinations = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs',
                             'tuv', 'wxyz']
        self.number = number

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


if __name__ == '__main__':
    ph_num = '1800734653'
    wordify = Wordify(ph_num)
    print(wordify.preprocess_number())

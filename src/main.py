import re
import sys
from abc import ABCMeta, abstractmethod

from pdfminer.high_level import extract_text


class Validator():
    __metaclass__ = ABCMeta

    @abstractmethod
    def is_valid(self, text):
        raise NotImplementedError()


class KeywordValidator(Validator):
    def __init__(self, keyword):
        self._keyword = keyword

    def is_valid(self, text):
        return self._keyword in text


class PatternValidator(Validator):
    def __init__(self, pattern):
        self._pattern = pattern

    def is_valid(self, text):
        return bool(re.compile(self._pattern).search(text))


def contains_keyword(text, keyword):
    return keyword in text


def contains_pattern(text, pattern):
    return re.compile(pattern).search(text)


def parse_local_cv(email):
    return extract_text(f'../cvs/{email}.pdf')


def main(emails):
    valid_mails = []
    for email in emails:
        if not KeywordValidator('python').is_valid(parse_local_cv(email).lower()):
            continue
        if not PatternValidator(r"\(?\d+\)?\s*\d+\-*\d+").is_valid(parse_local_cv(email).lower()):
            continue
        valid_mails.append(email)
    return valid_mails


if __name__ == '__main__':
    if len(sys.argv) > 1:
        mails = main(sys.argv[1:])
        print('\n'.join(mails))
    else:
        print("Envie pelo menos 1 email na saída")
        sys.exit(1)

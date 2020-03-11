import re
import sys
from abc import ABCMeta, abstractmethod

from pdfminer.high_level import extract_text


class Validator():
    __metaclass__ = ABCMeta

    @abstractmethod
    def is_valid(self, text):
        raise NotImplementedError()


class PatternValidator(Validator):
    def __init__(self, pattern):
        self._pattern = pattern

    def is_valid(self, text):
        return bool(re.compile(self._pattern).search(text))


def parse_local_cv(email):
    return extract_text(f'../cvs/{email}.pdf')


def is_valid(text, validators):
    return all(validator.is_valid(text) for validator in validators)


def main(emails, validators):
    return [
        email for email in emails
        if is_valid(parse_local_cv(email).lower(), validators)
    ]


VALIDATORS = {
    'python': (
        PatternValidator('python'),
        PatternValidator(r"\(?\d+\)?\s*\d+\-*\d+"),
    )
}


def available_validators():
    return ','.join(VALIDATORS.keys())


if __name__ == '__main__':
    if len(sys.argv) > 2:
        validation = sys.argv[1]
        if validation not in VALIDATORS:
            print(f"Validação desconhecida. Validações disponíveis: {available_validators()}")
            sys.exit(1)
        mails = main(sys.argv[2:], VALIDATORS[validation])
        print('\n'.join(mails))
    else:
        print("Envie pelo menos 1 email na saída")
        sys.exit(1)

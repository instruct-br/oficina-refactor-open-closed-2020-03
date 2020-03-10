import re
import sys

from pdfminer.high_level import extract_text


def contains_python(text, keyword='python'):
    return keyword in text


def contains_number(text):
    return re.compile(r"\(?\d+\)?\s*\d+\-*\d+").search(text)


def parse_local_cv(email):
    return extract_text(f'../cvs/{email}.pdf')


def main(emails):
    valid_mails = []
    for email in emails:
        if not contains_python(parse_local_cv(email).lower()):
            continue
        if not contains_number(parse_local_cv(email).lower()):
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

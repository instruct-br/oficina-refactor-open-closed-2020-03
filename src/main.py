import re
import sys

from pdfminer.high_level import extract_text


def contains_python(text):
    return 'python' in text


def contains_number(text):
    return re.compile(r"\(?\d+\)?\s*\d+\-*\d+").search(text)


def main(emails):
    valid_mails = []
    for email in emails:
        cv_txt = extract_text(f'../cvs/{email}.pdf')
        if not contains_python(cv_txt.lower()):
            continue
        if not contains_number(cv_txt.lower()):
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

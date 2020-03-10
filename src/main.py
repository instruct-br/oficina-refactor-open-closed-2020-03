import re
import sys

from pdfminer.high_level import extract_text


def main(emails):
    valid_mails = []
    phone_regex = re.compile(r"\(?\d+\)?\s*\d+\-*\d+")
    for email in emails:
        cv_txt = extract_text(f'../cvs/{email}.pdf')
        if 'python' not in cv_txt.lower():
            continue
        if not phone_regex.search(cv_txt.lower()):
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

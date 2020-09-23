import re

def abbreviate(words):
    # acronym = ''
    # delchars = ''.join(c for c in map(chr, range(256)) if not c.isalnum())
    # for i in words.split():
    #     if i == '-':
    #         continue
    #     for hypen in i.split('-'):
    #         acronym += hypen.translate(str.maketrans('', '', delchars)).upper()[0]
    # return acronym

    return ''.join((x[0] for x in re.split(r'[-_\s]', words) if len(x))).upper()
'''Read a text file, make sure everything is one case, remove all punctuation,
and write the words one per line to a second file.
'''

def main():
    with open('.\quick-python\ch6\moby_01.txt') as infile, \
        open('.\quick-python\ch6\moby_01_clean.txt', 'w') as outfile:
        for line in infile:
            translate_table = line.maketrans('.-,;','    ')
            outfile.write('\n'.join(line.translate(translate_table).lower().split()))
            outfile.write('\n')

if __name__ == '__main__':
    main()
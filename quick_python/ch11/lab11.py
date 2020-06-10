
'''Refactor lab8 to be more like the UNIX wc utility with command line argument passing 

   example test: python ./quick_python/ch11/lab11.py quick_python/ch8/word_count.tst
'''

from argparse import ArgumentParser

def count_words(command_args):
    longest = 0
    char_count, word_count, line_count = 0, 0, 0
    with open(command_args.path) as infile:
        for index, line in enumerate(infile):
            clean_line = line.rstrip('\n')
            char_count += len(clean_line)
            word_count += len(clean_line.split())
            line_count = index + 1
            longest = max(longest, len(line))

    if not command_args.characters and not command_args.lines and not command_args.words:
        print("File has {0} lines, {1} words, {2} characters".format(line_count, word_count, char_count))
    if command_args.characters:
        print("File has {0} characters".format(char_count))
    if command_args.lines:
        print("File has {0} lines".format(line_count))
    if command_args.words:
        print("File has {0} words".format(word_count))
    if command_args.longest_line:
        print("The longest line in the file has a length of: {0}".format(longest))

def main():
    parser = ArgumentParser()
    parser.add_argument('path', type=str, help='File path to read words')
    parser.add_argument('-l', '--lines', action='store_true', default=False, help='count lines')
    parser.add_argument('-w', '--words', action='store_true', default=False, help='count words')
    parser.add_argument('-c', '--characters', action='store_true', default=False, help='count characters')
    parser.add_argument('-L', '--longest_line', action='store_true', default=False, help='longest line length')
    args = parser.parse_args()

    print('arguments: ', args)

    count_words(args)

if __name__ == '__main__':
    main()
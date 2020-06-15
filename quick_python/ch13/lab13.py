
'''Rewrite the wc utility to implement both the distinction betwee bytes and characters and the ability 
to read from files and standard input
   example test: python ./quick_python/ch11/lab11.py quick_python/ch8/word_count.tst
'''

from argparse import ArgumentParser
import sys


def count_words(command_args):
    longest = 0
    char_count, word_count, line_count, byte_count = 0, 0, 0, 0


    if command_args.path != 'None':
        with open(command_args.path) as infile:
            for index, line in enumerate(infile):
                clean_line = line.rstrip('\n')
                char_count += len(clean_line)
                word_count += len(clean_line.split())
                line_count = index + 1
                longest = max(longest, len(line))
                byte_count += len(str.encode(clean_line))
    else:
        print('No path specified, reading from stdin: \n')
        with sys.stdin.read() as infile:
            for index, line in enumerate(infile):
                clean_line = line.rstrip('\n')
                char_count += len(clean_line)
                word_count += len(clean_line.split())
                line_count = index + 1
                longest = max(longest, len(line))
                byte_count += len(str.encode(clean_line))

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
    if command_args.bytes:
        print("File has {0} bytes".format(byte_count))

def main():
    parser = ArgumentParser()
    parser.add_argument('-path', type=str, default='None', help='File path to read words')
    parser.add_argument('-l', '--lines', action='store_true', default=False, help='count lines')
    parser.add_argument('-w', '--words', action='store_true', default=False, help='count words')
    parser.add_argument('-c', '--characters', action='store_true', default=False, help='count characters')
    parser.add_argument('-L', '--longest_line', action='store_true', default=False, help='longest line length')
    parser.add_argument('-b', '--bytes', action='store_true', default=False, help='count bytes')

    args = parser.parse_args()

    count_words(args)

if __name__ == '__main__':
    main()
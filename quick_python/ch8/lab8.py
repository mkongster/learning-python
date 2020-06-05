'''Reads a file and returns the number of lines, words,
   and characters - similar to the UNIX wc utility.
   Refactor the original code from quick-python book pg.111: 

infile = open('word_count.tst')

lines = infile.read().split("\n")

line_count = len(lines)

word_count = 0
char_count = 0

for line in lines:
    words = line.split()
    word_count += len(words)

    char_count += len(line)

print("File has {0} lines, {1} words, {2} characters".format
    (line_count, word_count, char_count))
'''


def main():
    char_count, word_count, line_count = 0, 0, 0
    with open('quick_python/ch8/word_count.tst') as infile:
        for index, line in enumerate(infile):
            clean_line = line.rstrip('\n')
            char_count += len(clean_line)
            word_count += len(clean_line.split())
            line_count = index + 1

    print("File has {0} lines, {1} words, {2} characters".format(line_count, word_count, char_count))       
            

if __name__ == '__main__':
    main()
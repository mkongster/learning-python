'''Read a text file, make sure everything is one case, remove all punctuation,
and write the words one per line to a second file.
'''

def clean_text(output_file=True): 
    output = []
    with open('quick_python\ch6\moby_01.txt') as infile, \
        open('quick_python\ch6\moby_01_clean.txt', 'w') as outfile:
        for line in infile:
            translate_table = line.maketrans('.-,;','    ')
            if output_file:
                outfile.write('\n'.join(line.translate(translate_table).lower().split()))
                outfile.write('\n')
            else:
                output.extend(line.translate(translate_table).lower().split())
    
    if not output_file:
        return output

def main():
    print(clean_text(False))

if __name__ == '__main__':
    main()
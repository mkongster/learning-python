from sys import getsizeof

class IntBits(int):
    def __init__(self):
        self.bit_string = 1
    
    def add(self, bit):
        self.bit_string <<= 2
        self.bit_string |= bit

    def __getitem__(self, i):
        if self.bit_string == 1:
            raise IndexError
        value = self.bit_string & 0b11
        self.bit_string >>= 2
        return value
    
    def __len__(self):
        return len(self.bit_string)


class CompressedGene:
    def __init__(self, gene):
        self.bits = IntBits()
        self.nucleotide_dict = {
            'A': 0b00,
            'C': 0b01,
            'G': 0b10,
            'T': 0b11
        }
        self.inv_dict = {v: k for k, v in self.nucleotide_dict.items()}
        self._compress(gene)
    
    def _compress(self, gene):
        for nucleotide in gene.upper():
            self.bits.add(self.nucleotide_dict[nucleotide])

    def decompress(self):
        gene = ''
        for i in self.bits:
            gene += self.inv_dict[i]
        return gene[::-1]


def main():
    original = 'ACGT'
    print('original is {} bytes'.format(getsizeof(original)))
    compressed = CompressedGene(original)
    print('compressed is {} bytes'.format(getsizeof(compressed.bits.bit_string)))
    print('original and decompressed are the same: {}'.format(original == compressed.decompress()))

if __name__ == "__main__":
    main()
class LCGRandom:

    def __init__(self):
        # self.oldseed = int(round(time.time() * 1000))
        self.oldseed = 1000
        self.mask = (1 << 48) - 1
        self.multiplier = 0x5DEECE66D
        self.addend = 0xB
        self.requierd_bits = 32
        sum_bits = ""
        zero_str = "0"
        for i in range(100000):
            result = self.next(self.requierd_bits)
            print(result)
            text_bits = '{0:b}'.format(result)
            while len(text_bits) < self.requierd_bits:
                text_bits = zero_str + text_bits
            sum_bits += text_bits

        file = open('/Users/truffy/Documents/Python/projects/PRNG_Lab/result.txt', 'w')
        file.write(sum_bits)
        file.close()

    def next(self, bits):
        self.nextseed = (self.oldseed * self.multiplier + self.addend) % self.mask
        self.oldseed = self.nextseed
        return self.nextseed >> (48 - bits)


if __name__ == '__main__':
    LCGRandom()
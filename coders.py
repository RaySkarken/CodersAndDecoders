from string import ascii_lowercase
from typing import Tuple

from math import log2, ceil

from utils import float_bin

class BWT_MTF:
    def __init__(self, alphabet_or_msg=None):
        if alphabet_or_msg is None:
            alphabet_or_msg = list(ascii_lowercase)
        alphabet_or_msg = list(alphabet_or_msg)
        assert len(alphabet_or_msg) == len(set(alphabet_or_msg)), "Alphabet must not contain duplicates"
        self.alphabet = alphabet_or_msg

    def bwt(self, s) -> Tuple[str, int]:
        """Apply Burrows-Wheeler transform to input string."""

        table = sorted(s[i:] + s[:i] for i in range(len(s)))  # Table of rotations of string
        last_column = [row[-1:] for row in table]  # Last characters of each row
        return "".join(last_column), table.index(s)  # Convert list of characters into string

    def move2front_encode(self, strng):
        sequence, pad = [], self.alphabet[:]
        for char in strng:
            indx = pad.index(char)
            sequence.append(indx)
            pad = [pad.pop(indx)] + pad
        return sequence

    def ibwt(self, r, idx):
        """Apply inverse Burrows-Wheeler transform."""
        table = [""] * len(r)  # Make empty table
        for _ in range(len(r)):
            table = sorted(r[i] + table[i] for i in range(len(r)))  # Add a column of r
        s = table[idx]  # Find the correct row
        return s

    def move2front_decode(self, sequence):
        chars, pad = [], self.alphabet[:]
        for indx in sequence:
            char = pad[indx]
            chars.append(char)
            pad = [pad.pop(indx)] + pad
        return ''.join(chars)

    def encode(self, msg):
        encoded, row = self.bwt(msg)
        self.row = row
        return self.move2front_encode(encoded), row

    def decode(self, encoded_m2f, row=None):
        if row is None:
            row = self.row
        decoded_m2f = self.move2front_decode(encoded_m2f)
        return self.ibwt(decoded_m2f, row)


class ShannonCoder:
    def __init__(self, alpha:list, probs: list):
        assert len(alpha) == len(probs)
        s_probs = sorted(probs, reverse=True)
        self.alpha_probs = sorted([(alpha[i], probs[i]) for i in range(len(alpha))], key=lambda x: -x[1])
        cumulative_frequency = [sum(s_probs[:i]) if i > 0 else 0.0 for i in range(len(s_probs))]
        lens = [ceil(-log2(p)) for p in s_probs]
        m_len = max(lens)
        cf_bin = [float_bin(p, places=m_len) for p in cumulative_frequency]
        self.alpha = list(map(lambda x: x[0], self.alpha_probs))
        self.codes = [x.split(".")[1][:l] for x, l in zip(cf_bin, lens)]
        self.alpha_to_code = {self.alpha[i]: self.codes[i] for i in range(len(self.alpha))}
        self.code_to_alpha = {self.codes[i]: self.alpha[i] for i in range(len(self.alpha))}

    def encode(self, string):
        res = ""
        for symbol in string:
            res += self.alpha_to_code[symbol]
        return res

    def decode(self, string):
        res = ""
        curr = ""
        for symbol in string:
            curr += symbol
            if curr in self.code_to_alpha:
                res += self.code_to_alpha[curr]
                curr = ""
        return res

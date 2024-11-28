"""
Created on 11/4/2024
@author:   Aidan Miller, Nicholas Tenebruso
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 6
"""

# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2**COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.


def numToBinary(n):
    """
    Converts decimal number n to binary, using the specified number of bits
    """
    if n == 0:
        return ""
    else:
        return numToBinary(n // 2) + str(n % 2)


def fixBits(s, bits):
    """
    Alters binary string s to match the specified number of bits
    """
    if len(s) == bits:
        return s
    elif len(s) < bits:
        return ("0" * (bits - len(s))) + s
    elif len(s) > bits:
        if s[0] == "1":
            return "1" * bits
        else:
            return fixBits(s[1:], bits)


def binaryToNum(s):
    """
    Converts binary string s to its decimal representation
    """
    if len(s) == 0:
        return 0
    elif s[0] == "1":
        return (2 ** (len(s) - 1)) + binaryToNum(s[1:])
    else:
        return binaryToNum(s[1:])


def countOccurrence(s, char, maxLen, currLen=0):
    """
    Returns the number of consecutive occurrences of char at the start of s. If maxLen is exceeded, returns 0.
    """
    if s == "":
        return 0
    elif currLen >= maxLen:
        return 0
    elif s[: len(char)] != char:
        return 0
    else:
        return 1 + countOccurrence(s[len(char) :], char, maxLen, currLen + 1)


# The largest number of bits the compress algorithm could produce,
# given a 64-bit string, would be 320 bits, as if there were only
# alternating ones and zeores, there would be five bits encoded for
# every bit in the unencoded string.


def compress(S):
    """
    Compresses binary string S using run-length encoding
    """

    def compHelp(s, char):
        """
        Compresses binary string S using run-length encoding. Uses "char" parameter to keep track of whether "0" or "1" is being searched for.
        """
        if s == "":
            return ""

        res = fixBits(
            numToBinary(countOccurrence(s, char, MAX_RUN_LENGTH)),
            COMPRESSED_BLOCK_SIZE,
        )

        if char == "0":
            return res + compHelp(s[countOccurrence(s, char, MAX_RUN_LENGTH) :], "1")
        elif char == "1":
            return res + compHelp(s[countOccurrence(s, char, MAX_RUN_LENGTH) :], "0")

    return compHelp(S, "0")


def uncompress(S):
    """
    Decompresses binary string S encoded with run-length encoding
    """

    def uncompHelp(s, char):
        """
        Decompresses binary string S encoded with run-length encoding. Uses "char" parameter to keep track of whether "0" or "1" is being searched for.
        """
        if s == "":
            return ""

        res = binaryToNum(s[:COMPRESSED_BLOCK_SIZE]) * char

        if char == "0":
            return res + uncompHelp(s[COMPRESSED_BLOCK_SIZE:], "1")
        elif char == "1":
            return res + uncompHelp(s[COMPRESSED_BLOCK_SIZE:], "0")

    return uncompHelp(S, "0")


def compression(S):
    """
    Returns the compression ratio between S encoded with run-length encoding, and uncompressed S
    """
    return len(compress(S)) / len(S)


def test_compress():
    """
    Tests the compress function
    """
    # RATIO: 1.484375
    penguin = (
        "00011000" + "00111100" * 3 + "01111110" + "11111111" + "00111100" + "00100100"
    )
    assert (
        compress(penguin)
        == "00011000100010100100001000010000100001000001100110000010100000010001000010000001000100000100010"
    )

    # RATIO: 1.328125
    smile = (
        "0" * 8
        + "01100110" * 2
        + "0" * 8
        + "00001000"
        + "01000010"
        + "01111110"
        + "0" * 8
    )
    assert (
        compress(smile)
        == "0100100010000100001000010000100001000010011010000100100000010010000001000100011001001"
    )

    # RATIO: 1.015625
    five = (
        "1" * 9
        + "0" * 7
        + "10000000" * 2
        + "1" * 7
        + "0"
        + "00000001" * 2
        + "1" * 7
        + "0"
    )
    assert (
        compress(five)
        == "00000010010011100001001110000100111001110100000001001110100000001"
    )


# Professor Lai would be incorrect, because if every character is
# unique and there is no pattern, the minimum that an algorithm
# could compress it would be exactly the same length, never shorter.
# Therefore, an compression algorithm will not ALWAYS be able to
# shorten the original text. At minimum, the algorithm will compress
# it to be the same length as the original.

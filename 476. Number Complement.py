"""
Promblem:

Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.


Note:
    任何二进制数和1111按位异都是该数字的互补数字
    比如
    (101)表示5
    (111)
    (010)得到5的互补数字是3


算法：
    1.得到与n的位数相同的1111
    2.与1111取异
"""
def numComplement(n):
    # 1.得到与n的二进制位数相同的111
    lenth = len(bin(n))-2
    compareN = 2 ** lenth -1
    # 2.让111与数字n取异
    complementN = compareN ^ n
    return complementN

def numComplement2(num):
    i = 1
    while i <= num:
        i = i << 1
    return (i - 1) ^ num


def test():
    n = 8
    m = numComplement2(n)
    print(bin(n),"的互补的二进制数是：",bin(m))


if __name__ == '__main__':
    test()
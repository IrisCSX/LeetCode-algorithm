"""
Problem:

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?

判断n是不是4的幂？

①、4的幂首先是2的幂，因为4^n = （2^2）^n，故可以先判断是否为2的幂，同样利用n & (n - 1);

②、唯一的不同是，4的幂的二进制表示中，1全奇数位上。

算法：
1.它是2的幂：n & (n-1) == 0
2.它的1在奇数位（长度为奇数）
"""
def isPowerOfFour(n):
    if n < 0:
        return False
    isPowerOfTwo = (n & (n-1) == 0)
    isLenOdd = len(bin(n))%2 != 0
    isPowerOf4 = isPowerOfTwo and isLenOdd
    return  isPowerOf4


def test():
    n = 1
    isPowerOf4 = isPowerOfFour(n)
    print('是4的幂吗：',isPowerOf4)


if __name__ == '__main__':
    test()

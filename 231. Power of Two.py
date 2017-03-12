'''
Given an integer, write a function to determine if it is a power of two.

Note:
    法1：
    一直除以2，直到不能被2整除，如果是2的幂，最后的值是1；如果不是，就不是1
    法2：
    判断n是否为2的幂？

    任何整数乘以2，都相当于向左移动了一位，而2的0次幂为1，所以2的n次幂就是1向左移动n位。这样，2的幂的特征就是二进制表示只有最高位为1，其他位均为0。那么，我们只要判断一个数的二进制表示只有一个1，那么它就是2的幂。
    n为整数，则n & (n - 1)可以消除n二进制表示的最低位的1，这个方法可以用来统计一个数二进制中1的个数，当然也可以用来判断是否为2的幂

    解释;n & (n-1)
    用n = 00101100 举例.（&是取每个位置的最小值）
    n = 00101100               n - 1 = 00101011
    n & (n - 1) = 00101100 & 00101011 = 00101000
    2的幂的二进制是1开头后面全是0，所以n & (n-1) = 0
'''


def isPowerOfTwo1(n):
    """
    可以延伸至3的幂，4的幂。。。
    :param n:
    :return:
    """
    if n <= 0:
        return False

    while n % 2 == 0:
        n = n / 2

    return n == 1


def isPowerOfTwo2(n):
    if n <= 0:
        return False
    if n & (n-1) == 0:
        return True
    return  False

def test():
    n = 44
    m = isPowerOfTwo2(n)
    print('是2的幂吗？：', m)

if __name__ == '__main__':
    test()
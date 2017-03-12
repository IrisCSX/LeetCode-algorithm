"""
Problem

Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

判断整型数据n是不是3的幂？

①、3的幂的特点：如果一个整数N是3的幂，那么其所有约数都是3的幂。那么，换一个角度，如果n小于N且是N的约数，那么其一定是3的幂；

②、int型数据最大值为2^31-1 = 2147483647 = 0x7fffffff，则int型数据中3的最大幂如下：

int max = (int) Math.pow(3, (int) (Math.log(0x7fffffff) / Math.log(3)));
③、最后判断整数n是不是max的约数，如下即可。

max % n == 0;
"""

import sys

def isPowerOfThree(n):
    max_int = sys.maxsize
    maxPowerOf3 = Math.pow(3,int(Math.log(max_int)/Math.log(3)))
    isPowerOf3 = maxPowerOf3 % n == 0
    return isPowerOf3


def test():
    n = 4
    m = isPowerOfThree(n)
    print("是3的幂吗：",m)


if __name__ == '__main__':
    test()
"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
----------------------------------------------------------------------------------------------
Note:
1. n & (n-1)的作用：（把最右边的1变成0）
    假设Value=X1X2……Xn-1Xn，其中Xi(1≤i≤n)为1或0
　　不妨设Xi是最右边的1，那么Value就可以写成如下的形式
　　Value=X1X2……Xi-1Xi0……0，其中(1≤i≤n)，Xi后面有n-i个0
　　因为Xi=1，所以Value=X1X2……Xi-110……0，其中(1≤i≤n)，1后面有n-i个0
　　则Value-1=X1X2……Xi-101……1，其中(1≤i≤n)，0后面有n-i个1
　　则Value And (Value-1)=X1X2……Xi-100……0，其中(1≤i≤n)，Xi-1后面有n-i+1个0
　　因此，Value And (Value-1)的效果把最右边的1变成0
　　在上面的代码中，每把最右边的1变成0，则统计数加1，直到所有的1变成0为止。
2. ^用法;
    2^4 表示把他们的二进制进行比较，不同的取1，相同的取0
    (010)表示2
    (100)表示4
    (110)表示2^4
"""
def Distance(x,y):
    # 1. 标记两个数的不同值
    xor = x ^ y

    # 2. 二进制中1的个数
    count = 0
    while xor:
        xor = xor & (xor - 1)
        count += 1
    return count

def test():
    n = 2
    m = 4
    Dis = Distance(n,m)
    print(n,"和",m,"的距离是",Dis)


if __name__ == '__main__':
    test()
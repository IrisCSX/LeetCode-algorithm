"""
题型：根据位置索引有3个不同的值选项。
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number
and for the multiples of five output “Buzz”.
For numbers which are multiples of both three and five output “FizzBuzz”.

Note：
or逻辑运算：	x or y	布尔"或"	- 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。	(a or b) 返回 10。
"""
def fizzOrBuzz(n):
    list = ['Fizz'*(not i%3)+'Buzz'*(not i%5) or str(i) for i in range(1,n+1)]
    return list


def test():
    n = 5
    FizzOrBuzz = fizzOrBuzz(n)
    print("Fizz! OR BUZZ!",FizzOrBuzz)

if __name__ == '__main__':
    test()

"""
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

Note:
    法1：
        反向的切片
    法2：
        把str转成list，用list的方法reverse转向

"""
def ReverseStr1(str):
    reverStr = str[::-1]
    return reverStr


def ReverseStr2(str):
    strList = list(str)
    strList.reverse()
    reverStr = ''.join(strList)
    return reverStr


def test():
    str = 'asdfg'
    reverStr = ReverseStr2(str)
    print(str,'翻转成：',reverStr)


if __name__ == '__main__':
    test()
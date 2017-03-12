'''
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Note:
    1.空格切片生成list ：[the,sky,is,blue]
    2.翻转list中的元素 [blue,is,sky,the]
    3.将翻转后的list转化成字符串，空格为间隔 "blue is sky the"
'''

def reverseWords(str):
    str_list = str.strip().split()
    reverse_str_list = str_list[::-1]
    reverse_str = " ".join(reverse_str_list)
    return reverse_str


def test():
    s = 'the sky is blue'
    re_s = reverseWords(s)
    print('原字符串:', s, '翻转字符串：', re_s)


if __name__ == '__main__':
    test()
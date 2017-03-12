"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.

思路：
    集合：无序、元素不重复
    1.把键盘上的三行放三个集合
    2.遍历每一个字符串，查看是否是集合的子集合
"""
def keyRow(words):
    keyboads = ['qwertyuiop','asdfghjkl','zxcvbnm']
    ans = []
    for word in words:
        setWord = set(word.lower())
        for keyboad in keyboads:
            setKeyboad = set(keyboad)
            if setWord.issubset(setKeyboad):
                ans.append(word)
    return ans


def test():
    words = ["Hello", "Alaska", "Dad", "Peace"]
    keyrow = keyRow(words)
    print('在同一行的单词有：',keyrow)

if __name__ == '__main__':
    test()
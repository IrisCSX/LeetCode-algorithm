"""
Count the number of prime numbers less than a non-negative number, n.

To find all the prime numbers less than or equal to 30, proceed as follows.

拿小于30的素数举例：
First generate a list of integers from 2 to 30:

 2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
The first number in the list is 2; cross out every 2nd number in the list after 2 by counting up from 2 in increments of 2 (these will be all the multiples of 2 in the list):

 2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
The next number in the list after 2 is 3; cross out every 3rd number in the list after 3 by counting up from 3 in increments of 3 (these will be all the multiples of 3 in the list):

 2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
The next number not yet crossed out in the list after 3 is 5; cross out every 5th number in the list after 5 by counting up from 5 in increments of 5 (i.e. all the multiples of 5):

 2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
The next number not yet crossed out in the list after 5 is 7; the next step would be to cross out every 7th number in the list after 7, but they are all already crossed out at this point, as these numbers (14, 21, 28) are also multiples of smaller primes because 7 × 7 is greater than 30. The numbers not crossed out at this point in the list are all the prime numbers below 30:

 2  3     5     7           11    13          17    19          23                29


 伪代码：此算法是小于等于n的素数。
 Input: an integer n > 1.

 Let A be an array of Boolean values, indexed by integers 2 to n,
 initially all set to true.

 for i = 2, 3, 4, ..., not exceeding √n:
   if A[i] is true:
     for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n:
       A[j] := false.

 Output: all i such that A[i] is true.
"""


def countPrimes(n):
    """
    下标和数字对应
    :param n:
    :return:
    """
    if n <= 2:
        return 0
    isPrime = [1] * n
    isPrime[0] = 0
    isPrime[1] = 0
    for i in range(2, int((n-1) ** 0.5) + 1):
        print("i是：",i)
        for j in range(i, int((n-1) / i) + 1):
            print("j是：",j)
            isPrime[i * j] = 0
    return sum(isPrime)


def test():
    n = 30
    pri_n = countPrimes(n)
    print('小于',n,'的素数有',pri_n,'个')

if __name__ == '__main__':
    test()
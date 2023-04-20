class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        abc = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                abc.append('FizzBuzz')
            elif i % 3 == 0:
                abc.append('Fizz')
            elif i % 5 == 0:
                abc.append('Buzz')
            else :
                abc.append(str(i))
        return abc

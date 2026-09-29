class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        fiz = []
        for i in range(1,n+1):
            if i%3==0 and i%5!=0:
                fiz.append("Fizz")
            elif i%5==0 and i%3!=0:
                fiz.append("Buzz")
            elif i%3==0 and i%5==0:
                fiz.append("FizzBuzz")
            else:
                fiz.append(str(i))
        return fiz
        
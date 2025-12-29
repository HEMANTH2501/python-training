'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
 class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            sumi=0
            while num>0:
                rem=num%10
                sumi+=rem
                num=num//10
            num=sumi
        return num       
        
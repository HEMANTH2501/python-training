'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
#leetcode 169 problem
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=0
        candidate=0
        for num in nums:
            if c==0:
                candidate=num
                c+=1
            elif candidate==num:
                c+=1
            else:
                c-=1
        return candidate

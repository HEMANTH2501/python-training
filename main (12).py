'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def kk(nums):
    k=[]
    s=""
    for num in nums:
        s+=str(num)
    i=int(s)+1
    z=str(i)
    for ch in z:
        k.append(int(ch))
    print(k)
nums=[9,9,9]
kk(nums)
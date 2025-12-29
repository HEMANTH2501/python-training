def reversewords(s):
        s=s.split()
        out=[]
        for i in range(len(s)):
            out.append(s.pop())
        return " ".join(out)   
        
s=input("Enter the string:")
print(reversewords(s))

# l1=[x for x in range(5)]
# print(sum(l1))


# a,b,s = -1,1,0
# for i in range(int(input("enter a range limit to print fibonacci series , n = "))):
#     s=a+b
#     print(s ,end=",")
#     a=b
#     b=s
    

# import math
# print(math.factorial(int(input("enter a no:"))))

# vowels=['a','e','i','o','u']
# consonants=[chr(x) for x in range(ord('a'),ord('z')+1) if chr(x) not in vowels]
# v=c=d=s=0
# str1=input("enter a string:-")
# str1=str1.lower()
# print(str1)
# for ch in str1 :
#     if ch in vowels:
#         v+=1    
#     elif ch in consonants :
#         c+=1
#     elif ch >= '0' and ch <='9' :
#         d+=1
#     else :
#          s+=1
# print('v=',v,'c=',c,'d=',d,'s=',s,sep=" ")

#print(input())
s=input("enter str").split()
d={x:len(x) for x in s}
print()
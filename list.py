# n=int(input("enter no "))
# l=[]
# for i in range(0,n):
#     x=int(input())
#     l.append(x)
# print(l)

# a=[10,23,4,5,5]
# # a.insert(2,200)
# # print(a)
# a.pop(-3)
# print(a)

# a.reverse()
# print(a)


# a=[1,2,3,4,5]
# for i in range(0,len(a)):
    
# n=5
# for i in range(1,n+1):
#     for j in range(n,i-1,-1):
#         print("*",end=" ")
#     print()
    
    


# n=5
# for i in range(1,n+1):
#     for j in range(1,i):
#         print(" ",end=" ")
#     for j in range(1,n-i+2):
#         print("*",end=" ")
#     print()


# n=5
# for i in range(1,n+1):
#     if(i%2==1):
#         for j in range(1,n-i+1):
#             print(j,end=" ")
#     else:
#         for j in range(n,i-2,-1):
#             print(n-i+2,end=" ")
#     print()


# n=5
# for i in range(1,n+1):
#     c=i
#     d=n-1
#     for j in range(1,i+1):
#         print(c,end=" ")
#         c=c+d
#         d-=1
#     print()

# def is_prime(c):
#     for i in range(2,c):
#         if(c%i==0):
#             return False
#     return True
# n=5
# for i in range(1,n+1):
#     c=2
#     j=1
#     while j<=i:
#         if is_prime(c):
#             print(c,end=" ")
#             j+=1
#         c+=1
#     print()


# n=5
# c=1
# for i in range(1,n+1):
#     d=c
#     for j in range(1,i+1):
#         print(d,end=" ")
#         d=d-1
#     c=c+i+1
#     print()
        

# n=5
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# n=n-1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(" ",end="")
#     for j in range(1,n-i+2):
#         print("*",end=" ")
#     print()



# n=5
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     for j in range(1,i):
#         print("*",end=" ")
#     print()

# a=[1,2,3,4,6]
# print(a)
# a.pop(1)
# print(a)


def min_find(l):
    m=float("inf")
    for i in l:
        if(i<m):
            m=i
    return m
def check(key,l):
    for i in l:
        if(i==key):
            return True
    return False
l=[6,8,10,22,12,67,20]
x=min_find(l)
key=x+1
c=0
while c<4:
    if not check(key,l):
        print(key,end=" ")
        c+=1
    key+=1

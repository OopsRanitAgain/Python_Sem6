def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

n = 10
for i in range(n):
   print(fibonacci(i))


"""Iterative Approach"""
print("Iterative Approach")

a,b=0,1

print(a)
for i in range(n):
    a,b= b,a+b
    print(a)
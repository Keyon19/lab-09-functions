def factorial(n):
    return n * (n-1) * (n-2) * (n-3)

userstr = input("Number please: ")
usernum = int(userstr)

print(factorial(usernum))

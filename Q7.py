

factorial = (lambda n: 1 if n==0 else n*factorial(n-1) )

num = int(input("Enter a number to find the factorial"))
result= factorial(num)
print("Factorial of ",num," is: ",result)
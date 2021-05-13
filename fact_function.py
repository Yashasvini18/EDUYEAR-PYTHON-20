def factorial(a):
    fact=1
    i=1
    while i<=a:
        fact=fact*i
        i=i+1
    print(fact)
a=int(input("Enter a number: "))
factorial(a)

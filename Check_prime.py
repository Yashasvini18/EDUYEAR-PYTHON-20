def check_prime(a):
    if a<=1:
        print("Neither prime nor composite")
    elif a==2:
        print("2 is prime")
    elif a>2:
        for i in range (2,a):
            if (a%i)==0:
                print(a,"is not prime number")
                break
        else:
            print(a,"is prime")


check_prime(35)
    

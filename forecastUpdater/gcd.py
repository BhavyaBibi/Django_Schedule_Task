def hcf(a, b):
    if(b == 0):
        return a
    else:
        return hcf(b, a % b)
  
a = 60
b = 48
  
# prints 12
print("The gcd of 60 and 48 is : ", end="")
print(hcf(60, 48))

//gcd uses for 
The GCD is used for a variety of applications in number theory, particularly in modular arithmetic and thus encryption algorithms such as RSA.
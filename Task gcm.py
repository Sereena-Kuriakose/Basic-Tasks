num1 = int(input("Enter first positive integer: "))
num2 = int(input("Enter second positive integer: "))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def lcm(a,b):
    return a*b/gcd()






print("The GCD of", num1, "and", num2, "is", gcd(num2,num1) "and lcm is" lcm(num1,num2))

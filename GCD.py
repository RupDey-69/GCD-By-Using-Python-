#Gcd Two Number

a=int(input("Enter the fast Number:"))
b=int(input("Enter the Second Number:"))

x,y=a,b

while b!=0:
    a,b=b,a%b

print(f"The Gcd {x} and {y} is:{a}")
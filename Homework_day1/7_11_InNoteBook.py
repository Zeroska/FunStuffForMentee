#!/usr/bin/python3


print("[*] your 7.11 in your god damn notebook")
print("Enter your x value")
x = int(input())
print("Enter your n times value")
n_times = int(input())
total = 0


#sqr of x^1/2 + x^1/4 so xn = x^(1/2)^2

for i in range(1,n_times + 1):
    if (n_times == 3):
        total += x**(1/2)
    total += x**(1/2)**i

print("The total of 7.11: " + str(total)) 

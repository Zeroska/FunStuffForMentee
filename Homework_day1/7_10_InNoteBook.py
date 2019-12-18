#!/usr/bin/python3.7

print("[*] Welcome to 7.10")


n_natural_number = int(input("Enter n number: "))
total = 0
for i in range(1,n_natural_number + 1):
    total += 1/i
print("Total of the S: " + str(total))

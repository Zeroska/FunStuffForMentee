#!/usr/bin/python3.7 

array_of_number = []
n_numbers = int(input("[*] How many number you want in your array: "))
target_number = int(input("Number you want to find k: "))
for i in range(n_numbers):
    number = int(input("Your " + str(i) + " number: "))
    array_of_number.append(number)

print(array_of_number)
count = 0


for i in range(len(array_of_number)):
    if target_number == array_of_number[i]:
        count = count + 1



if count == 0:
    print("Boss we can't find shit")
else:
    print("number of " + str(target_number) + "found is: "+ str(count)) 

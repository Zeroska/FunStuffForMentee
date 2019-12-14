
#Find the UCLN thuc su

#nguyen duong p 
#so nhap vao n

number = int(input("Enter you n number: "))     
total = 0
for i in range(number):
    if(i > 1 and i < number and number % i == 0):
        total += i
print(total)
        
        



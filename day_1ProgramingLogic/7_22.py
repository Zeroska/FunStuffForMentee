

#find the perfect number 

print("""

 |  __ \|  ____|  __ \|  ____|  ____/ ____|__   __| | \ | | |  | |  \/  |  _ \|  ____|  __ \ 
 | |__) | |__  | |__) | |__  | |__ | |       | |    |  \| | |  | | \  / | |_) | |__  | |__) |
 |  ___/|  __| |  _  /|  __| |  __|| |       | |    | . ` | |  | | |\/| |  _ <|  __| |  _  / 
 | |    | |____| | \ \| |    | |___| |____   | |    | |\  | |__| | |  | | |_) | |____| | \ \ 
 |_|    |______|_|  \_\_|    |______\_____|  |_|    |_| \_|\____/|_|  |_|____/|______|_|  \_\

""")
maximum_number = int(input("Max range: "))

#what is perfect number 

#find all UC
 
for numbers in range(1,maximum_number + 1): #number > 0
    perfect_number = 0
    temp = numbers 
    for j in range(1, numbers): #this loop until numbers - 1 then stop 
        if(temp % j == 0): #check whether the numbers is divisible
            perfect_number += j #if yes then add it to perfect_number 
    if perfect_number == temp: #
        print(perfect_number)


            

    



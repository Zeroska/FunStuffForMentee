



print(""" 
     ___           _______..___  ___.      _______.___________..______        ______   .__   __.   _______ 
    /   \         /       ||   \/   |     /       |           ||   _  \      /  __  \  |  \ |  |  /  _____|
   /  ^  \       |   (----`|  \  /  |    |   (----`---|  |----`|  |_)  |    |  |  |  | |   \|  | |  |  __  
  /  /_\  \       \   \    |  |\/|  |     \   \       |  |     |      /     |  |  |  | |  . `  | |  | |_ | 
 /  _____  \  .----)   |   |  |  |  | .----)   |      |  |     |  |\  \----.|  `--'  | |  |\   | |  |__| | 
/__/     \__\ |_______/    |__|  |__| |_______/       |__|     | _| `._____| \______/  |__| \__|  \______| 

""")

num = int(input("[*] Enter you Amstrong limit: "))
for number in range(num):
    temp =  number #For holding the number, not changing the i value
    total = 0 #Hold the ASM number
    power = len(str(number))  
    while temp > 0: #i can't be zero
        digit = temp % 10 
        total +=  digit ** power 
        temp //= 10 #Hold the value of the number left
    if total == number:
        print(number)

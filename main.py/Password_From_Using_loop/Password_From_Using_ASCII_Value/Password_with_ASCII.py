import random 
import time



print("\n\n                    **************  Strong Password Generator and Manager  **************\n\n")
time.sleep(2)

Servers = input("Which Server or Website do you need to generate password for ? (eg... Instagram , Facebook , Twitter) :  ")
User_name = input("\nPlease Enter Username Exactly on Server or Website ? : @")

if Servers==User_name :
    print("\n                 Error : Server and Username both are Exactly same       \n\n")
    exit()
    
Digits = int(input("\nHow long do you want the password to be ? : "))

Password = []

for i in range(0,Digits):
    ASCII_Value = chr(random.randint(33,127))
    Password.append(ASCII_Value)


print(f"\n\nServer     :  {Servers}\nUsername     :  {User_name}\nHere Your Password  :  {"".join(Password)}")
time.sleep(2.0)
print(f"\n\n   .............   Your password has been saved to the file : {Servers}_Password.txt   ............."+"\n\n\n")    


with open(f"{Servers}_Password.txt" ,'a') as file :
    file.write(f"Server  : {Servers}\nUsername : {User_name}")
    file.write("\nPassword : "+"".join(Password))



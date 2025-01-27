import random 
import time
from tabulate import tabulate

Letter = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
Number = "0123456789"
Symbol = r"/*-.},.;'[]\=-?><|+_)!@$%#^&*("


print("\n\n                    **************  Strong Password Generator and Manager  **************\n\n")
time.sleep(2)

Servers = input("Which Server or Website do you need to generate password for ? (eg... Instagram , Facebook , Twitter) :  ")
User_name = input("Please Enter Username Exactly on Server or Website ? : @")

if Servers==User_name :
    print("\n                 Error : Server and Username both are Exactly same       \n\n")
    exit()

print("\t\n")
tips = [ 
    ["1" , "Alphabets (Letters) Mix of uppercase and lowercase" , "6 to 8" ],
    ["2" , "Numbers" , "2 to 4"],
    ["3" , "Symbols", "2 to 3"]
]
header = ["No." , "Characters"  , "Ideal Proportion of Characters"]
tip_table = tabulate(tips, headers=header, tablefmt="grid")
time.sleep(3.5)
print("Tip For Creating Strong Passwords : ")
print(tip_table)

print("\n")

Letter_input = int(input("How many Letters Should  be there : "))
Number_input = int(input("How many Numbers  Should  be there : "))
Symbol_input = int(input("How many Symbols Should  be there : "))

if Letter_input < 0 or Number_input < 0 or Symbol_input < 0:
    print("\n                 Invalid Input      \n\n")
    exit()

Password = []

Password.extend(random.choices(Letter,k=Letter_input))
Password.extend(random.choices(Number,k=Number_input))
Password.extend(random.choices(Symbol,k=Symbol_input))
     
random.shuffle(Password)   

Passwords = "".join(Password)

print(f"\n\nServer     :   {Servers}\nUsername     :   @{User_name}\nHere Your Password     :   {Passwords}")
time.sleep(2.0)
print(f"\n\n   Your Password has been saved to the file : {Servers}_Password.txt"+"\n\n\n")    


with open(f"{Servers}_Password.txt" ,'a') as file :
    file.write(f"Server  : {Servers}\nUsername : @{User_name}")
    file.write(f"\nPassword : {Passwords}")



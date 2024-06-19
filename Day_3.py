# Data Types in Python

print("""
int : is use for inter value 
float : float is used for decimal values like 23.2 , 234.45 etc
str :  is used for string values like ABCDEFGHIJKLMNOPQRSTUVWXYZ
bool : is used for boolean values like true, false, yes, no, 0, 1
list :  is used for list values like [1, 2, 3]
tuple: is used for tuple values like [1, 2, 3,]
dict : is used for key value pairs like { "Ram":50,"Shyam":45} etc
""")

# Lets Take Example of each Data Type
i = int(input("Write your number which you want to print \n ")) # we use int for store only integers values
print(i)

s = str(input("Write your String which you want to print \n")) # we use str for store only strings values
print(s)

f = float(input("Write your decimal which you want to print")) # we use float for store only numbers values
print(f)

list =[1,2,3,4,5] # It is used to more than one values in a single variable and also different values
print(list[2])


tuple = (1, 34, "Shyam", False, 43.3)  
print(tuple[4])


dict = {"Shyam":50,"Jeet":45,"HariOm":56}
print(dict)
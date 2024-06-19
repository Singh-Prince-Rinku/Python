# Lets talk about f string which is introduce in python 3.6 

import datetime
from datetime import date
today = date.today()
name = input ("Enter your name \n")
print(f"Good Afternoon{name} sir")

print(f"How can i help you {today}")


#Also we can replaced string using replaced

letter = ''' Dear Name
             You are selected
                on Date'''
                
print(letter.replace("Name", f"{name}").replace("Date",f"{today}"))


# Note : Strings are also immutable so you cannot  change or replaced original string,
# you can copy strings then you perform those tasks
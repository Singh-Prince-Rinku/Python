''' Today we are going to discuss, operator in python
 As similar all the programming languages python has also same operator
 Python divides the operators in the following groups:

     Arithmetic operators
     Assignment operators
     Comparison operators
     Logical operators
     Identity operators
     Membership operators
     Bitwise operators


Let's discuss each operator '''

# 1. Arithmetic operators
print(5+4)
print(5-2)
print(5*4)
print(5/5)
print(5%2)
print(5**2)


# 2.Assignment operators
a = 5

c = 4
c +=4
print(c)

d = 5
d -= 5
print(d)

e = 5
e *=5
print(e)

f = 5
f/=5
print(f)

g = 5
g %= 5
print(g)

h = 5
h //=5
print(h)

i = 5
i **= 5
print(i)

j = 5
j &= 5
print(j)

K = 5
K |= 5
print(K)

l = 5
l ^= 5
print(l)


m = 5
m >>= 5
print(m)

n = 5
n <<= 5
print(n)


print(n:=5)

# 3.Comparison operators
a = 5
b = 5 
if(a==b):
    print("Equal operators")


c = 4
d = 5    
if(c!=d):
    print("Not Equal operators")
    
e = 7
f = 5
if (e > f):
    print("Greaterthan operators")
    
g = 5
h = 4
if(g < h):
    print("Lessthan operators")
    

i = 50
j = 51
if(i >= j):
    print("Greaterthan equal to operators")
    

k = 50
l = 45
if(k <= j):
    print("Lessthan equal to operators")
    

# 4.Logical operators_____________________________________________________________________________________________

'''Logical operators are used to combine conditional statements:

Operator                         	Description 	                          Example
and             	Returns True if both statements are true 	            x < 5 and  x < 10 	
or            	Returns True if one of the statements is true 	       x < 5 or x < 4 	
not     	Reverse the result, returns False if the result is true 	   not(x < 5 and x < 10) '''


# ________________________________________________________________________________________________________________________


# 5.Identity Operators___________________________________________________________________________________________________

'''Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, 
with the same memory location:

Operator                         	Description                                             	Example
is             	Returns True if both variables are the same object                       	x is y 	
is not 	       Returns True if both variables are not the same object                        	x is not y '''

#_______________________________________________________________________________________________________________________

# 6.Membership Operators_______________________________________________________________________________________________
'''Membership operators are used to test if a sequence is presented in an object:

 Operator 	                        Description 	                            Example
 in          	Returns True if a sequence with the specified value             x in y
                      is present in the object 	 

	
 not in 	          Returns True if a sequence with the specified             x not in y
                         value is not present in the object 	                                         '''
#_______________________________________________________________________________________________________________________

# 7.Bitwise operators_______________________________________________________________________________________________
''' Bitwise operators are used to compare (binary) numbers:

 Operator    	Name             	     Description 	                          Example

 &           	AND 	      Sets each bit to 1 if both bits are 1               	x & y 	


 | 	         OR 	    Sets each bit to 1 if one of two bits is 1           	x | y 	



 ^ 	        XOR 	     Sets each bit to 1 if only one of two bits is 1 	    x ^ y 	


 ~ 	        NOT 	              Inverts all the bits 	                         ~x 	


 << 	       Zero fill           Shift left by pushing
             left shift         zeros in from the right and 
                              let the leftmost bits fall off 	                    x << 2 	


 >> 	     Signed            Shift right by pushing copies of the 
             right                leftmost bit in from the left, 
            shift 	            and let the rightmost bits fall off 	            x >> 2        '''
# Today we are going to discuss about tuple and which type of operation can be perform on it.

#Tuple

tuple = (1,2 ,3,4,5,"Prince","Jeet","Hariom",False,True,3,2)  # We creat a tuple which store different type of values in a single tuple.
print(tuple) # For printing whole tuple elements.

tuple.count(2)
print(tuple) 

tuple.index("Prince")
print(tuple)

print(len(tuple)) # Len is used for to know the length of the tuple

tuple2 = (1,2,3,4,5,) 
print(tuple2 + tuple)  # concatenate two tuples together

print(tuple2 * 2)  # Repetition that how many time you want to repeat just use multiple with values

print(3 in tuple2)# To check the element is present or not in tuple , in this case present so it return true 

print(23 in tuple2)  # In this case the element is not present so it return false:

for item in tuple2:
    print(item)  # For printing all the elements in tuple using loop and also called iteration
    


a, b, c, d, e,  = tuple2  #Assigning the elements of a tuple to variables
print(a,b,c,d,e)  


'''
Note : Tuple is immutable so we cannot copy or change the value in a tuple 
        and also not sorting or reversing:
        but can be possible to convert tuples into list 
                                                                                   '''
                                                                                   
l = list(tuple2)  # Convert tuple into list
print(l)

l.sort()
print(l)

l.remove(4)
print(l)


l.reverse()
print(l)

#And many more:::::
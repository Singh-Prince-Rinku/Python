# Today we are going to discuss about  list in detail and what can be perform:

# List

List = [ 2, 34, "Prince", 54.345, False] #We creat a tuple and store different type of the data in a single list :

print(List) # Simple Print the all value of the list
print(List[2])  # through these we access perticular values of the list using index:
List[2]=456   # Using these we can change the value of the list :
# Note: The value of the list can be change because list are mutuable 
print(List)

List.append("Geeta")    #Append is used to add element in the last of the list
print(List)

List.insert(2,"Itachi")  #Insert is used to add element in the perticular index of the list
print(List)

List.remove(False) #Remove is used to remove element from the list by name 
print(List)

List.pop(2) #Pop is used to remove element from the list by index value
print(List)

List.clear()  #Clear is used to clear all the element in a list 
print(List)

List = [ 34,45,213,1,2,45,56]

List.sort()  # sort is used to sort the list
print(List) 

List.reverse() #reverse is used to reverse the list
print(List)

l = List.index(45) #Index is used to count how many repetated elements are in the list  
print(l)

l = List.count(2)  # Count is also used for count same element in a given list
print(l)


list = List.copy()  # Copy is used for copy list into new variable list
print(list)
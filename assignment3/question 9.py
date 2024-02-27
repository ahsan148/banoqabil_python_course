#Question 9
#Combine two strings using concatenation. Use string interpolation to include the length of the resulting string in a print statement. Explore different ways to manipulate strings in Python.
string1 = "Muhammad"
string2 = "Ahsan"
# + operator is used to combine strings
print(string1 + string2)
print("total length of combine string is :",len(string1+string2))
# join() method is used to combine the strings
print ("".join([string1, string2]))
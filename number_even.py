#A four-digit integer is given. Find the number of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value
var_int=5225
x1=var_int%10
x2=var_int%100//10
x3=var_int%1000//100
x4=var_int//1000

#Print the number of even digits in the variable "var_int".
print((x1+1)%2+(x2+1)%2+(x3+1)%2+(x4+1)%2)
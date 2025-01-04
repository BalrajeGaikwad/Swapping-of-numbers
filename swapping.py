# Two numbers are input through the keyboard into two locations C and D. Write a program to interchange the contents of C and D.


c=int(input(" Enter the number for c :-"))
d=int(input("Enter the number for d :- "))

c, d=d,c

print("The Value of C is :- ",c)
print("The Value of d is :- ",d)
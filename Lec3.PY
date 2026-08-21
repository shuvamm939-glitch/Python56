###Operators

##Arithmetic Operators

print(3+2)
print(9*3)
print(9/3)  ##[Single Division] It will give the float value(Ex.3.0)
print(9//3) ##[Floor Division] It will give the integer value(Ex.3)

###Modulus Operator --->"%"
print(9%2) ## It will give the remainder value(Ex.1),it's like in bengali Bhagsesh
print(9%3) ## 0(Ex.0)

###Power Operator --->"**"
print(9**3) ## It will give the power value(Ex.729),it's like in bengali Gunitok(Power)


#Q.Calculator
#take two int as input from user and print the sum,subtraction,multiplication,division,floor division,modulus,power of them.
N1 = int(input())
N2 = int(input())
print(N1+N2,N1-N2,N1*N2,N1/N2,N1//N2,N1%N2,N1**N2)

##2nd method
N1 = int(input())
N2 = int(input())
print(("Addition:",N1+N2),("Subtraction:",N1-N2),("Multiplication:",N1*N2),("Division:",N1/N2),("Floor Division:",N1//N2),("Modulus:",N1%N2),("Power:",N1**N2))

##Assignment Operators
x = 5 #Ex.1
x +=10 #x = x + 10(same as x+=10)
print(x)

x = 10 #Ex=2
x -= 5
print(x)

x = 10 #Ex.3
x *= 5
print(x)

x = 10 #Ex.4
x /= 5
print(x)

x = 10 #Ex.5
x//= 5
print(x)

x = 10 #Ex.6
x%= 5
print(x)

x = 20 #Ex.7
x**= 5
print(x)

##Comparison Operators
print(5 == 5)  # True
print(5 != 5)  # False ###"!=" means not equal to
print(5 > 3)   # True
print(5 < 3)   # False
print(5 >= 5)  # True
print(5 <= 5)  # True

##Logical Operators
  # and, or, not
print(True and True)   # True
     ##for example (4 > 3) and (5 > 2) = True both are true so the answer is True overall
print(True and False)  # False
     ##for example (4 > 3) and (5 < 2) = False one is false so the answer is False overall
print(False and False) # False
    ##for example (4 < 3) and (5 < 2) = False both are false so the answer is False overall
print(True or True)    # True
     ##for example (4 > 3) or (5 < 2) = True one is true so the answer is True overall
print(True or False)   # True
     ##for example (4 < 3) or (5 > 2) = True one is true so the answer is True overall
print(False or False)  # False
     ##for example (4 < 3) or (5 < 2) = False both are false so the answer is False overall
print(not True)        # False
     ##for example not (4 > 3) = False
print(not False)       # True
     ##for example not (4 < 3) = True
##not operator
 #not --> toggle

 #True --> False
 #False --> True

##Membership Operators
"a" in "Aditya"  # True
"b" in "Aditya"  # False
"c" not in "Aditya"  # True
"D" in "Aditya"  # False
"d" in "Aditya"  # True

##Quizes

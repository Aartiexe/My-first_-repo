                            #DAY -1 of practice
                           
                         
                 
                 # Program -1 ( Weather posibility)#
    
    
temp = int( input ( " Enter temperature of a day :"))
if temp >= 15  and   temp <= 20 :    # use logical operator
   print ( " chilled weather")
elif temp >= 25 and  temp <= 30 :
   print ( " sunny weather")
elif temp >=  35 and temp <= 50 :
	print ( " intens weather")
else :
	print ( " The weather is unpredicetable ")
	
	
	
	             # Program -2 ( Simple calculator logic )#
	             
	             
n1 = float ( input ( " Enter first number:"))
n2 = float ( input ( " Enter second number: "))
print ( " select operation: ")
print ( " 1 . Add")
print ( " 2 . Subtract")
print ( " 3 . Multiply")
print ( " 4 . Divide")

select = int(input ( " Enter select ( 1/ 2/ 3 / 4 ) : ")) # apply logic by operation 
if select == 1 :
	print ( " result : " , n1 + n2 )
elif select == 2 :
	print ( " result : " , n1 - n2 )
elif select == 3 :
	print ( " result : " , n1 * n2 )
elif select == 4 : 
     if n2 != 0:
     	print ( " result: " , n1/n2 )
     else:
     	print ( " cannot divide by zero")
else :
     print ( " invalid select ")
     
     
     
                   # Program - 3 ( Money tranfer system)#
                    
                    
account1 = 10000
account2 = 5000

amount = float(input("Enter amount to be transfer:"))

if amount <= account1 :
	account1 -= amount # money get withdraw
	account2 += amount # money get depoist
else :
	print ("Insufficient funds")
	
	
print("account1 balance :", account1)
print("account2 balance :", account2)



                      # Program - 4 (Fraud detection system)
                      
                      
                      
amount = float(input("Enter transaction amount: "))
attempts = int(input("Enter wrong PIN attempts: "))
location1 = input("Enter previous location: ")
location2 = input("Enter current location: ")

fraud_score = 0 #intialization

if amount > 10000:
    fraud_score += 1

if attempts >= 3:
    fraud_score += 1

if location1 != location2:
    fraud_score += 1

print("\nFraud Score:", fraud_score)  #( \n = it used to start next line)


if fraud_score == 0:
    print("Transaction Safe ")

elif fraud_score == 1 :
    print("Transaction Unsafe ")
    
elif fraud_score == 2 :
    print("Suspicious acitivity")
    
else :
    
    print("Fraud detected")
    
    
    
    
             # Program - 5 ( Calc on geomaterical shape)
             
             
             
             

while True :  # to create a infinite loop
  
    print("1. Perimeter of rectangle")
    print("2. Area of rectangle")
    print("3. Circumference of circle")
    print("4. Area of circle")
    print("0. Exit")

    num = int(input("Enter number: "))

    if num == 1:
        l = int(input("Length: "))
        b = int(input("Breadth: "))
        print("Perimeter =", 2*(l+b))

    elif num == 2:
        l = int(input("Length: "))
        b = int(input("Breadth: "))
        print("Area =", l*b)

    elif num == 3:
        r = int(input("Radius: "))
        print("Circumference =", 2*3.14*r)

    elif num == 4:
        r = int(input("Radius: "))
        print("Area =", 3.14*r*r)

    elif num == 0:
        break   # exit condition

    else:
        print(" Default value is assigning")
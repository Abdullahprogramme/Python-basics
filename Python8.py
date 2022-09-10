positiveNumber=0
sum=0
for count in range(6):
    number=int(input("Input number here: "))
    while number < 0:
        if number < 0:
            print("Input number again")
            number=int(input())   
    sum = sum + number           
    positiveNumber = positiveNumber + 1 
print("This is sum " + str(sum) + " and these are the positive numbers " + str(positiveNumber))
sum=0
for count in range(3):
    print("Input a number ")
    number=int(input())
    sum = sum + number
    if sum > 40:break
print(sum)  
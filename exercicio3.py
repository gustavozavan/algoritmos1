num1=int(input("Digite um número A: "))
num2=int(input("Digite outro número B: "))
num3=int(input("Digite outro número C: "))

if(num1>num2)and(num1>num3)and(num2>num3):
    print ("em crescente", num3, num2, num1)
elif(num1>num2)and(num1>num3)and(num3>num2):
    print ("em crescente", num2, num3, num1)
elif(num2>num1)and(num2>num3)and(num3>num1):
    print("em crescente", num1, num3, num2)
elif(num2>num1)and(num2>num3)and(num1>num3):
    print("em crescente", num3, num1, num2)
elif(num3>num1)and(num3>num2)and(num2>num1):
    print("em crescente", num1, num2, num3)
elif(num3>num1)and(num3>num2)and(num1>num2):
    print("em crescente", num2, num1, num3)

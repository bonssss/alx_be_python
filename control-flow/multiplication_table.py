number = int(input("Enter a number to see its multiplication table: "))
for i in range(1, 11):
    result = number * i
    print(number, "*",i, "=", result)
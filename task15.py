age = int(input("Enter please your age: "))

for i in range(0,age+1,2):
    if age % 2 == 0:
        print(i, end= " ")

for i in range(1,age+1,2):
    if age % 2 != 0:
        print(i, end= " ")
    
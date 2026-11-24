n = int(input("Enter number of entries: "))
student = {}
for _ in range(n):
    key = input("Enter key")
    value = input("Enter value")
    student[key] = value
print(student)
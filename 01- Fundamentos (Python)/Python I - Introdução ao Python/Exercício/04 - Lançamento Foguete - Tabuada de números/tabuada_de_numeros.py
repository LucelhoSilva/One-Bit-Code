number = int(input("Tabuada de: "))
begin = int(input("De: "))
end = int(input("Até: "))

for i in range(begin, end + 1):
    print(f"{number} x {i} = {number * i}")
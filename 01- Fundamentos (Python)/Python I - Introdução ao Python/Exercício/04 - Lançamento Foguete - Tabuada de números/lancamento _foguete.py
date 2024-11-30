x = 10

for i in range(x,-1, -1):
    print(i)
    if i == 0:
        print("Foguete lançado!")
        import winsound
        winsound.Beep(2500, 500)
        break
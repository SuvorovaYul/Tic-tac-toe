field = [[" "] * 3 for i in range (3) ]

def show():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | { ' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()

show()

def ask():
    while True:
        cords = input("          Ващ ход: ").split()

        if len(cords) != 2:
            print("Введите 2 координаты!")
            continue
        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите числа!")
            continue

        x, y = int(x), int(y)

        if 0 <= x <= 2 and 0 <= y <= 2 :
            if field[x][y] == " ":
                return x, y
            else:
                print("Клетка занята!")
        else:
            print("Координаты вне диапазона!")

ask()

num = 0
while True:
    num += 1

    if num % 2 == 1:
        print("Ходит крестик!")
    else:
        print("Ходит нолик!")

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"
    show()

    if num == 9:
        print("Ничья!")
        break
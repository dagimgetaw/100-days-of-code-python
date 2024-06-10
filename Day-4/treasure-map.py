row1 = ["📦","📦","📦"]
row2 = ["📦","📦","📦"]
row3 = ["📦","📦","📦"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do u want to put the treasure: ")

row = int(position[0])
col = int(position[1])
row -= 1
col -= 1

map[col][row] = "X"
print(f"{row1}\n{row2}\n{row3}")
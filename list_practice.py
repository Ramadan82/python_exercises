
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
position = input("enter position")
horizontal = int(position[0])
vertical = int(position[1])
# selected_row = map[vertical - 1]
# selected_row[horizontal - 1] = "X"
map[vertical - 1][horizontal - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")

"""
Input:

In the first line, two numbers n and m are given, which indicate the number of rows and columns in the table,
respectively. Then on the next line is a number k, which indicates the number of bombs in the table. Finally,
in each of the next k lines, in each line, an even pair of numbers indicating the location of the bombs is input to
the program. In each pair, first the row number and then the corresponding column are displayed; Suppose the table is
numbered from left to right with columns 1 to m and its rows from top to bottom numbered natural numbers 1 to n.

Output:

The program must print m × n in the output of a table. Print the symbol * for the bombs and the corresponding number
for the other cells in the table. Print a space between two consecutive elements in a row to separate them.
"""
row, column = input().split()
row = int(row)
column = int(column)
number_of_bombs = int(input())
a = []
f = []
u = []

for x in range(number_of_bombs):
    a.append(input().split())
a = sorted(a)

for t in range(row):
    for x in range(column):
        f.append('U')
    u.append(f)
    f = []
b = 0
for x in range(number_of_bombs):
    s = int(a[x][0])
    s1 = int(a[x][1])
    u[s - 1][s1 - 1] = "*"

for h in range(row):
    # print(u[h])
    for t in range(column):
        if (u[h][t]) != "*":
            # print("CHECKING 1")

            if h - 1 >= 0 and t - 1 >= 0 and u[h - 1][t - 1] == "*":
                b = b + 1
                # print('b1 is ', b)
                u[h][t] = b

            # print("CHECKING 2")

            if h - 1 >= 0 and u[h - 1][t] == "*":
                b = b + 1
                # print('b2 is ', b)
                u[h][t] = b

            # print("CHECKING 3")
            if h - 1 >= 0 and t + 1 < column and u[h - 1][t + 1] == "*":
                b = b + 1
                # print('b3 is ', b)
                u[h][t] = b
            # print("CHECKING 4")
            if t - 1 >= 0 and u[h][t - 1] == "*":
                b = b + 1
                # print('b4 is ', b)
                u[h][t] = b
            # print("CHECKING 5")

            if t + 1 < column and u[h][t + 1] == "*":
                b = b + 1
                # print('b5 is ', b)
                u[h][t] = b
            # print("CHECKING 6")

            if h + 1 < row and u[h + 1][t] == "*":
                b = b + 1
                # print('b6 is ', b)
                u[h][t] = b
            # print("CHECKING 7")
            if t - 1 >= 0 and h + 1 < row and u[h + 1][t - 1] == "*":
                b = b + 1
                # print('b7 is ', b)
                u[h][t] = b
            # print("CHECKING 8")

            if h + 1 < row and t + 1 < column and u[h + 1][t + 1] == "*":
                b = b + 1
                # print('b8 is ', b)
                u[h][t] = b

            u[h][t] = b
        b = 0
    b = 0
for h in range(row):
    for x in range(column):
        print(u[h][x], end=' ')
    print()

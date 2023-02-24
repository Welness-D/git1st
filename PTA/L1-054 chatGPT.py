char, n = input().split()
n = int(n)

grid = []
for i in range(n):
    line = input().strip()
    if len(line) != n:
        raise ValueError("Invalid input: number of characters in line does not match n.")
    grid.append(line)

# 判断是否对称
is_symmetric = True
for i in range(n):
    for j in range(n):
        if grid[i][j] != grid[n-1-i][n-1-j]:
            is_symmetric = False
            break
    if not is_symmetric:
        break

if is_symmetric:
    print("bu yong dao le")
else:
    for i in range(n):
        for j in range(n):
            if grid[n-1-i][n-1-j] == ' ':
                print(' ', end='')
            else:
                print(char, end='')
        print()

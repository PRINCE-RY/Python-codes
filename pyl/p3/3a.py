n=5
for i in range(1, n + 1):
    row = "* " * i
    print(row.strip().center(2 * n - 1))
for i in range(n - 1, 0, -1):
    row = "* " * i
    print(row.strip().center(2 * n - 1))

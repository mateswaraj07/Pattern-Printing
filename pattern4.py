# Expected output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# Print increasing numbers in each row

for i in range(1, 6):
    # Print numbers from 1 to the current row
    for j in range(1, i + 1):
        print(j, end=" ")

    print()
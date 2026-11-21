# Expected output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# Print the row number repeatedly

for i in range(1, 6):
    # Print the current row number i times
    for j in range(i):
        print(i, end=" ")

    print()
# Expected output:
# *
# * *
# *   *
# *     *
# * * * * *
# Print a hollow right-angled triangle

for i in range(1, 6):
    for j in range(1, i + 1):
        # Print stars on the boundary
        if j == 1 or j == i or i == 5:
            print("*", end=" ")
        else:
            # Print spaces inside the triangle
            print(" ", end=" ")

    print()
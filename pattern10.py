# Expected output:
# * * * * *
# *       *
# *       *
# *       *
# * * * * *
# Print a hollow square of 5 rows and 5 columns

for i in range(5):
    for j in range(5):
        # Print stars on the boundary
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end=" ")
        else:
            # Print spaces inside the square
            print(" ", end=" ")

    print()
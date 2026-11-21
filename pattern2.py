# Expected output:
# *
# * *
# * * *
# * * * *
# * * * * *

# Print a right-angled triangle

for i in range(1, 6):
    # Print stars equal to the current row number
    for j in range(i):
        print("*", end=" ")

    print()
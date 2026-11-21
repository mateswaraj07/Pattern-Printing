# Expected output:
# * * * * *
# * * * *
# * * *
# * *
# *

# Print an inverted right-angled triangle

for i in range(5, 0, -1):
    # Print stars from 5 to 1
    for j in range(i):
        print("*", end=" ")

    print()
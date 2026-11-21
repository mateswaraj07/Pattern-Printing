# Expected output:
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

# Print a right-aligned triangle

for i in range(1, 6):
    # Print spaces before the stars
    for j in range(5 - i):
        print("  ", end="")

    # Print stars according to the row number
    for j in range(i):
        print("*", end=" ")

    print()
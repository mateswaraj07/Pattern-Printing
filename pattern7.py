# Expected output:
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
# Print a star pyramid

for i in range(1, 6):
    # Print spaces to center the stars
    for j in range(5 - i):
        print("  ", end="")

    # Print odd number of stars
    for j in range(2 * i - 1):
        print("*", end=" ")

    print()
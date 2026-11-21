# Expected output:
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *
# Print an inverted star pyramid

for i in range(5, 0, -1):
    # Print spaces before the stars
    for j in range(5 - i):
        print("  ", end="")

    # Print decreasing odd number of stars
    for j in range(2 * i - 1):
        print("*", end=" ")

    print()
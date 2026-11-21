# Expected output:
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

# Print the upper half of the diamond

for i in range(1, 6):
    # Print spaces
    for j in range(5 - i):
        print("  ", end="")

    # Print increasing stars
    for j in range(2 * i - 1):
        print("*", end=" ")

    print()

# Print the lower half of the diamond

for i in range(4, 0, -1):
    # Print spaces
    for j in range(5 - i):
        print("  ", end="")

    # Print decreasing stars
    for j in range(2 * i - 1):
        print("*", end=" ")

    print()
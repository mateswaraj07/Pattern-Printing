# Expected output:
# *                 *
# * *             * *
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *
# * * * *     * * * *
# * * *         * * *
# * *             * *
# *                 *

# Print the upper half of the butterfly

for i in range(1, 6):
    # Print increasing stars on the left
    for j in range(i):
        print("*", end=" ")

    # Print spaces in the middle
    for j in range(2 * (5 - i)):
        print("  ", end="")

    # Print increasing stars on the right
    for j in range(i):
        print("*", end=" ")

    print()

# Print the lower half of the butterfly

for i in range(4, 0, -1):
    # Print decreasing stars on the left
    for j in range(i):
        print("*", end=" ")

    # Print spaces in the middle
    for j in range(2 * (5 - i)):
        print("  ", end="")

    # Print decreasing stars on the right
    for j in range(i):
        print("*", end=" ")

    print()
# Expected output:
# * * * *
# * * * *
# * * * *
# * * * *
# Print a solid square of 4 rows and 4 columns

for i in range(4):
    # Print 4 stars in each row
    for j in range(4):
        print("*", end=" ")

    # Move to the next line
    print()
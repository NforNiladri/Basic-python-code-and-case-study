#this is a program which will find factors of given number and find whether the factor is even or odd.


# Take input from the user
num = int(input("Enter a number: "))

# Loop through all the numbers from 1 to the given number
for i in range(1, num+1):

    # Check if i is a factor of the given number
    if num % i == 0:

        # Determine if the factor is even or odd
        if i % 2 == 0:
            print(i, "is an even factor of", num)
        else:
            print(i, "is an odd factor of", num)


# define height of the pyramid
rows = 5

# outer loop for each row
i = 1
while i <= rows:
    #print spaces
    space = rows - i
    while space > 0:
        print(" ", end="")
        space -= 1

    #print asterisks
    star = 1
    while star <= (2 * i - 1):
        print("*", end="")
        star += 1

    # move to the next line after each row
    print()
    i += 1
def count_as(file_name):

    # Create a function that takes a filename as string parameter,
    # counts the occurances of the letter "a", and returns it as a number.
    # If the file does not exist, the function should return 0 and not break.
    file_open= open(file_name, 'r')
    text = file_open.read()
    counter = 0
    try:
        for i in text:
            if i == 'a' or i == 'A':
                counter += 1
        return counter
    except FileNotFoundError:
        return 0

print(count_as("afile.txt")) # should print 28
print(count_as("not-a-file")) # should print 0

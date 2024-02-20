# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Creates the file if it doesn't exist as long as the mode is set to 'w'
# with open("new_file.txt", mode="w") as file:
#     file.write("\nNew text.")

# When the mode is 'a' then we are appending to the existing file
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")



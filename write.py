# Open a file in write mode ('w' creates the file if it doesn't exist,
# or overwrites it if it does)
file = open("myfile.txt", "w")

# Write some content to the file
file.write("Hello, this is my first line.\n")
file.write("This is the second line.\n")
file.write("Python file handling is easy!\n")

# Close the file to save changes
file.close()

print("File created and content written successfully!")








# Open the file in read mode ('r' is the default mode, but it's good to be explicit)
with open("myfile.txt", "r") as file:
    content = file.read()

# Display the content
print(content)
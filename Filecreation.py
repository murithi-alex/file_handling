# File Creation: Creating and writing to "my_file.txt"
try:
    with open("my_file.txt", "w") as file:
        file.write("Line 1: Hello, World!\n")
        file.write("Line 2: The number is 12345\n")
        file.write("Line 3: Python is fun!\n")
    print("File created and written successfully.")

except (FileNotFoundError, PermissionError) as e:
    print(f"Error occurred during file creation/writing: {e}")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("\nContents of 'my_file.txt':")
        print(content)

except (FileNotFoundError, PermissionError) as e:
    print(f"Error occurred while reading the file: {e}")

# File Appending: Appending additional lines to "my_file.txt"
try:
    with open("my_file.txt", "a") as file:
        file.write("Line 4: Appending more text.\n")
        file.write("Line 5: Another line with numbers: 67890\n")
        file.write("Line 6: The end of the file.\n")
    print("Additional lines appended successfully.")

except (FileNotFoundError, PermissionError) as e:
    print(f"Error occurred while appending to the file: {e}")

# Reading the file again to verify appended content
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("\nUpdated contents of 'my_file.txt':")
        print(content)

except (FileNotFoundError, PermissionError) as e:
    print(f"Error occurred while reading the updated file: {e}")

finally:
    print("\nFile operation completed.")

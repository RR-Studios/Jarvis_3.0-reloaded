import os


def create_file_with_extension(extension):
    try:
        # Get the file name from the user
        file_name = input("Enter the file name (without extension): ")

        # Construct the full file name with the given extension
        full_file_name = f"{file_name}.{extension}"

        # Create an empty file with the specified extension
        with open(full_file_name, 'w'):
            pass

        print(f"File '{full_file_name}' has been created successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    print("Choose a file extension to create a new file:")
    print("1. .xlsx")
    print("2. .docx")
    print("3. .doc")
    print("4. .pdf")
    print("5. .accdb")
    print("6. .py")
    print("7. .HTML")
    print("8. .css")
    print("9. .json")
    print("10. .js")

    choice = input("Enter your choice (1-10): ")

    extensions = {
        '1': 'xlsx',
        '2': 'docx',
        '3': 'doc',
        '4': 'pdf',
        '5': 'accdb',
        '6': 'py',
        '7': 'HTML',
        '8': 'css',
        '9': 'json',
        '10': 'js'
    }

    if choice in extensions:
        create_file_with_extension(extensions[choice])
    else:
        print("Invalid choice. Please select a valid option.")

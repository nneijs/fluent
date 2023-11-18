def create_file(file_name, content):
    try:
        # Open the file in write mode ('w')
        with open(file_name, 'w') as file:
            # Write content to the file
            file.write(content)
        print(f"File '{file_name}' created successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Ask the user for confirmation
confirmation = input("Please enter your package name : ").lower()

if confirmation == 'sks add fluent':
    # Hardcoded file name and content
    file_name = "index.js"
    file_content = "// Hello, this is the content of the file."

    # Call the create_file function with the hardcoded values
    create_file(file_name, file_content)
else:
    print("No file was created.")

try:
    # Ask user for the input file name
    input_file = input("Enter the name of the file to read: ")
    
    # Read the content of the file
    with open(input_file, 'r') as file:
        content = file.readlines()
    
    # Add line numbers to each line
    modified_content = [f"{i + 1}: {line}" for i, line in enumerate(content)]
    
    # Ask user for the output file name
    output_file = input("Enter the name of the new file to write: ")
    
    # Write the modified content to the new file
    with open(output_file, 'w') as file:
        file.writelines(modified_content)
    
    print("File has been modified and saved successfully.")
    
except FileNotFoundError:
    print("Error: File not found. Please check the file name and try again.")
except Exception as e:
    print(f"An error occurred: {e}")

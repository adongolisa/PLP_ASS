def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as file:
            content = file.read()

        # Modify the content (for example, convert to uppercase)
        modified_content = content.upper()

        # Open the output file for writing
        with open(output_filename, 'w') as file:
            file.write(modified_content)

        print(f"The modified content has been written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read the file '{input_filename}'.")

# Ask the user for the filenames
input_filename = input("Enter the input filename: ")
output_filename = input("Enter the output filename: ")

# Call the function with the provided filenames
read_and_modify_file(input_filename, output_filename)

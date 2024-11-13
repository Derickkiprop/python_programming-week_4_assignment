import os

def read_and_modify_file():
    try:
        # Ask the user for the filename
        filename = input("Enter the filename to read: ")
        
        # Check if the file exists
        if not os.path.isfile(filename):
            raise FileNotFoundError(f"The file '{filename}' does not exist.")
        
        # Attempt to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
        
        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()
        
        # Define the name of the new file
        new_filename = 'modified_' + filename
        
        # Write the modified content to the new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
        
        print(f"Modified content written to '{new_filename}' successfully.")
    
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    
    except PermissionError:
        print("Error: You do not have permission to read or write to this file.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
read_and_modify_file()

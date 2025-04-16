def get_valid_input_file():
    while True:
        filename = input("Enter the name of the input file to read: ").strip()
        try:
            with open(filename, 'r') as test_file:
                test_file.read(1)  
            return filename
        except FileNotFoundError:
            print(f"Error: The file '{filename}' does not exist. Please try again.")
        except PermissionError:
            print(f"Error: No permission to read '{filename}'. Please try again.")
        except Exception as e:
            print(f"Error accessing file: {str(e)}. Please try again.")

def get_valid_output_file():
    while True:
        filename = input("Enter the name of the output file to write: ").strip()
        try:
            with open(filename, 'w') as test_file:
                test_file.write("")
            return filename
        except PermissionError:
            print(f"Error: No permission to write to '{filename}'. Please try again.")
        except Exception as e:
            print(f"Error with output file: {str(e)}. Please try again.")

def modify_and_write_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
        
        modified_content = content.upper()
        
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        print(f"Successfully read from '{input_filename}' and wrote modified content to '{output_filename}'")
        
    except Exception as e:
        print(f"An error occurred during file processing: {str(e)}")

if __name__ == "__main__":
    print("Welcome to the file modifier program!")
    
    input_file = get_valid_input_file()
    output_file = get_valid_output_file()
    
    modify_and_write_file(input_file, output_file)
def modify_and_write_file(input_filename, output_filename):    # Fixed parameter names
    try:
        with open(input_filename, 'r') as input_file:         # Use parameter name, not string literal
            content = input_file.read()
        
        modified_content = content.upper()
        
        with open(output_filename, 'w') as output_file:       # Use parameter name, not string literal
            output_file.write(modified_content)
        print(f"Successfully read from {input_filename} and wrote modified content to {output_filename}")
        
    except FileNotFoundError:
        print(f"Error: The file {input_filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    input_file = "food.txt"
    output_file = "justaprogrammer.txt"
    modify_and_write_file(input_file, output_file)
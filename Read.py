def read_and_write_file():
    filename = input("Enter the name of the file to read: ")
    try:
        with open(filename, 'r', encoding='utf-8') as infile:
            data = infile.read()
        # Modify data (e.g., make it uppercase)
        modified_data = data.upper()
        output_filename = f"modified_{filename}"
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.write(modified_data)
        print(f"Modified data written to {output_filename}")
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: Cannot read the file.")

if __name__ == "__main__":
    read_and_write_file()
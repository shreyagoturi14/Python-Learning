import os

def list_directory_contents(path='.'):
    """Prints the contents of the specified directory. Defaults to current directory."""
    try:
        contents = os.listdir(path)
        print(f"Contents of directory '{path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"Error: The directory '{path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    directory_path = input("Enter the directory path (or press Enter for current directory): ").strip()
    if not directory_path:
        directory_path = '.'
    list_directory_contents()

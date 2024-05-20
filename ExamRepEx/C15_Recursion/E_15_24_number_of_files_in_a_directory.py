import os

# iterative
# def count_files_in_directory(directory):
#     try:
#         files_count = 0
#         for item in os.listdir(directory):
#             item_path = os.path.join(directory, item)
#             if os.path.isfile(item_path):
#                 files_count += 1
#         return files_count
#     except FileNotFoundError:
#         return "Directory not found."
#     except PermissionError:
#         return "Permission denied to access the directory."

# recursively
import os

def count_files_in_directory(directory):
    try:
        # Initialize count
        files_count = 0
        
        # Recursively explore the directory
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):
                files_count += 1
            elif os.path.isdir(item_path):
                files_count += count_files_in_directory(item_path)  # Recursive call for subdirectories
        
        return files_count
    except FileNotFoundError:
        return "Directory not found."
    except PermissionError:
        return "Permission denied to access the directory."


def main():
    directory = input("Enter a directory: ")
    files_count = count_files_in_directory(directory)
    print("Number of files in the directory:", files_count)

if __name__ == "__main__":
    main()
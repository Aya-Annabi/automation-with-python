import os
import shutil

def organize_folder(folder_path):
    # Check if the provided path is valid
    if not os.path.isdir(folder_path):
        print(f"The path '{folder_path}' is not a valid directory.")
        return

    # Create a dictionary to hold files by their extension
    files_by_extension = {}

    # Iterate over all the files in the specified folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower()  # Normalize the extension to lowercase

        # Skip files without an extension
        if not ext:
            continue

        # Add the file to the corresponding extension list
        if ext not in files_by_extension:
            files_by_extension[ext] = []
        files_by_extension[ext].append(file_path)

    # Create subfolders for each extension and move the files
    for ext, files in files_by_extension.items():
        ext_folder = os.path.join(folder_path, ext[1:] + '_files')  # Remove the leading dot and add '_files'
        os.makedirs(ext_folder, exist_ok=True)

        for file_path in files:
            shutil.move(file_path, ext_folder)

    print("Folder organization complete.")

if __name__ == "__main__":
    # Specify the path to the folder you want to organize
    folder_path = input("Enter the path to the folder you want to organize: ").strip()

    organize_folder(folder_path)

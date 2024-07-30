import os
import shutil

def organize_files(directory):
    # Ensure the directory exists
    if not os.path.isdir(directory):
        print(f"The directory {directory} does not exist.")
        return
    
    # Change to the specified directory
    os.chdir(directory)
    
    # List all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(f)]
    
    for file in files:
        # Get the file extension and create a directory for it if it doesn't exist
        file_extension = file.split('.')[-1]
        if len(file_extension) > 1:  # Avoid hidden files and directories without extensions
            target_dir = os.path.join(directory, file_extension.upper() + '_files')
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            
            # Move the file to the appropriate directory
            shutil.move(file, os.path.join(target_dir, file))
            print(f"Moved {file} to {target_dir}")

def main():
    directory = input("Enter the path of the directory to organize: ")
    organize_files(directory)
    print("File organization complete.")

if __name__ == "__main__":
    main()
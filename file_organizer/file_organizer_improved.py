import os
import shutil
from datetime import datetime

# Define categories and their extensions
FILE_CATEGORIES = {
    "Music": [".mp3", ".wav", ".flac"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Pictures": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx", ".csv"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Programs": [".exe", ".msi", ".sh", ".bat"],
    "Shortcuts": [".lnk"],  # New category for shortcuts
    "Others": []  # Catch-all for any unrecognized extensions
}

def organize_folder(folder_path):
    """
    Organize files in the given folder_path by their extensions.
    """
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist. Please check the path.")
        return

    # Log file setup
    log_file = os.path.join(folder_path, "organization_log.txt")
    with open(log_file, "w") as log:
        log.write(f"File Organization Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        log.write("=" * 50 + "\n")

    # Create categorized folders if they don't already exist
    for category in FILE_CATEGORIES.keys():
        category_folder = os.path.join(folder_path, category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

    # Process each file in the folder
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        # Skip directories and the log file
        if os.path.isdir(item_path) or item == "organization_log.txt":
            continue

        # Get file extension
        _, file_extension = os.path.splitext(item)
        
        # Move the file to the appropriate folder
        destination_folder = None
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension.lower() in extensions:
                destination_folder = os.path.join(folder_path, category)
                break
        # If no matching category, move to "Others"
        if not destination_folder:
            destination_folder = os.path.join(folder_path, "Others")

        shutil.move(item_path, destination_folder)
        with open(log_file, "a") as log:
            log.write(f"Moved: {item} -> {destination_folder}\n")
        print(f"Moved: {item} -> {destination_folder}")

    # Remove empty folders
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path) and not os.listdir(item_path):
            os.rmdir(item_path)
            with open(log_file, "a") as log:
                log.write(f"Removed empty folder: {item_path}\n")
            print(f"Removed empty folder: {item_path}")

    print("Organization complete!")
    print(f"Log saved to: {log_file}")

# Example usage
if __name__ == "__main__":
    folder_to_organize = input("Enter the path of the folder to organize: ").strip()
    organize_folder(folder_to_organize)

import shutil
import stat

def remove_folder(folder_path):
    """
    Safely remove a folder, handling permissions issues.
    """
    try:
        os.rmdir(folder_path)  # Try removing as an empty folder
        print(f"Removed empty folder: {folder_path}")
    except PermissionError:
        print(f"PermissionError: Could not remove {folder_path}. Trying elevated permissions...")
        # Change folder attributes and retry
        os.chmod(folder_path, stat.S_IWRITE)
        shutil.rmtree(folder_path, ignore_errors=True)
        print(f"Removed non-empty folder with elevated permissions: {folder_path}")
    except Exception as e:
        print(f"Error removing folder {folder_path}: {e}")

# Replace os.rmdir(item_path) in the script with this function
if os.path.isdir(item_path) and not os.listdir(item_path):
    remove_folder(item_path)

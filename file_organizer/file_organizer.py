import os
import shutil

# Define categories and their extensions
FILE_CATEGORIES = {
    "Music": [".mp3", ".wav", ".flac"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Pictures": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Programs": [".exe", ".msi", ".sh", ".bat"],
    "Others": []  # Catch-all for any unrecognized extensions
}

def organize_folder(folder_path):
    """
    Organize files in the given folder_path by their extensions.
    """
    if not os.path.exists(folder_path):
        print(f"The folder {folder_path} does not exist.")
        return

    # Create categorized folders if they don't already exist
    for category in FILE_CATEGORIES.keys():
        category_folder = os.path.join(folder_path, category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

    # Process each file in the folder
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        # Skip directories
        if os.path.isdir(item_path):
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
        print(f"Moved: {item} -> {destination_folder}")

    print("Organization complete!")

# Example usage
if __name__ == "__main__":
    folder_to_organize = input("Enter the path of the folder to organize: ").strip()
    organize_folder(folder_to_organize)

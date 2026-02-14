# File Organizer Script
import os
import shutil

# File type categories
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar"],
    "Scripts": [".py", ".js", ".html", ".css"]
}

def find_folder(folder_name):

    """
    searches the user's home directory for a folder with the given name.
    Returns the full path if found otherwise none.
    """
    home = os.path.expanduser("~")
    print(f"\nSearching for folder '{folder_name}' in {home} ...\n")

    for root, dirs, files in os.walk(home):
        if folder_name in dirs:
            found_path = os.path.join(root, folder_name)
            print(f"Found folder: {found_path}\n")
            return found_path

    print("Folder not found in your home directory.\n")
    return None

def organize_folder(folder_path):
    # Organizes files inside the given folder into subfolders by file type.
    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
        return

    print(f"Organizing folder: {folder_path}\n")
    files_moved = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if not os.path.isfile(file_path) or filename.startswith('.'):
            continue

        _, ext = os.path.splitext(filename)
        moved = False

        for category, extensions in CATEGORIES.items():
            if ext.lower() in extensions:
                category_folder = os.path.join(folder_path, category)
                os.makedirs(category_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(category_folder, filename))
                print(f"Moved: {filename}  →  {category}/")
                moved = True
                files_moved += 1
                break

        if not moved:
            other_folder = os.path.join(folder_path, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, filename))
            print(f"Moved: {filename}  →  Others/")
            files_moved += 1

    print(f"\nDone. {files_moved} files organized.\n")

def main():
    print(" File Organizer \n")

    folder_name = input("Enter the folder name to organize: ").strip()
    folder_path = find_folder(folder_name)

    if not folder_path:
        custom = input("Folder not found automatically.\nEnter the full path manually: ").strip()
        if not os.path.exists(custom):
            print("Still not found. Exiting.")
            return
        folder_path = custom

    organize_folder(folder_path)

if __name__ == "__main__":
    main()

import os
import shutil
import argparse

# Folder categories and file extensions
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar"],
    "Scripts": [".py", ".js", ".html", ".css"]
}

def organize_folder(folder_path, dry_run=False):
    if not os.path.exists(folder_path):
        print(f"❌ Folder not found: {folder_path}")
        return

    print(f"\n📁 Organizing folder: {os.path.abspath(folder_path)}\n")
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

                if not dry_run:
                    shutil.move(file_path, os.path.join(category_folder, filename))

                print(f"📂 {filename} → {category}/")
                moved = True
                files_moved += 1
                break

        if not moved:
            other_folder = os.path.join(folder_path, "Others")
            os.makedirs(other_folder, exist_ok=True)

            if not dry_run:
                shutil.move(file_path, os.path.join(other_folder, filename))

            print(f"📁 {filename} → Others/")
            files_moved += 1

    print(f"\n✅ Done! {files_moved} files {'would be moved' if dry_run else 'moved'}.\n")

def main():
    parser = argparse.ArgumentParser(description="📂 Organize files in a folder by type.")
    parser.add_argument(
        "--path", "-p",
        help="Folder path or name (default: current directory)."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview what would be moved without actually moving files."
    )

    args = parser.parse_args()

    # 🧭 If no path is given → use current folder
    folder_path = args.path or os.getcwd()

    # If user gives a short folder name, make it absolute
    if not os.path.isabs(folder_path):
        folder_path = os.path.join(os.getcwd(), folder_path)

    organize_folder(folder_path, dry_run=args.dry_run)

if __name__ == "__main__":
    main()

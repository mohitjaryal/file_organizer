import os
import shutil

# Folder categories and file extensions
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar"],
    "Scripts": [".py", ".js", ".html", ".css"]
}

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print("❌ Folder not found!")
        return
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            moved = False
            for category, extensions in categories.items():
                if ext.lower() in extensions:
                    category_folder = os.path.join(folder_path, category)
                    os.makedirs(category_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_folder, filename))
                    moved = True
                    print(f"📂 Moved: {filename} → {category}/")
                    break
            
            if not moved:
                other_folder = os.path.join(folder_path, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, filename))
                print(f"📁 Moved: {filename} → Others/")

def main():
    folder = input("Enter folder path to organize: ").strip()
    organize_folder(folder)
    print("\n✅ Folder organized successfully!")

if __name__ == "__main__":
    main()

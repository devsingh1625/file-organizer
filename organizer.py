from pathlib import Path
import shutil

default_folder = Path.home() / "Downloads"

while True:
    raw = input("Which folder do you want to organize? [default: {}]: ".format(
        default_folder)).strip()
    if raw:
        target = Path(raw).expanduser()
    else:
        target = default_folder

    if target.exists() and target.is_dir():
        print("✅ Using folder: {}".format(target))
        break
    else:
        print("❌ That path is not a valid folder. Try Again.\n ")

# --- Categories of file extensions ---
categories = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".heic"],
    "pdfs": [".pdf"],
    "documents": [".txt", ".doc", ".docx", ".md"],
    "spreadsheets": [".csv", ".xlsx", ".xls"],
    "presentations": [".ppt", ".pptx"],
    "zips": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "audio": [".mp3", ".wav", ".aac", ".flac"],
    "videos": [".mp4", ".mov", ".avi", ".mkv"],
    "code": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp"],
}

# --- Step 2: Organize files ---
for item in target.iterdir():
    if item.is_file():
        ext = item.suffix.lower()

        # Find matching category
        moved = False
        for folder_name, extensions in categories.items():
            if ext in extensions:
                dest_folder = target / folder_name
                # make the folder if it doesn't exist
                dest_folder.mkdir(exist_ok=True)
                shutil.move(str(item), dest_folder / item.name)
                print(f"Moved {item.name} → {folder_name}/")
                moved = True
                break

        # If no matching category, move to "others"
        if not moved:
            others_folder = target / "others"
            others_folder.mkdir(exist_ok=True)
            shutil.move(str(item), others_folder / item.name)
            print(f"Moved {item.name} → others/")

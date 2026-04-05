import os
import shutil

FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".exr"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Documents": [".pdf", ".txt", ".docx"]
}

def organise_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)

            moved = False
            for folder, extensions in FILE_TYPES.items():
                if ext.lower() in extensions:
                    target_folder = os.path.join(folder_path, folder)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    print(f"Moved {filename} to {folder}")
                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(folder_path, "Other")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, filename))
                print(f"Moved {filename} to Other")

if __name__ == "__main__":
    folder = input("Enter folder path to organise: ")
    organise_files(folder)

from pathlib import Path
import shutil
import os
import sys


file_extension = {
    "images": [".jpg", ".jpeg", ".png", ".webp", ".gif"],
    "videos": [".mp4", ".avi", ".mov", ".mkv"],
    "code": [".py", ".c", ".cpp", ".java", ".js", ".html", ".css"],
    "documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "audio": [".wav"],
    "other": []
}


def get_non_empty_string(prompt: str) -> str:
    """Prompt until user enters a non-empty string."""
    while True:
        try:
            value = input(prompt).strip()
            if value:
                return value
            print("\nInput cannot be empty. Try again.")
        except (KeyboardInterrupt, EOFError):
            exit_program()


def exit_program():
    """Function to gracefully exit the program."""
    print("\nGoodbye!")
    sys.exit()


def show_menu():
    """Display the program menu."""
    print("\n=== File Organizer ===")
    print("1. Organize files in a directory")
    print("q. Quit")


def contains_file_scandir(directory_path):
    """Checks if a given directory contains any files using os.scandir()."""
    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' is not a valid directory.")
        return False

    with os.scandir(directory_path) as entries:
        return any(entry.is_file() for entry in entries)


def move_files(directory_path):
    """Move all the files to their corresponding directory."""
    for entry in Path(directory_path).iterdir():
        if entry.is_file():
            extension = entry.suffix.lower()
            moved = False

            for category, extensions in file_extension.items():
                if extension in extensions:
                    dest_folder = Path(directory_path) / category.upper()
                    dest_path = dest_folder / entry.name
                    shutil.move(str(entry), str(dest_path))
                    moved = True
                    break

            if not moved:
                dest_folder = Path(directory_path) / "OTHER"
                dest_path = dest_folder / entry.name
                shutil.move(str(entry), str(dest_path))

        elif entry.is_dir():
            print(f"Skipping directory: {entry}")


def create_directories(directory_path):
    """Create the categorized directories inside the given directory."""
    try:
        for directory in file_extension.keys():
            base = Path(directory_path)
            my_directory = base / directory.upper()
            my_directory.mkdir(exist_ok=True)
        print("Directories created!")
    except FileExistsError as e:
        print(f"The directory {e} already exists.")


def main():
    """Main function of the program."""
    while True:
        show_menu()
        directory_path = get_non_empty_string("\nEnter the directory (or 'q' to exit): ")

        if directory_path.lower() == "q":
            exit_program()

        if contains_file_scandir(directory_path):
            create_directories(directory_path)
            move_files(directory_path)
            print("Files organized successfully!")
        else:
            print(f"The folder '{directory_path}' does not contain any files and cannot be organized.")

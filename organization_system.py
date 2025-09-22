from pathlib import Path
import shutil
import os
import sys


# File extension categories
FILE_EXTENSIONS = {
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


def contains_file_scandir(directory_path: str) -> bool:
    """Checks if a given directory contains any files using os.scandir()."""
    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' is not a valid directory.")
        return False

    with os.scandir(directory_path) as entries:
        return any(entry.is_file() for entry in entries)


def create_directories(directory_path: str):
    """Create categorized directories inside the given directory."""
    base = Path(directory_path)
    for directory in FILE_EXTENSIONS.keys():
        (base / directory.upper()).mkdir(exist_ok=True)
    # Ensure OTHER folder exists
    (base / "OTHER").mkdir(exist_ok=True)


def move_files(directory_path: str):
    """Move all files to their corresponding categorized directories."""
    base = Path(directory_path)
    create_directories(base)  # Ensure folders exist before moving

    for entry in base.iterdir():
        if entry.is_file():
            extension = entry.suffix.lower()
            dest_folder = None

            # Find matching category
            for category, extensions in FILE_EXTENSIONS.items():
                if extension in extensions:
                    dest_folder = base / category.upper()
                    break

            # Default to OTHER if no category matches
            if dest_folder is None:
                dest_folder = base / "OTHER"

            dest_path = dest_folder / entry.name

            # Avoid overwriting files with the same name
            counter = 1
            while dest_path.exists():
                dest_path = dest_folder / f"{entry.stem}_{counter}{entry.suffix}"
                counter += 1

            shutil.move(str(entry), str(dest_path))

        elif entry.is_dir():
            if entry.name.upper() not in [cat.upper() for cat in FILE_EXTENSIONS.keys()] + ["OTHER"]:
                print(f"Skipping directory: {entry}")


def main():
    """Main function of the program."""
    while True:
        show_menu()
        choice = get_non_empty_string("\nEnter your choice: ")

        if choice.lower() == "q":
            exit_program()

        elif choice == "1":
            directory_path = get_non_empty_string("\nEnter the directory path: ")

            if contains_file_scandir(directory_path):
                move_files(directory_path)
                print("Files organized successfully!")
            else:
                print(f"The folder '{directory_path}' does not contain any files and cannot be organized.")

        else:
            print("Invalid choice. Please try again.")

# File Organizer CLI

A lightweight Python command-line tool to automatically organize files in a directory by type.  
The program creates categorized folders (e.g., Images, Videos, Documents, Code) and moves your files into the right place.

---

## ✨ Features
- Sorts files into categories:
  - **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`
  - **Videos**: `.mp4`, `.avi`, `.mov`, `.mkv`
  - **Documents**: `.pdf`, `.docx`, `.txt`, `.xlsx`
  - **Code**: `.py`, `.c`, `.cpp`, `.java`, `.js`, `.html`, `.css`
  - **Audio**: `.wav`
  - **Other**: anything else
- Automatically creates folders if they don’t exist.
- Skips invalid paths and handles empty directories safely.
- Works on Windows, Linux, and macOS.

---

## 📂 Project Structure
```html
file-organizer-cli/
│
├── main.py                # Entry point
├── organization_system.py # Core logic
├── README.md
└── LICENSE
```

## ⚡ Installation

Clone the repository:
```
git clone https://github.com/BelacEr/file-organizer-cli.git
cd file-organizer-cli
```

## 🖥️ Usage

Run the program with:
```bash
python main.py
```

Enter the path of the directory you want to organize.
For example:

Enter the directory (or 'q' to exit): /home/user/Downloads

After running, the directory will look like this:

```html
Downloads/
├── AUDIO/
├── CODE/
├── DOCUMENTS/
├── IMAGES/
├── OTHER/
└── VIDEOS/
```
## 📜 License

[MIT](https://github.com/BelacEr/file-organizer-cli/blob/main/LICENSE) Copyright (c) [BelacEr](https://github.com/BelacEr)
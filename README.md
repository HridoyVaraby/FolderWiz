# FolderWiz

FolderWiz is a Windows application that automatically organizes files in a selected folder based on their file types. It integrates with the Windows Explorer context menu, allowing you to quickly rearrange files by right-clicking on a folder.

## Features

-   **Automatic File Sorting:** Sorts files into designated folders (e.g., images, videos, documents, archives, executables, illustrator, photoshop, music) based on their extensions.
-   **Context Menu Integration:** Adds a "Rearrange Files" option to the right-click context menu in Windows Explorer.
-   **User-Friendly Interface:** Provides a simple GUI using Tkinter for selecting the folder to organize.

## File Types Supported

-   **Images:** .jpg, .jpeg, .png, .gif, .bmp, .webp
-   **Videos:** .mp4, .avi, .mov, .mkv
-   **Documents:** .doc, .docx, .pdf, .txt, .rtf, .csv
-   **Archives:** .zip, .rar, .7z, .tar, .gz
-   **Executables:** .exe, .msi
-   **Illustrator:** .ai
-   **Photoshop:** .psd, .psb
-   **Music:** .mp3, .wav, .flac, .aac

## Installation

1.  **Download the script:** Download the `folderwiz.py` file from the GitHub repository.
2.  **Install pywin32:** Since `pip` is not available in this environment, you will need to manually install `pywin32`.
    -   Go to the official pywin32 releases page on GitHub: [https://github.com/mhammond/pywin32/releases](https://github.com/mhammond/pywin32/releases)
    -   Download the appropriate installer for your Python version and system architecture (e.g., `pywin32-306.win-amd64-py3.11.exe` for Python 3.11 64-bit).
    -   Run the installer and follow the on-screen instructions.
3.  **Install pyinstaller (optional):** If you want to create a single executable file, you'll need `pyinstaller`.
    -   Download and install `pyinstaller` manually.
    -   After installing `pyinstaller`, run the following command in your terminal: `pyinstaller --onefile --noconsole folderwiz.py`. This will create a single executable file in the `dist` folder.

## How to Run

1.  **Run the script:** Open a command prompt or terminal, navigate to the directory where you saved `folderwiz.py`, and run the script using:
    ```
    python folderwiz.py
    ```
    **Important:** You need to run the script as an administrator for the context menu integration to work correctly. Right-click on the `folderwiz.py` file and select "Run as administrator".
2.  **Using the GUI:**
    -   The FolderWiz GUI will open.
    -   Click the "Browse" button to select the folder you want to organize.
    -   Click the "Rearrange Files" button to start organizing the files.
3.  **Using the Context Menu:**
    -   After running the script as an administrator, you can right-click on any folder in Windows Explorer.
    -   Select the "Rearrange Files" option to organize the files in that folder.

## Troubleshooting

-   **"Failed to add context menu: \[WinError 5] Access is denied"**: This error indicates that the script was not run with administrator privileges. Make sure to run the script as an administrator.
-   **ModuleNotFoundError: No module named 'win32con'**: This error indicates that the `pywin32` library is not installed. Follow the installation instructions above.

## Contributing

Feel free to contribute to this project by submitting pull requests or reporting issues.

## License

This project is licensed under the MIT License.
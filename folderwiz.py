import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
import win32con
import win32gui
import winreg
import sys

class FolderWiz:
    def __init__(self, root):
        self.root = root
        self.root.title("FolderWiz")

        self.folder_path = tk.StringVar()

        tk.Label(root, text="Select Folder:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        tk.Entry(root, textvariable=self.folder_path, width=50).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(root, text="Browse", command=self.browse_folder).grid(row=0, column=2, padx=5, pady=5)

        tk.Button(root, text="Rearrange Files", command=self.rearrange_files).grid(row=1, column=0, columnspan=3, pady=20)

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.folder_path.set(folder_selected)

    def rearrange_files(self):
        folder = self.folder_path.get()
        if not folder:
            messagebox.showerror("Error", "Please select a folder.")
            return

        try:
            self.organize_files(folder)
            messagebox.showinfo("Success", "Files rearranged successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def organize_files(self, folder):
        file_types = {
            "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
            "videos": [".mp4", ".avi", ".mov", ".mkv"],
            "documents": [".doc", ".docx", ".pdf", ".txt", ".rtf", ".csv", ".gdoc", ".gsheet"],
            "archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
            "executables": [".exe", ".msi"],
            "illustrator": [".ai"],
            "photoshop": [".psd", ".psb"],
            "music": [".mp3", ".wav", ".flac", ".aac"],
        }

        for filename in os.listdir(folder):
            if os.path.isfile(os.path.join(folder, filename)):
                file_extension = os.path.splitext(filename)[1].lower()
                for category, extensions in file_types.items():
                    if file_extension in extensions:
                        category_folder = os.path.join(folder, category)
                        os.makedirs(category_folder, exist_ok=True)
                        shutil.move(os.path.join(folder, filename), os.path.join(category_folder, filename))
                        break

def add_context_menu():
    key_path = r"Directory\shell\RearrangeFiles"
    try:
        key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, key_path)
        winreg.SetValueEx(key, "", 0, winreg.REG_SZ, "Rearrange Files")
        winreg.SetValueEx(key, "Icon", 0, winreg.REG_SZ, os.path.abspath(sys.argv[0]))

        command_key = winreg.CreateKey(key, r"command")
        winreg.SetValueEx(command_key, "", 0, winreg.REG_SZ, f'"{sys.executable}" "{os.path.abspath(sys.argv[0])}" "%1"')
        winreg.CloseKey(key)
        winreg.CloseKey(command_key)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add context menu: {e}")

def remove_context_menu():
    key_path = r"Directory\shell\RearrangeFiles"
    try:
        winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, key_path)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to remove context menu: {e}")

def main():
    if len(sys.argv) > 1:
        folder_path = sys.argv[1]
        try:
            app = FolderWiz(tk.Tk())
            app.organize_files(folder_path)
            messagebox.showinfo("Success", "Files rearranged successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        root = tk.Tk()
        app = FolderWiz(root)
        root.protocol("WM_DELETE_WINDOW", lambda: on_close(root))
        add_context_menu()
        root.mainloop()

def on_close(root):
    remove_context_menu()
    root.destroy()

if __name__ == "__main__":
    main()

import os
import shutil
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class RenamerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Safe Bulk File Renamer")
        
        self.source_dir = tk.StringVar()
        self.dest_dir = tk.StringVar()
        self.prefix = tk.StringVar()
        self.suffix = tk.StringVar()
        self.start_num = tk.IntVar()
        self.start_num.set(1)
        
        self.create_widgets()
    
    def create_widgets(self):
        # Directory selection
        ttk.Label(self.master, text="Source Directory:").grid(row=0, column=0, sticky="w")
        ttk.Entry(self.master, textvariable=self.source_dir, width=40).grid(row=0, column=1)
        ttk.Button(self.master, text="Browse", command=self.browse_source).grid(row=0, column=2)
        
        ttk.Label(self.master, text="Destination Directory:").grid(row=1, column=0, sticky="w")
        ttk.Entry(self.master, textvariable=self.dest_dir, width=40).grid(row=1, column=1)
        ttk.Button(self.master, text="Browse", command=self.browse_dest).grid(row=1, column=2)
        
        # Renaming options
        ttk.Label(self.master, text="Prefix:").grid(row=2, column=0, sticky="w")
        ttk.Entry(self.master, textvariable=self.prefix).grid(row=2, column=1, sticky="ew")
        
        ttk.Label(self.master, text="Suffix:").grid(row=3, column=0, sticky="w")
        ttk.Entry(self.master, textvariable=self.suffix).grid(row=3, column=1, sticky="ew")
        
        ttk.Label(self.master, text="Start Number:").grid(row=4, column=0, sticky="w")
        ttk.Spinbox(self.master, from_=1, to=1000, textvariable=self.start_num).grid(row=4, column=1, sticky="w")
        
        # Action buttons
        ttk.Button(self.master, text="Preview", command=self.preview).grid(row=5, column=0, pady=10)
        ttk.Button(self.master, text="Rename", command=self.rename).grid(row=5, column=1, pady=10)
        ttk.Button(self.master, text="Quit", command=self.master.quit).grid(row=5, column=2, pady=10)
    
    def browse_source(self):
        directory = filedialog.askdirectory()
        if directory:
            self.source_dir.set(directory)
    
    def browse_dest(self):
        directory = filedialog.askdirectory()
        if directory:
            self.dest_dir.set(directory)
    
    def preview(self):
        if not self.validate_inputs():
            return
        
        source = self.source_dir.get()
        files = [f for f in os.listdir(source) if os.path.isfile(os.path.join(source, f))]
        
        preview = []
        num = self.start_num.get()
        for file in files:
            name, ext = os.path.splitext(file)
            new_name = f"{self.prefix.get()}{name}{self.suffix.get()}{ext}"
            preview.append(f"{file} → {new_name}")
        
        messagebox.showinfo("Preview", "\n".join(preview))
    
    def rename(self):
        if not self.validate_inputs():
            return
        
        source = self.source_dir.get()
        dest = self.dest_dir.get()
        files = [f for f in os.listdir(source) if os.path.isfile(os.path.join(source, f))]
        
        num = self.start_num.get()
        for file in files:
            name, ext = os.path.splitext(file)
            new_name = f"{self.prefix.get()}{name}{self.suffix.get()}{ext}"
            shutil.move(os.path.join(source, file), os.path.join(dest, new_name))
        
        messagebox.showinfo("Success", f"Renamed {len(files)} files successfully!")
    
    def validate_inputs(self):
        if not self.source_dir.get():
            messagebox.showerror("Error", "Source directory is required")
            return False
        if not self.dest_dir.get():
            messagebox.showerror("Error", "Destination directory is required")
            return False
        return True

if __name__ == "__main__":
    root = tk.Tk()
    app = RenamerApp(root)
    root.mainloop()
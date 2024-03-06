import tkinter as tk
from tkinter import filedialog, messagebox

# Function to scan a file for predefined malware signatures
def scan_file(file_path):
    # Predefined malware signatures
    malware_signatures = ['.exe', '.mrf', '.bat']

    # Open the file and read its content
    try:
        with open(file_path, 'rb') as file:
            content = file.read()

        # Check if any malware signatures are present in the file content
        for signature in malware_signatures:
            if signature.encode() in content:
                messagebox.showwarning("Virus Detected", f"Virus detected: {signature}")
                return
        messagebox.showinfo("Scan Completed", "File is clean. No viruses detected.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while scanning the file: {e}")

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_label.config(text="Selected File: " + file_path)
        scan_file(file_path)

def create_gui():
    window = tk.Tk()
    window.title("Professional Antivirus App")
    window.geometry("400x200")

    label = tk.Label(window, text="Welcome to the Antivirus App", font=("Arial", 14))
    label.pack(pady=20)

    select_button = tk.Button(window, text="Select File", command=select_file)
    select_button.pack()

    global file_label
    file_label = tk.Label(window, text="Selected File: ", wraplength=300)
    file_label.pack()

    window.mainloop()

if __name__ == "__main__":
    create_gui()

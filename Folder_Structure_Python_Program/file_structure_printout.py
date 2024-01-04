import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def print_folder_structure(folder_path, indent=0, output_file=None):
    folder_name = os.path.basename(folder_path)
    indentation = '  ' * indent
    output = f"{indentation}- {folder_name}\n"

    if output_file is None:
        print(output, end='')
    else:
        output_file.write(output)

    if os.path.isdir(folder_path):
        subfolders = sorted(os.listdir(folder_path))
        for subfolder in subfolders:
            subfolder_path = os.path.join(folder_path, subfolder)
            if os.path.isdir(subfolder_path):
                print_folder_structure(subfolder_path, indent=indent + 1, output_file=output_file)

def browse_folder():
    folder_path = filedialog.askdirectory()
    target_folder_entry.delete(0, tk.END)
    target_folder_entry.insert(tk.END, folder_path)

def browse_output_location():
    output_location = filedialog.asksaveasfilename(defaultextension='.txt', initialfile='Folder_Structure_Output.txt')
    output_location_entry.delete(0, tk.END)
    output_location_entry.insert(tk.END, output_location)

def run_program():
    folder_path = target_folder_entry.get()
    output_file_path = output_location_entry.get()

    with open(output_file_path, 'w') as output_file:
        print_folder_structure(folder_path, output_file=output_file)

    messagebox.showinfo('Program Finished', 'Folder structure printed successfully!')

def exit_program():
    root.destroy()

root = tk.Tk()
root.title('Folder Structure Printer')

target_folder_label = tk.Label(root, text='Target Folder:')
target_folder_label.pack()

target_folder_entry = tk.Entry(root, width=50)
target_folder_entry.pack()

browse_folder_button = tk.Button(root, text='Browse', command=browse_folder)
browse_folder_button.pack()

output_location_label = tk.Label(root, text='Output Location:')
output_location_label.pack()

output_location_entry = tk.Entry(root, width=50)
output_location_entry.pack()

browse_output_location_button = tk.Button(root, text='Browse', command=browse_output_location)
browse_output_location_button.pack()

run_button = tk.Button(root, text='Run', command=run_program)
run_button.pack()

exit_button = tk.Button(root, text='Exit', command=exit_program)
exit_button.pack()

root.mainloop()
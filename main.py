import tkinter as tk
import psutil
import platform
import subprocess

def get_specs():
    # Get CPU name
    cpu = platform.processor()
    
    # Get GPU names
    try:
        gpu_info = subprocess.check_output("wmic path win32_videocontroller get name", shell=True).decode().splitlines()
        gpus = [gpu.strip() for gpu in gpu_info if gpu.strip() and gpu.strip() != "Name"]
    except Exception as e:
        gpus = ["Error fetching GPU information"]

    # Get RAM details
    ram_total = round(psutil.virtual_memory().total / (1024 ** 3), 2)  # in GB
    ram_used = round(psutil.virtual_memory().used / (1024 ** 3), 2)    # in GB

    # Update specs display
    specs_display = f"Cpu:\n{cpu}\n\nGpu1:\n{gpus[0] if len(gpus) > 0 else 'N/A'}\nGpu2:\n{gpus[1] if len(gpus) > 1 else 'N/A'}\n\nRam:\n{ram_total} GB\nRam Used:\n{ram_used} GB"
    specs_label.config(text=specs_display)
    
    # Hide the button and expand the specs box
    check_button.pack_forget()
    specs_frame.pack(expand=True, fill=tk.BOTH)

# Create the main window
root = tk.Tk()
root.title("System Specs Checker")
root.geometry("600x400")  # Set a larger window size
root.configure(bg='black')

# Create a frame for styling
frame = tk.Frame(root, bg='black', bd=10)
frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

# Create a frame for the specs display
specs_frame = tk.Frame(frame, bg='grey', bd=5)
specs_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Create a label to display the specs
specs_label = tk.Label(specs_frame, text="", bg='grey', fg='black', font=('Arial', 14), justify=tk.LEFT)
specs_label.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

# Create a button to check specs
check_button = tk.Button(frame, text="Check Specs", command=get_specs, bg='blue', fg='white', font=('Arial', 20), height=2, width=15)
check_button.pack(pady=20)

# Start the GUI loop
root.mainloop()

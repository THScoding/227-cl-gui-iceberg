import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
from tkinter import ttk
import time
import threading

# do_command function for all buttons
def do_command(command):
    global command_textbox, url_entry

    # If url_entry is blank, use localhost IP address 
    url_val = url_entry.get()
    if (len(url_val) == 0):
        # url_val = "127.0.0.1"
        url_val = "::1"
        
    if command == "ipconfig":
      url_val = " "
    
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()

    with subprocess.Popen(command + ' ' + url_val, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True) as p:
        for line in p.stdout:
            command_textbox.insert(tk.END,line)
            command_textbox.update()

# Save function
def mSave(progressbar, start_button):
  
  # get file type (checked by radiobuttons)
  selected_type = file_type_variable.get()
  
  if selected_type == ".txt":
    filetypes = [("Text Files", "*.txt"), ("All files", "*.*")]
    defaultextension = ".txt"
  elif selected_type == ".py":
    filetypes = [("Python File", ".py"), ("All files", "*.*")]
    defaultextension = ".py"
  elif (selected_type == "*.*"):
    filetypes = [("All Files", "*.*")]
    defaultextension = "*.*"
  
  # Saves file according to file type
  filename = asksaveasfilename(defaultextension = defaultextension, filetypes = filetypes)
  if filename is None:
    return
  file = open (filename, mode = 'w')
  text_to_save = command_textbox.get("1.0", tk.END)
  
  thread = threading.Thread(target=start_task, args=(progressbar, start_button))
  thread.start()
  
  file.write(text_to_save)
  file.close()

# Main window

root = tk.Tk()
root.wm_geometry("1200x650")
root.configure(bg = "LightCyan2")
root.title("Command Line Tools")
frame = tk.Frame(root)
frame.pack()

# creates the frame with label for the input text box
frame_URL = tk.Frame(root, pady=20,  bg="LightCyan2") # change frame color
frame_URL.pack()

# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
    compound="center",
    font=("comic sans", 14),
    bd=0, 
    relief=tk.FLAT, 
    fg="black",
    bg="LightCyan2")
url_label.pack(side=tk.LEFT, pady = 20)
url_entry= tk.Entry(frame_URL,  font=("comic sans", 14)) # change font
url_entry.pack(side=tk.LEFT, pady = 20)

# input frame
input_frame = tk.Frame(root,  bg="LightCyan2") # change frame color
input_frame.pack()

# set up button to run the do_command function
# Makes the command button pass its name to a function using lambda

# ping button
ping_btn = tk.Button(input_frame, text="Check if a URL is up and active", 
    command=lambda:do_command("ping"),
    compound="center",
    width = 25,
    font=("comic sans", 12),
    bd=2, 
    relief = tk.RAISED,
    bg="thistle2", activebackground="thistle4")
ping_btn.pack(side = tk.LEFT, padx = 20) 

# tracert button
tracert_btn = tk.Button(input_frame, text="Map how data packets travel", 
    command=lambda:do_command("tracert"),
    compound="center",
    width = 25,
    font=("comic sans", 12),
    bd=2, 
    relief = tk.RAISED,
    bg="thistle2", activebackground="thistle4")
tracert_btn.pack(side = tk.LEFT, padx = 20) 

# nslookup button
nslookup_btn = tk.Button(input_frame, text="Retrieve DNS data", 
    command=lambda:do_command("nslookup"),
    compound="center",
    width = 25,
    font=("comic sans", 12),
    bd=2, 
    relief = tk.RAISED,
    bg="thistle2", activebackground="thistle4")
nslookup_btn.pack(side = tk.LEFT, padx = 20) 

# ipconfig button
ipconfig_btn = tk.Button(input_frame, text="Display IP network configuration", 
    command=lambda:do_command("ipconfig"),
    compound="center",
    width = 25,
    font=("comic sans", 12),
    bd=2, 
    relief = tk.RAISED,
    bg="thistle2", activebackground="thistle4")
ipconfig_btn.pack(side = tk.LEFT, padx = 20) 

# output frame
output_frame = tk.Frame(root,  bg="LightCyan2") # change frame color
output_frame.pack()

# Adds an output box to GUI.
command_textbox = tksc.ScrolledText(output_frame, height=15, width=100)
command_textbox.pack(pady = 30)

# ----- Radiobuttons -----

# default file type to .txt
file_type_variable = tk.StringVar(value = ".txt")

# Creates radiobuttons
txt_button = tk.Radiobutton(output_frame, text = "Text (.txt)", width = 10, variable = file_type_variable, value = ".txt")
txt_button.pack()

py_button = tk.Radiobutton(output_frame, text = "Python (.py)", width = 10, variable = file_type_variable, value = ".py")
py_button.pack()

all_button = tk.Radiobutton(output_frame, text = "All Files (*.*)", width = 10, variable = file_type_variable, value = "*.*")
all_button.pack()

# ----- Progress Bar -----

def start_task(progressbar, start_button):
    """Simulates a task and updates the progress bar."""
    start_button['state'] = 'disabled' # Disable button during task
    progressbar['value'] = 0
    max_value = 100
    progressbar['maximum'] = max_value


    for i in range(max_value + 1):
        time.sleep(0.03) # Simulate work
        progressbar['value'] = i
        # Update the GUI to show the current progress
        progressbar.update_idletasks()

    start_button['state'] = 'normal' # Re-enable button after task
    print("Task Complete!")

# Progress bar widget
progress_bar = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate')
progress_bar.pack(pady=20)

# Save button
# The command calls on_start_button_click and passes the progress bar and button as arguments
save_button = tk.Button(root, text="Start Download", command=lambda: mSave(progress_bar, save_button))
save_button.pack(pady=10)

root.mainloop()

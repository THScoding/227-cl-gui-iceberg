import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

'''def do_command():
    command = ["ping", "localhost"]
    # Windows version to limit to 4 requests: command = ["ping", "localhost", "-n", "4"]
    # Mac version to limit to 4 requests:     command = ["ping", "localhost", "-n", "4"]
    
    subprocess.run(command)'''

# Modify the do_command function:
# to use the new button as needed
def do_command(command):
    global command_textbox, url_entry

    # If url_entry is blank, use localhost IP address 
    url_val = url_entry.get()
    if (len(url_val) == 0):
        # url_val = "127.0.0.1"
        url_val = "::1"
    
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()

    with subprocess.Popen(command + ' ' + url_val, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True) as p:
        for line in p.stdout:
            command_textbox.insert(tk.END,line)
            command_textbox.update()

# Save function.
def mSave():
  filename = asksaveasfilename(defaultextension='.txt',filetypes = (('Text files', '*.txt'),('Python files', '*.py *.pyw'),('All files', '*.*')))
  if filename is None:
    return
  file = open (filename, mode = 'w')
  text_to_save = command_textbox.get("1.0", tk.END)
  
  file.write(text_to_save)
  file.close()

# Main window

root = tk.Tk()
root.wm_geometry("1000x600")
root.configure(bg = "LightCyan2")
frame = tk.Frame(root)
frame.pack()

# creates the frame with label for the input text box
frame_URL = tk.Frame(root, pady=10,  bg="LightCyan2") # change frame color
frame_URL.pack()

# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
    compound="center",
    font=("comic sans", 14),
    bd=0, 
    relief=tk.FLAT, 
    fg="black",
    bg="LightCyan2")
url_label.pack(side=tk.LEFT)
url_entry= tk.Entry(frame_URL,  font=("comic sans", 14)) # change font
url_entry.pack(side=tk.LEFT)

frame = tk.Frame(root,  bg="LightCyan2") # change frame color
frame.pack()

# set up button to run the do_command function
# Makes the command button pass it's name to a function using lambda

# ping button
ping_btn = tk.Button(frame, text="Check if a URL is up and active", 
    command=lambda:do_command("ping"),
    compound="center",
    font=("comic sans", 12),
    bd=0, 
    relief="flat",
    bg="thistle2", activebackground="thistle4")
ping_btn.pack() 

# tracert button
tracert_btn = tk.Button(frame, text="Map how data packets travel", 
    command=lambda:do_command("tracert"),
    compound="center",
    font=("comic sans", 12),
    bd=0, 
    relief="flat",
    bg="thistle2", activebackground="thistle4")
tracert_btn.pack() 

# nslookup button
nslookup_btn = tk.Button(frame, text="Retrieve DNS data", 
    command=lambda:do_command("nslookup"),
    compound="center",
    font=("comic sans", 12),
    bd=0, 
    relief="flat",
    bg="thistle2", activebackground="thistle4")
nslookup_btn.pack() 

# nmap button
nmap_btn = tk.Button(frame, text="Find live hosts, devices, and connections", 
    command=lambda:do_command("nmap"),
    compound="center",
    font=("comic sans", 12),
    bd=0, 
    relief="flat",
    bg="thistle2", activebackground="thistle4")
nmap_btn.pack() 

# Adds an output box to GUI.
command_textbox = tksc.ScrolledText(frame, height=10, width=100)
command_textbox.pack()


root.mainloop()

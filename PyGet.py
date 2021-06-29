from tkinter import *
from tkinter import messagebox
import os, platform, subprocess as sp, sys

# We want to create a new window
root = Tk()
root.title("PyGet - Pip GUI")
root.config(bg='#3d3d3d')
root.geometry("500x400")

# We decided that it can remain resizable
#root.resizable(0, 0)

# Find os name
osname = platform.system()

# Check for osname, and change the PIP command
# If this doesnt work on your operating system. Please open a github issue
if osname == "Linux": execc = "python3 -m pip"
elif osname == "Windows": execc = "pip"
elif osname == "Darwin": exec = "pip"
elif osname == "Java":
    # I dont know the pip command (or even if python is supported) on Java based platforms.
    messagebox.showerror("Unsupported OS?", f"Java based Plaforms are not supported by PyGet?")
    sys.exit()
else:
    # IDK if python supports any other OS
    messagebox.showerror("Unsupported OS?", f"{osname} OS/Platform is not suppored by PyGet?")
    sys.exit()

print(execc)

# Define some help text
help_text = """PyGet is an GUI for pip, pythons package manager. PyGet allows you to:
- Install PIP moudles
- Execute pip commands
- Show this help message"""

# Create an input box
inputs = Entry(root, bg='#808080', fg='black', bd=0, state=DISABLED)
inputs.config(font=('Consolas', 16), selectbackground='lightblue')
inputs.config(selectforeground='black', highlightthickness=0)
inputs.pack(fill='x', side='bottom', ipady=3, ipadx=3)

# Header
header = Label(root, bg='#3d3d3d', text='PyGet - Pip GUI', fg='white')
header.config(font=('arab', 26))
header.pack(fill='x', padx=5, pady=5)

# Now the frame
frames = Frame(root, bg='#808080', bd=0)
frames.pack(anchor='center')

def hidexe():
    output.config(state=NORMAL)
    inputs.config(state=NORMAL)
    output.delete(1.0, END)
    inputs.config(state=DISABLED)
    output.config(state=DISABLED)
    exec_btn.config(command=execWpip)

def executeThePip(e):
    global output
    pip_cmd_out = str(sp.getoutput(f"{execc} {inputs.get()}"))

    output.pack(fill='x', expand=1, pady=5, padx=5)
    output.config(state=NORMAL)
    output.delete(1.0, END)
    output.insert(1.0, pip_cmd_out)
    output.config(state=DISABLED)
    inputs.config(state=DISABLED)

    exec_btn.config(command=hidexe)

    print(pip_cmd_out)

# An pip exec function
def execWpip():
    inputs.config(state=NORMAL)
    inputs.bind("<Return>", executeThePip)

# Hide view
def hideView():
    output.pack_forget()
    output.config(state=DISABLED)
    view_btn.config(command=pip_view)

# View function
def pip_view():
    global output
    ls_out = str(sp.getoutput(f"{execc} list"))

    output.pack(fill='x', expand=1, pady=5, padx=5)
    output.config(state=NORMAL)
    output.delete(1.0, END)
    output.insert(1.0, ls_out)
    output.config(state=DISABLED)

    view_btn.config(command=hideView)

# hide pip
def hidePip():
    global output, inputs
    output.pack_forget()
    output.config(state=DISABLED)
    inputs.config(state=DISABLED)

    install_btn.config(command=install)

# execute pip
def exec_pip(e):
    global output
    exec_out = str(sp.getoutput(f"{execc} install {inputs.get()}"))

    output.pack(fill='x', expand=1, pady=5, padx=5)
    output.config(state=NORMAL)
    output.delete(1.0, END)
    output.insert(1.0, exec_out)
    output.config(state=DISABLED)

    install_btn.config(command=hidePip)

    print(exec_out)

# install function
def install():
    inputs.config(state=NORMAL)
    inputs.bind("<Return>", exec_pip)

# Hide help
def hideHelp():
    output.pack_forget()
    output.config(state=NORMAL)
    output.delete(1.0, END)
    output.config(state=DISABLED)

    help_btn.config(command=getHelp)

# Help function
def getHelp():
    output.pack(fill='x', expand=1, pady=5, padx=5)
    output.config(state=NORMAL)
    output.insert(1.0, help_text)
    output.config(state=DISABLED)
    help_btn.config(command=hideHelp)

# Install button
install_btn = Button(frames, bg='#808080', text='Install', bd=0, fg='white', command=install)
install_btn.configure(highlightthickness=0, font=('Consolas', 18))
install_btn.config(activebackground='#808080', activeforeground='#1a1a1a')
install_btn.grid(row=0, column=0, ipady=1, ipadx=1, sticky='w', padx=8)

# Help button
help_btn = Button(frames, bg='#808080', text='Help', bd=0, fg='white', command=getHelp)
help_btn.configure(highlightthickness=0, font=('Consolas', 18))
help_btn.config(activebackground='#808080', activeforeground='#1a1a1a')
help_btn.grid(row=0, column=1, ipady=1, ipadx=1, sticky='e', padx=8)

# View button
view_btn = Button(frames, bg='#808080', text='View', bd=0, fg='white', command=pip_view)
view_btn.configure(highlightthickness=0, font=('Consolas', 18))
view_btn.config(activebackground='#808080', activeforeground='#1a1a1a')
view_btn.grid(row=0, column=3, ipady=1, ipadx=1, sticky='e', padx=8)

# Execute command
exec_btn = Button(frames, bg='#808080', text='PIP', bd=0, fg='white', command=execWpip)
exec_btn.configure(highlightthickness=0, font=('Consolas', 18))
exec_btn.config(activebackground='#808080', activeforeground='#1a1a1a')
exec_btn.grid(row=0, column=4, ipady=1, ipadx=1, sticky='e', padx=8)

# Output
output = Text(root, bg='#3d3d3d', bd=0, font=('Arab', 14), selectforeground='white')
output.config(highlightthickness=0, selectbackground='#3d3d3d', fg='white', state=DISABLED, wrap=WORD)

# Mainloop
if __name__ == "__main__":
    try:
        root.mainloop()
    except EOFError: pass
    except KeyboardInterrupt: pass

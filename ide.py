from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import subprocess
import main  # Import the MainCompiler from your compiler module

# Create the main window for the app and set its title
window = Tk()
window.title('Group 8s IDE')

# Make the window full screen
window.attributes('-fullscreen', True)

# Global variable to store the path of the file being worked on
gpath = ''

# Function to run the Python code written in the text editor
def runMyCode():
    global gpath
    if gpath == '':  # If no file is open or saved, show a message
        saveMsg = Toplevel()  # Create a new popup window
        msg = Label(saveMsg, text="Please save the file first")  # Display this message
        msg.pack()  # Pack the message into the window
        return  # Exit the function if no file is saved

    # Get the code from the editor for compiling
    code = textEditor.get('1.0', END)
    compiler = main(code)  # Create a MainCompiler instance with the code
    compiler.compile()  # Compile the code

    # Display the result in the output box
    output.delete('1.0', END)  # Clear previous output
    output.insert('1.0', "Compilation finished. Check terminal for errors.")  # Update output box

# Function to open an existing Python file
def openMyFile():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])  # Open a file dialog to select a Python file
    with open(path, 'r') as file:  # Open the selected file in read mode
        code = file.read()  # Read the content of the file
        textEditor.delete('1.0', END)  # Clear the current text in the editor
        textEditor.insert('1.0', code)  # Insert the code from the file into the text editor
        updateLineNumbers()  # Update line numbers when a file is opened
        global gpath
        gpath = path  # Store the file path globally for future access (e.g., when saving or running)

# Function to save the file (either to the existing file or as a new file)
def saveMyFileAs():
    global gpath
    if gpath == '':  # If no file is open, ask the user where to save it
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:  # If a file is already open, use that path
        path = gpath    
    with open(path, 'w') as file:  # Open the file in write mode
        code = textEditor.get('1.0', END)  # Get the current code from the text editor
        file.write(code)  # Write the code to the file

# Function to update line numbers
def updateLineNumbers(event=None):
    lineNumbers.config(state='normal')  # Enable the lineNumbers widget
    lineNumbers.delete('1.0', END)  # Clear current line numbers
    lines = textEditor.index('end').split('.')[0]  # Get the total number of lines
    lineNumbersText = "\n".join(str(i) for i in range(1, int(lines)))  # Create line numbers from 1 to the last line
    lineNumbers.insert('1.0', lineNumbersText)  # Insert the line numbers
    lineNumbers.config(state='disabled')  # Disable the lineNumbers widget to prevent user edits

# Sync scrolling between line numbers and text editor
def onScroll(*args):
    textEditor.yview(*args)
    lineNumbers.yview(*args)

# Frame to contain both the line numbers and the text editor
editorFrame = Frame(window)
editorFrame.pack(expand=True, fill='both')

# Line numbers text widget (non-editable)
lineNumbers = Text(editorFrame, width=4, padx=5, takefocus=0, bg='black', fg='white')
lineNumbers.pack(side='left', fill='y')

# Text editor for writing code, with custom colors for background, text, and cursor
textEditor = Text(editorFrame, undo=True, bg='white', fg='black', insertbackground='black')
textEditor.pack(side='left', expand=True, fill='both')

# Bind the text editor to the function that updates line numbers
textEditor.bind('<KeyRelease>', updateLineNumbers)
textEditor.bind('<MouseWheel>', updateLineNumbers)

# Sync the scrolling between line numbers and text editor
textEditor.config(yscrollcommand=lambda *args: onScroll(*args))
lineNumbers.config(yscrollcommand=lambda *args: onScroll(*args))

# Text widget for displaying the output or errors, with custom colors
output = Text(height=2)  # Set the height of the output widget
output.config(bg='black', fg='#1dd604')  # Set background and text color for the output
output.pack(expand=True, fill='both')  # Allow the output widget to expand and fill the window

# Creating a menu bar at the top of the window
menuBar = Menu(window)

# Creating the "File" menu with options to open, save, save as, and exit
fileBar = Menu(menuBar, tearoff=0)
fileBar.add_command(label='Open', command=openMyFile)  # Option to open a file
fileBar.add_command(label='Save', command=saveMyFileAs)  # Option to save the current file
fileBar.add_command(label='SaveAs', command=saveMyFileAs)  # Option to save the file as a new file
fileBar.add_command(label='Exit', command=exit)  # Option to exit the program
menuBar.add_cascade(label='File', menu=fileBar)  # Add the "File" menu to the menu bar

# Creating the "Run" menu with an option to run the code
runBar = Menu(menuBar, tearoff=0)
runBar.add_command(label='Run', command=runMyCode)  # Option to run the current code
menuBar.add_cascade(label='Run', menu=runBar)  # Add the "Run" menu to the menu bar

# Configure the window to use the created menu bar
window.config(menu=menuBar)

# Start the Tkinter main loop to display the window and keep the app running
window.mainloop()

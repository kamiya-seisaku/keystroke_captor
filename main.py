import tkinter as tk

# Initialize the Tkinter window
root = tk.Tk()
root.title("Refined Keystroke App with Clipboard")

# Initialize variables
keystrokes = ""
modifier = ""

# Function to handle keystrokes
def on_key(event):
    global keystrokes, modifier
    if event.keysym == 'Escape':
        root.quit()
    else:
        if event.keysym in ['Shift_L', 'Shift_R', 'Control_L', 'Control_R', 'Alt_L', 'Alt_R']:
            modifier = event.keysym + "+"
        else:
            if len(keystrokes.split(',')) < 10:
                combined_key = f"{modifier}{event.keysym}"
                keystrokes += f"{combined_key}, "
                label.config(text=f"Keystrokes: {keystrokes}")
                root.clipboard_clear()
                root.clipboard_append(keystrokes)
                root.update()  # Now it stays on the clipboard after the window is closed
            modifier = ""

# Create a label to display the keystrokes
label = tk.Label(root, text="Keystrokes: ")
label.pack()

# Bind the key event to the root window
root.bind("<Key>", on_key)

# Run the Tkinter event loop
root.mainloop()

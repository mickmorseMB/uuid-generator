import tkinter as tk

# Create the Window
window = tk.Tk()
window.title('Unique: The UUID Generator')
window.iconbitmap('./icon/icon.ico')
window.geometry("512x256")

# Create the Top Menu Bar
menuBar = tk.Menu(window)
fileMenu = tk.Menu(menuBar,tearoff=0)
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save")
fileMenu.add_command(label="Save As...")
fileMenu.add_separator()
fileMenu.add_command(label="Exit")
menuBar.add_cascade(label="File", menu=fileMenu)
uuidMenu = tk.Menu(menuBar,tearoff=0)
uuidMenu.add_command(label="Version 0")
uuidMenu.add_command(label="Version 1")
uuidMenu.add_command(label="Version 4")
uuidMenu.add_separator()
uuidMenu.add_command(label="Version 3")
uuidMenu.add_command(label="Version 5")
menuBar.add_cascade(label="Generate UUIDs", menu=uuidMenu)
window.config(menu=menuBar)

# Start the Window Main Loop
window.mainloop()